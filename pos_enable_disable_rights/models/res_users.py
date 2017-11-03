# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _

class Users(models.Model):
    _inherit = 'res.users'

    pos_disc_al = fields.Boolean(string='Allow Discount')
    pos_pri_al = fields.Boolean(string='Allow Price Change')
    pos_refund_al = fields.Boolean(string='Allow Refund Products')
