# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions

class List_Service(models.Model):
    _name = 'hotel.list_service'
    _description = 'Hotel List Service'
    _rec_name = 'service_ids'

    customer_name = fields.Many2one('hotel.customer', string="Tên khách hàng")
    customer_room = fields.Many2one('hotel.room', string="Phòng khách hàng")
    service_name = fields.Many2one('hotel.service', string="Tên dịch vụ")
    description = fields.Text(string="Mô tả", related='service_name.description')
    count = fields.Integer(string="Số lượng")
    note = fields.Text(string="Note")
    price = fields.Float(string='Giá dịch vụ', required=True, related='service_name.price')
    service_ids = fields.Many2one('hotel.booking', string="Khách hàng sử dụng dịch vụ")