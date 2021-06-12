# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions

class List_Room(models.Model):
    _name = 'hotel.list_room'
    _description = 'Hotel List Room'
    _rec_name = 'list_room'

    room_name = fields.Many2one('hotel.room',string="Phòng", required=True)
    room_type = fields.Selection(
        [('basic', 'Normal'), ('vip', 'Vip'), ('lux', 'Luxury')],
        string='Loại phòng', default='basic', required=True, related='room_name.type'
    )
    room_view = fields.Selection(
        [('sea_view', 'View Biển'), ('mountain_view', 'View Núi'), ('city_view', 'View Thành phố'),
         ('other_view', 'Khác')],
        string="View phòng", required=True, related='room_name.view_room'
    )
    room_price = fields.Float(string='Giá phòng', related= 'room_name.price')
    room_code = fields.Char(string='Mã phòng', required=True, related= 'room_name.code')
    day_begin_use = fields.Date(string="Ngày bắt đầu sử dụng phòng")
    day_end_use = fields.Date(string="Ngày kết thúc sử dụng phòng")
    room_status = fields.Selection([('wait', 'Đang chờ'),('open', 'Đang sử dụng'), ('close', 'Đã trả phòng')], string='Trạng thái', required=True)
    customer_name = fields.Many2one('hotel.customer', string="Tên khách hàng")
    customer_id = fields.Integer(string="Số CMT/CCCD", related='customer_name.customer_id')
    list_room = fields.Many2one('hotel.booking', string="Khách hàng sử dụng phòng")