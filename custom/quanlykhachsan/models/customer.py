# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions


class Customer(models.Model):
    _name = 'hotel.customer'
    _description = 'Hotel Customer'
    _rec_name = 'customer_name'

    customer_name = fields.Char(string='Tên khách hàng', required=True)
    customer_id = fields.Integer(string="Số CMND/CCCD", required=True)
    customer_birthday = fields.Date(string="Ngày sinh")
    customer_address = fields.Text(string="Địa chỉ")
    phone_number = fields.Char(string="Số điện thoại", required=True)
    visa_card = fields.Integer(string="Visa")
    customer_email = fields.Char(string="Email")
    portrait = fields.Binary(string="Ảnh")
