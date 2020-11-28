# -*- coding: utf-8 -*-
# from odoo import http


# class EggHunt(http.Controller):
#     @http.route('/egg_hunt/egg_hunt/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/egg_hunt/egg_hunt/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('egg_hunt.listing', {
#             'root': '/egg_hunt/egg_hunt',
#             'objects': http.request.env['egg_hunt.egg_hunt'].search([]),
#         })

#     @http.route('/egg_hunt/egg_hunt/objects/<model("egg_hunt.egg_hunt"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('egg_hunt.object', {
#             'object': obj
#         })
