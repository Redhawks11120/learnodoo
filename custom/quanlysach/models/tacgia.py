# -*- coding: utf-8 -*-
from odoo import models, fields


class TacGia(models.Model):
    _name = "quanlysach.tacgia"
    _register = True

    name = fields.Char("Tên tác giả")
    dateofb= fields.Date("Ngày sinh")

    sach = fields.One2many(
        comodel_name="quanlysach.sachcuatui",
        inverse_name="tacgia_chinh", string="Sách của tác giả")