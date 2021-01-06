
# -*- coding: utf-8 -*-


from odoo import models, fields, api, _



class EggsHuntLine(models.Model):
    _name = 'eggs.hunt.line'
    _description = "Eggs Hunt Line"
    _rec_name = 'partner_id'

    partner_id = fields.Many2one('res.partner', string = 'Participant')
    hunt_id = fields.Many2one('eggs.hunt', string = 'Hunt')
    year = fields.Selection(related='hunt_id.name', string='Year', readonly=True)
    egg_ids = fields.One2many('eggs.hunt.line.color', 'child_id', string='Eggs')
    user_id = fields.Many2one('res.users', 'Korisnik', default=lambda self: self.env.user)


