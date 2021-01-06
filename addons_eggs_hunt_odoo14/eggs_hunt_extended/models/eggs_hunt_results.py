
# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class EggsHuntResults(models.Model):
    _name = 'eggs.hunt.results'
    _description = "Eggs Hunt Results"
    _order = 'egg_count desc'

    hunt_id = fields.Many2one('eggs.hunt', string = 'Hunt')
    name = fields.Char('Name')
    egg_count = fields.Integer('Egg Count')
    user_id = fields.Many2one('res.users', 'Korisnik', default=lambda self: self.env.user)