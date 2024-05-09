# -*- coding: utf-8 -*-

#roomtypes.py


from odoo import models, fields, api

class RoomTypes(models.Model):
    _name = 'hotel.roomtypes'
    _description = 'Hotel Room Types'
    _order="name"

    imageroom = fields.Image("Room");
    imagebathroom = fields.Image("Bath Room");

    name = fields.Char("Room Type");
    description = fields.Char("Room Type Description");

    room_ids = fields.One2many('hotel.rooms','roomtype_id', string='Rooms List')

    dailycharges_ids=fields.One2many('hotel.dailycharges','roomtype_id', string='Daily Charges')
    class dailycharges(models.Model):
        _name = 'hotel.dailycharges'
        _description = 'hotel roomtype daily charges list'
        charge_id = fields.Many2one('hotel.charges',string="Charges")
        amount = fields.Float("Daily Amount", digits=(10,2), options={'always_reload': True})
        roomtype_id = fields.Many2one('hotel.roomtypes', string="Roomtype")