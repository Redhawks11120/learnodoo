# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions

class Teacher(models.Model):
    _name = 'uni.teacher'
    _description = 'uni teacher'

    name = fields.Char(string='Tên', required=True)
    address = fields.Char(string='Địa chỉ')
    phone = fields.Char(string='Số điện thoại')
    salary = fields.Float(string='Lương')
    gender = fields.Selection(
        [('male', 'Nam'), ('female', 'Nữ')]
    )
    code = fields.Char(string='CMND/CCCD')
    birthday = fields.Date(string='Ngày sinh')
    uni_id = fields.Char(string='Mã giảng viên')
