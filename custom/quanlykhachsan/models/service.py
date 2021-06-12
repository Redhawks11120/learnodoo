# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions

class Service(models.Model):
    _name = 'hotel.service'
    _description = 'Hotel Service'

    name = fields.Char(string="Tên dịch vụ")
    price = fields.Float(string="Giá dịch vụ")
    description = fields.Text(string='Mô tả')