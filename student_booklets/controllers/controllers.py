# -*- coding: utf-8 -*-
# from odoo import http


# class ./apps/studentBooklets(http.Controller):
#     @http.route('/./apps/student_booklets/./apps/student_booklets', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/./apps/student_booklets/./apps/student_booklets/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('./apps/student_booklets.listing', {
#             'root': '/./apps/student_booklets/./apps/student_booklets',
#             'objects': http.request.env['./apps/student_booklets../apps/student_booklets'].search([]),
#         })

#     @http.route('/./apps/student_booklets/./apps/student_booklets/objects/<model("./apps/student_booklets../apps/student_booklets"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('./apps/student_booklets.object', {
#             'object': obj
#         })
