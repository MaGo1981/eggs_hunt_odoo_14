# -*- coding: utf-8 -*-
import uuid
from werkzeug.urls import url_encode
from odoo import api, exceptions, fields, models, _
from odoo.exceptions import UserError


class EggsHunt(models.Model):
    _name = 'eggs.hunt'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin', 'utm.mixin']
    _description = "Eggs Hunt"
    _check_company_auto = True

    name_seq = fields.Char(string='Hunt Reference', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    child_ids = fields.One2many('eggs.hunt.line', 'hunt_id', string='Children')
    calculation_ids = fields.One2many('eggs.hunt.calculate', 'hunt_id', string="Calculation")
    user_id = fields.Many2one('res.users', string='User', default=lambda self: self.env.user)

    state = fields.Selection([("draft", "Draft"),
                              ("results", "Results"),
                              ("done", "Done")], "State", default="draft", tracking=True)
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.company)


    @api.model
    def year_selection(self):
        year = 2010
        year_list = []
        while year != 2030:
            year_list.append((str(year), str(year)))
            year += 1
        return year_list

    name = fields.Selection( year_selection, string="Year")

    @api.model
    def create(self, vals):
        sequence_id = self.env.company.hunt_sequence_id
        if sequence_id:
            if vals.get('name_seq', _('New')) == _('New'):
                vals['name_seq'] = sequence_id.next_by_id()
            result = super(EggsHunt, self).create(vals)
            return result
        else:
            raise UserError(_('Please select the sequence for the hunt from Settings menu!'))


    def action_family_results(self):
        for record in self:
            record.state = 'results'
            calculation_dict = {}
            count_dict = {}
            for child in record.child_ids:
                last_name = child.partner_id.name.split(' ')[-1]
                if last_name not in calculation_dict:
                    calculation_dict[last_name] = {}
                    count_dict[last_name] = {}
                    count_dict[last_name]['person_count'] = 1
                    count_dict[last_name]['egg_count'] = 0
                else:
                    count_dict[last_name]['person_count'] += 1
                for color in child.egg_ids[:]:
                    if color.color_id.id not in calculation_dict[last_name]:
                        calculation_dict[last_name][color.color_id.id] = 1
                        count_dict[last_name]['egg_count'] += 1
                    else:
                        calculation_dict[last_name][color.color_id.id] += 1
                        count_dict[last_name]['egg_count'] += 1
            record.calculation_ids.unlink()
            count = 0
            family_average = None
            for last_name in count_dict:
                count_dict[last_name]['family_average'] = count_dict[last_name]['egg_count'] / float(
                    count_dict[last_name]['person_count'])
                family_average = count_dict[last_name]['family_average']
                person_count = count_dict[last_name]['person_count']
                egg_count = count_dict[last_name]['egg_count']
                record.calculation_ids.create({'hunt_id': record.id,
                                               'name': last_name,
                                               'family_average': family_average,
                                               'person_count': person_count,
                                               'egg_count': egg_count})
            for line in calculation_dict:
                count += 1
                count_dict[last_name]['family_average'] = count_dict[last_name]['egg_count'] / float(
                    count_dict[last_name]['person_count'])
            for calculation in record.calculation_ids:
                for color in calculation_dict[calculation.name]:
                    calculation.calculation_colors_ids.create({'calculate_id': calculation.id,
                                                               'hunt_id': record.id,
                                                               'color_id': color,
                                                               'sum': calculation_dict[calculation.name][color]})



    def action_draft(self):
        for record in self:
            record.state = 'draft'
            self.env['eggs.hunt.calculate.colors'].search([('hunt_id', '=', self.id)]).unlink()


    def action_done(self):
        for record in self:
            record.state = 'done'