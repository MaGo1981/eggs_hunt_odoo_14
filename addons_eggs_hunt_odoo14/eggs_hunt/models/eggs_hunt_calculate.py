
# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class EggsHuntCalculate(models.Model):
    _name = 'eggs.hunt.calculate'
    _description = "Eggs Hunt Calculate"
    _order = 'family_average desc'

    hunt_id = fields.Many2one('eggs.hunt', string = 'Hunt')
    name = fields.Char('Last Name')
    calculation_colors_ids = fields.One2many('eggs.hunt.calculate.colors', 'calculate_id', string="colors")
    person_count = fields.Integer('Person Count')
    egg_count = fields.Integer('Egg Count')
    family_average = fields.Float('Family Average')
    user_id = fields.Many2one('res.users', 'Korisnik', default=lambda
        self: self.env.user)

