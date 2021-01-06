# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class EggsHunt(models.Model):
    _inherit = 'eggs.hunt'
    _check_company_auto = True

    result_type = fields.Selection([
        ('google_doc', 'Google Doc'), ('text', 'Text')],
        string="Work Sheet", default="text",
        help="Defines if you want to use a PDF or a Google Slide as work sheet."
    )
    note = fields.Text('Description', help="Text results description")
    result_google_doc = fields.Char('Google Doc',
                                    help="Paste the url of your Google Doc. Make sure the access to the document is public.")
    last_change_date_time = fields.Datetime('Last Change', readonly=True)
    organizer_id = fields.Many2one('res.partner', readonly=False, tracking=True, string='Organizer',
                                   states={'done': [('readonly', True)]})

    results = fields.Selection([("none", ""), ("individual", "Individual"), ("family", "Family"), ("both", "Individual and Family")],
                               string="Results", default='none')

    result_ids = fields.One2many('eggs.hunt.results', 'hunt_id', string="Result")

    signature = fields.Binary(string='Organizer Signature')
    signed_by = fields.Many2one('res.partner', string='Signed By', help='Name of the person that signed.', copy=False, compute='_compute_signed_by')
    signed_on = fields.Datetime(string='Signed On', help='Date of the signature.', copy=False)

    @api.depends('organizer_id')
    def _compute_signed_by(self):
        for record in self:
            record.signed_by = self.organizer_id


    def action_individual_results(self):
        for record in self:
            record.signed_on = False
            record.signature = False
            record.state = 'results'
            record.result_ids.unlink()
            for child in record.child_ids:
                child_name = child.display_name
                egg_count = len(child.egg_ids)
                self.env['eggs.hunt.results'].create({'hunt_id': record.id,
                                          'name': child_name,
                                          'egg_count': egg_count})


    def action_family_results(self):
        for record in self:
            self.env['eggs.hunt'].search([('id', '=', record.id)]).child_ids.unlink()
            self.env['eggs.hunt.line'].search([('hunt_id', '=', record.id)]).unlink()
            self.env['eggs.hunt.line.color'].search([('hunt_id', '=', record.id)]).unlink()
            attachments = self.env['ir.attachment'].search([('res_model', '=', 'eggs.hunt'), ('res_id', '=', record.id)])
            if len(attachments) > 1:
                raise UserError(_('There are to many attachments. Please attach one csv file.'))
            try:
                attachment_id = \
                    self.env['ir.attachment'].search([('res_model', '=', 'eggs.hunt'), ('res_id', '=', record.id)])[0]
            except:
                raise UserError(_('There is no attachment. Please attach a csv file.'))
            if attachment_id.name[-4:] != '.csv':
                raise UserError(_('Your file is not in requested format. Please attach one csv file.'))
            imported_str = str(attachment_id.raw)
            new_str = imported_str.replace("\\n", ";")
            no_b_str = new_str.replace("b\'", "")
            clean_str = no_b_str.replace("\'", "")
            lista = clean_str.split(';')
            no_headings_list = lista[2:-1]
            index = 0
            for element in range(len(no_headings_list)):
                name = no_headings_list[element]
                if index % 2 == 0:
                    if len(self.env['res.partner'].search([('name', '=', name)])) == 0:
                        partner = self.env['res.partner'].create({'name': name, 'is_participant': True})
                        self.env['mail.followers'].create(
                            {'res_id': record.id, 'res_model': 'eggs.hunt', 'partner_id': partner.id, 'name': partner.name,
                             'display_name': partner.name})
                    else:
                        partner = self.env['res.partner'].search([('name', '=', name)])[0]
                        followers = self.env['mail.followers'].search(
                            [('res_id', '=', record.id), ('res_model', '=', 'eggs.hunt')])
                        is_follower = False
                        for follower in followers:
                            if partner.id == follower.partner_id.id:
                                is_follower = True
                        if is_follower == False:
                            self.env['mail.followers'].create(
                                {'res_id': record.id, 'res_model': 'eggs.hunt', 'partner_id': partner.id,
                                 'name': partner.name, 'display_name': partner.name})
                elif index % 2 == 1:
                    colors_list = no_headings_list[index].split(',')
                    count = 0
                    line = self.env['eggs.hunt.line'].create({'hunt_id': record.id, 'partner_id': partner.id})
                    for name in colors_list:
                        count += 1
                        if len(self.env['egg.color'].search([('name', '=', name)])) == 0:
                            color = self.env['egg.color'].create({'name': name})
                            line_color = self.env['eggs.hunt.line.color'].create(
                                {'color_id': color.id, 'child_id': line.id, 'hunt_id': record.id})
                        else:
                            color = self.env['egg.color'].search([('name', '=', name)])[0]
                            line_color = self.env['eggs.hunt.line.color'].create(
                                {'color_id': color.id, 'child_id': line.id, 'hunt_id': record.id})
                    line_color_ids = self.env['eggs.hunt.line.color'].search(
                        [('child_id', '=', line.id), ('hunt_id', '=', record.id)])
                    record.child_ids.search([('partner_id', '=', partner.id), ('hunt_id', '=', record.id)]).write(
                        {'egg_ids': [(6, 0, line_color_ids.ids)]})
                index += 1
            record.signed_on = False
            record.signature = False
            res = super(EggsHunt, self).action_family_results()
            return res

    @api.model
    def create(self, vals):
        vals['last_change_date_time'] = fields.Datetime.now()
        if 'signature' in vals:
            vals['signed_on'] = fields.Datetime.now()
        res = super(EggsHunt, self).create(vals)
        return res

    def write(self, vals):
        vals['last_change_date_time'] = fields.Datetime.now()
        if 'signature' in vals and vals['signature'] != False:
            vals['signed_on'] = fields.Datetime.now()
        res = super(EggsHunt, self).write(vals)
        return res

    def action_draft(self):
        for record in self:
            record.results = 'none'
            res = super(EggsHunt, self).action_draft()
            return res


    def action_done(self):
        for record in self:
            if record.signature == False:
                raise UserError(_('You can not change the state to done, until the results are calculated and signed!'))
            res = super(EggsHunt, self).action_done()
            return res