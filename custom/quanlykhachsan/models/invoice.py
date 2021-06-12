# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions


class Invoice(models.Model):
    _name = 'hotel.invoice'
    _description = 'Hotel Invoice'
    _rec_name = 'code_invoice'

    code_invoice = fields.Char(string='Mã hóa đơn', required=True)
    code_booking = fields.Many2one('hotel.booking', string='Mã đặt phòng', required=True)
    customer_name = fields.Char(string='Tên khách hàng')
    customer_id = fields.Char(string='Tên khách hàng')
    customer_phone = fields.Char(string='Số điện thoại')
    time_start = fields.Date(string="Ngày bắt đầu thuê", readonly=True)
    time_end = fields.Date(string="Ngày trả phòng", readonly=True)
    list_room_booking = fields.One2many(string='Danh sách phòng', related='code_booking.room_ids', readonly=True)
    list_service_booking = fields.One2many(string='Danh sách dịch vụ', related='code_booking.service_ids', readonly=True)
    status = fields.Selection([
        ('unpaid', 'Chưa thanh toán'),
        ('paid', 'Đã thanh toán')],
        string='Trạng thái', track_visibility='always', default='unpaid'
    )
    price_all_room  = fields.Float(string="Tổng giá phòng")
    price_all_service = fields.Float(string="Tổng giá dịch vụ")
    price_all = fields.Float(string="Tổng giá")

    @api.multi
    def print_report(self):
        return self.env.ref('quanlykhachsan.report_invoice_card').report_action(self)

    @api.model
    def action_send_card(self):
        template_id = self.env.ref('quanlykhachsan.email_template_hotel_invoice').id
        self.env['mail.template'].browse(template_id).send_mail(self.id, force_send=True)
