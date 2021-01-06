
# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class EggColor(models.Model):
    _name = 'egg.color'
    _description = "Eggs Color"

    name = fields.Char( string='Color')
