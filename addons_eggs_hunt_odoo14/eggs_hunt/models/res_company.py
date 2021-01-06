# -*- coding: utf-8 -*-

from odoo import fields, models


class ResCompanyUpdate(models.Model):
    _inherit = 'res.company'

    hunt_sequence_id = fields.Many2one('ir.sequence')
