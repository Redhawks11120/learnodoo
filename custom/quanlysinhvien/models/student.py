# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions

class Student(models.Model):
    _name = 'uni.student'
    _description = 'uni student'

    name = fields.Char(string='Tên', required=True)
    address = fields.Char(string='Địa chỉ')
    phone = fields.Char(string='Số điện thoại')
    uni_id = fields.Char(string='Mã sinh viên')
    gender = fields.Selection(
        [('male', 'Nam'), ('female', 'Nữ')]
    )
    code = fields.Char(string='CMND/CCCD')
    birthday = fields.Date(string='Ngày sinh')