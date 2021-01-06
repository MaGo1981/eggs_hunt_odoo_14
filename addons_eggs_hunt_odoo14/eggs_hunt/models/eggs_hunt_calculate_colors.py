
# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class EggsHuntCalculateColors(models.Model):
    _name = 'eggs.hunt.calculate.colors'
    _description = "Eggs Hunt Calculate Colors"

    calculate_id = fields.Many2one('eggs.hunt.calculate', string = 'Hunt')
    color_id = fields.Many2one('egg.color', string='Color ID')
    sum = fields.Char('Count')
    user_id = fields.Many2one('res.users', 'Korisnik', default=lambda
        self: self.env.user)
    hunt_id = fields.Many2one('eggs.hunt', string = 'Hunt')
