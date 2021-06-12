# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError
from datetime import date

class Booking(models.Model):
    _name = 'hotel.booking'
    _description = 'Hotel Booking'
    _rec_name = 'booking_id'

    booking_id = fields.Char(string="Mã đặt phòng", required= True)
    booking_status = fields.Selection([('open', 'Đang sử dụng'), ('close', 'Đã trả phòng')], string='Trạng thái', required=True)
    room_name = fields.Many2one('hotel.room', string='Phòng')
    room_price = fields.Float(string="Giá cơ bản", related='room_name.price')
    room_view = fields.Selection(
        [('sea_view', 'View Biển'), ('mountain_view', 'View Núi'), ('city_view', 'View Thành phố'),
         ('other_view', 'Khác')],
        string="View phòng", required=True, related='room_name.view_room'
    )
    room_status = fields.Selection(
        [('open', 'Open'), ('close', 'Close'), ('maintain', 'Maintain'), ('stop', 'Stop')],
        default='open', string='Trạng thái', related='room_name.status'
    )
    customer_name = fields.Many2one('hotel.customer', string='Khách hàng')
    customer_phone = fields.Char(string="Số điện thoại", related='customer_name.phone_number')
    customer_id = fields.Integer(string="Số CMT/CCCD", related='customer_name.customer_id')
    customer_person = fields.Integer(string="Số lượng khách hàng")
    days_check_in = fields.Date(string="Ngày bắt đầu thuê")
    days_check_out = fields.Date(string="Ngày trả phòng")
    current_days = fields.Date.today()
    room_ids = fields.One2many(comodel_name='hotel.list_room',inverse_name='list_room', String='Danh sách phòng')
    service_ids = fields.One2many(comodel_name='hotel.list_service',inverse_name='service_ids', String='Danh sách dịch vụ')

    @api.multi
    @api.constrains('days_check_in','days_check_out')
    def date_contrain(self):
        for rec in self:
            if rec.days_check_out < rec.days_check_in:
                raise ValidationError('Ngày đến phải lớn ngày đi')

    @api.multi
    @api.constrains('days_check_in')
    def time_check_in(self):
        for rec in self:
            if rec.days_check_in < rec.current_days:
                raise ValidationError('Ngày đến phải lớn hơn hiện tại')

    @api.multi
    def actions_mark_as_paid(self):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        return {
            "type": "ir.actions.act_url",
            "url": base_url + "/web/customers",
            "target": "new",  # self
        }
