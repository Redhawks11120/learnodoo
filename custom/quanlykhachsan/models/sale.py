# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError
from datetime import date

class Sale(models.Model):
    _name = 'hotel.sale'
    _description = 'Hotel Sale'

    name = fields.Char(string= 'Tên sale')
    type = fields.Selection(
        [('percent', 'Phần trăm'), ('vnd', 'Việt Nam Đồng')], string= 'Kiểu', default='percent'
    )
    amount = fields.Float(string='Giá trị')