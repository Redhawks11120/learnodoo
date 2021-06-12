# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions


class Subject(models.Model):
    _name = 'uni.subject'
    _description = 'uni subject'

    name = fields.Char(string='Tên môn học')
    sub_id = fields.Char(string='Mã môn học')
    sub_credits = fields.Integer(string='Số tín chỉ')