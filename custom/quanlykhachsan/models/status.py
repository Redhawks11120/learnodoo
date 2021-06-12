# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions


class Status(models.Model):
    _name = "hotel.status"
    _description = "Hotel Status"

    name_room = fields.Char(string='Tên Phòng', required= True)
    status_room = fields.Selection(
        [('open', 'Open'), ('close', 'Close'), ('maintain', 'Maintain'), ('stop', 'Stop')],
        default='open', string='Trạng thái'
    )
    customer_name = fields.Char(string="Tên khách hàng")
    day_begin = fields.Date(string="Ngày bắt đầu thuê")
    day_end = fields.Date(string="Ngày trả phòng")
