# -*- coding: utf-8 -*-
# from odoo import http


# class EggsHuntExtended(http.Controller):
#     @http.route('/eggs_hunt_extended/eggs_hunt_extended/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/eggs_hunt_extended/eggs_hunt_extended/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('eggs_hunt_extended.listing', {
#             'root': '/eggs_hunt_extended/eggs_hunt_extended',
#             'objects': http.request.env['eggs_hunt_extended.eggs_hunt_extended'].search([]),
#         })

#     @http.route('/eggs_hunt_extended/eggs_hunt_extended/objects/<model("eggs_hunt_extended.eggs_hunt_extended"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('eggs_hunt_extended.object', {
#             'object': obj
#         })
