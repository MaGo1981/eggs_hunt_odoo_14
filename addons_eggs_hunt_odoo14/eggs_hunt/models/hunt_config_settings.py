# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class HuntConfigSettings(models.TransientModel):
    _name = 'hunt.config.settings'
    _description = "Res Config Settings"
    _inherit = 'res.config.settings'


    hunt_sequence_id = fields.Many2one('ir.sequence', string='Hunt Reference', related='company_id.hunt_sequence_id', readonly=False, domain=[('code', '=', 'eggs.hunt.sequence')])
