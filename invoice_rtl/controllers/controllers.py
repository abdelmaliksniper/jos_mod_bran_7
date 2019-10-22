# -*- coding: utf-8 -*-
from odoo import http

# class InvoiceRtl(http.Controller):
#     @http.route('/invoice_rtl/invoice_rtl/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/invoice_rtl/invoice_rtl/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('invoice_rtl.listing', {
#             'root': '/invoice_rtl/invoice_rtl',
#             'objects': http.request.env['invoice_rtl.invoice_rtl'].search([]),
#         })

#     @http.route('/invoice_rtl/invoice_rtl/objects/<model("invoice_rtl.invoice_rtl"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('invoice_rtl.object', {
#             'object': obj
#         })