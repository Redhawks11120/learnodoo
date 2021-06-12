# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions


class Sach(models.Model):
    _name = "quanlysach.sachcuatui"
    _rec_name = "ten_sach"
    _description = u'Sách của tui'
    _order = 'tacgia_chinh,ten_sach'

    ten_sach = fields.Char("Tên sách", size=200, translate=True, default="Sách mới")
    mota = fields.Text("Mô tả", help="Viết mô tả ở đây")
    ngay = fields.Date("Ngày xuất bản", required=True)
    tacgia_chinh = fields.Many2one(comodel_name="quanlysach.tacgia", string="Tác giả chính")
    trangthai = fields.Selection(string="Trạng thái",
                                 selection=[('con', 'Còn sách'), ('het', 'Hết sách'), ('shet', 'Sắp hết sách')])
    soluong = fields.Integer("Số lượng")
    giagoc = fields.Float("Giá gốc")
    giab = fields.Float("Giá bán", compute="_tinh_giab", store=True)
    _sql_constraints = [('ten_sach_la_duy_nhat', 'UNIQUE(ten_sach)', u'Tên trung rồi chọn cái khác đi')]

    @api.multi
    @api.constrains("ten_sach")
    def _kiem_tra_ten_sach(self):
        for rec in self:
            if len(rec.ten_sach) < 6:
                raise exceptions.ValidationError("Tên sách quá ngắn")

    @api.onchange("tacgia_chinh")
    def _them_tg_ten_sach(self):
        try:
            pos = self.ten_sach.rfind("-")
            if pos == -1:
                self.ten_sach += " - " + self.tacgia_chinh.name
            else:
                self.ten_sach = self.ten_sach[0:pos + 2] \
                                + self.tacgia_chinh.name
        except:
            pass

    @api.model
    def doi_trang_thai(self, sl):
        if 0 < sl < 10:
            self.trangthai = 'shet'
        elif sl == 0:
            self.trangthai = 'het'
        else:
            self.trangthai = 'con'

    @api.onchange("soluong")
    def thaydoi_soluong(self):
        self.doi_trang_thai(self.soluong)

    @api.depends("soluong", "giagoc")
    def _tinh_giab(self):
        for sach in self:
            if sach.soluong > 100:
                sach.giab = sach.giagoc * 1.2
            elif 50 < sach.soluong <= 100:
                sach.giab = sach.giagoc * 1.5
            else:
                sach.giab = sach.giagoc * 2.0
