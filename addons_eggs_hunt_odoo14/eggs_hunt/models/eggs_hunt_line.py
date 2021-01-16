
# -*- coding: utf-8 -*-


from odoo import models, fields, api, _
from odoo.exceptions import ValidationError



class EggsHuntLine(models.Model):
    _name = 'eggs.hunt.line'
    _description = "Eggs Hunt Line"
    _rec_name = 'partner_id'

    partner_id = fields.Many2one('res.partner', string = 'Participant')
    hunt_id = fields.Many2one('eggs.hunt', string = 'Hunt')
    year = fields.Selection(related='hunt_id.name', string='Year', readonly=True)
    egg_ids = fields.One2many('eggs.hunt.line.color', 'child_id', string='Eggs')
    user_id = fields.Many2one('res.users', 'User')

    @api.constrains('user_id')
    def check_user_id(self):
        assigned_users = self.env['eggs.hunt.line'].search([('id', '!=', self.id)]).user_id
        existing_participant_line = self.env['eggs.hunt.line'].search([('partner_id.display_name', '=', self.partner_id.display_name),('id', '!=', self.id)])
        line_users = existing_participant_line.user_id
        for record in self:
            if record.user_id in line_users:
                record.user_id = line_users[0]
                raise ValidationError(_('This participant already has an assigned user {0} on another record.').format(line_users[-1].name))
            elif record.user_id in assigned_users:
                raise ValidationError(_('This user is already assigned to another participant. Please assign another user or create and assign one.'))

    @api.constrains('user_id')
    def check_user_id(self):
        for record in self:
            assigned_lines = self.env['eggs.hunt.line'].search([('id', '!=', record.id)])
            assigned_users = assigned_lines.user_id
            assigned_partners = assigned_lines.partner_id
            existing_participant_line = self.env['eggs.hunt.line'].search([('partner_id.display_name', '=', self.partner_id.display_name),('id', '!=', self.id)])
            line_users = existing_participant_line.user_id
            if len(line_users) > 0 and record.user_id.display_name != line_users[0].display_name and record.user_id.id != False:
                raise ValidationError(_('This participant {1} already has an assigned user {0} on another record. Please assign the same user to this record.').format(line_users[-1].name, existing_participant_line[0].partner_id.name))
            if record.partner_id in assigned_partners:
                id_list=[]
                for id in assigned_partners:
                    id_list.append(id)
                index = id_list.index(record.partner_id)
                if record.partner_id.display_name != assigned_partners[index].display_name:
                    raise ValidationError(_('This user {0} is already assigned to another participant. Please assign another user or create and assign one.').format(record.user_id.display_name))
            elif record.user_id in assigned_users:
                raise ValidationError(_('This user {0} is already assigned to another participant. Please assign another user or create and assign one.').format(record.user_id.display_name))
