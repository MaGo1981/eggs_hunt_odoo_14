
# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class EggsHuntColor(models.Model):
    _name = 'eggs.hunt.line.color'
    _description = "Eggs Hunt Line Color"
    _rec_name = 'color_id'

    color_id = fields.Many2one('egg.color', string='Color')
    child_id = fields.Many2one('eggs.hunt.line', string = 'Line')
    user_id = fields.Many2one('res.users', 'Korisnik', default=lambda
        self: self.env.user)
    hunt_id = fields.Many2one('eggs.hunt', string='Hunt')
