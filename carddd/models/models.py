# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime


class Card(models.Model):
    _name = 'carddd.card'
    _description = 'Kartu Fisik'
    _rec_name = 'card_uid'

    card_uid = fields.Char(
        string='Card UID',
        required=True,
        unique=True,
        help='Nomor unik dari kartu fisik (dari card reader)'
    )
    card_name = fields.Char(
        string='Nama Kartu',
        required=True,
        help='Nama atau deskripsi kartu'
    )
    card_type = fields.Selection([
        ('access', 'Akses'),
        ('employee', 'Karyawan'),
        ('visitor', 'Pengunjung'),
        ('other', 'Lainnya')
    ], string='Tipe Kartu', default='access')
    
    holder_name = fields.Char(
        string='Nama Pemegang',
        help='Nama orang yang membawa kartu'
    )
    holder_email = fields.Char(
        string='Email Pemegang',
        help='Email pemegang kartu'
    )
    is_active = fields.Boolean(
        string='Aktif',
        default=True,
        help='Status aktivasi kartu'
    )
    
    created_date = fields.Datetime(
        string='Tanggal Dibuat',
        default=datetime.now(),
        readonly=True
    )
    notes = fields.Text(
        string='Catatan'
    )
    
    reading_ids = fields.One2many(
        'carddd.card_reading',
        'card_id',
        string='History Pembacaan'
    )
    reading_count = fields.Integer(
        string='Jumlah Pembacaan',
        compute='_compute_reading_count'
    )
    
    @api.depends('reading_ids')
    def _compute_reading_count(self):
        for record in self:
            record.reading_count = len(record.reading_ids)
    
    _sql_constraints = [
        ('unique_card_uid', 'unique(card_uid)', 'Card UID harus unik!')
    ]


class CardReading(models.Model):
    _name = 'carddd.card_reading'
    _description = 'Log Pembacaan Kartu'
    _rec_name = 'card_id'
    _order = 'reading_time desc'

    card_id = fields.Many2one(
        'carddd.card',
        string='Kartu',
        required=True,
        ondelete='cascade',
        help='Kartu yang dibaca'
    )
    card_uid = fields.Char(
        string='Card UID',
        related='card_id.card_uid',
        store=True,
        readonly=True
    )
    holder_name = fields.Char(
        string='Nama Pemegang',
        related='card_id.holder_name',
        store=True,
        readonly=True
    )
    reading_time = fields.Datetime(
        string='Waktu Pembacaan',
        required=True,
        default=datetime.now(),
        help='Waktu kartu dibaca'
    )
    reader_device = fields.Char(
        string='Perangkat Pembaca',
        help='Nama atau ID perangkat card reader',
        default='DEFAULT_READER'
    )
    location = fields.Char(
        string='Lokasi',
        help='Lokasi pembacaan kartu'
    )
    status = fields.Selection([
        ('success', 'Berhasil'),
        ('failed', 'Gagal'),
        ('invalid', 'Tidak Valid')
    ], string='Status', default='success')
    
    notes = fields.Text(
        string='Catatan'
    )
    
    @api.model
    def create_from_reader(self, card_uid, reader_device='DEFAULT_READER', location='', status='success'):
        """
        Method untuk membuat record pembacaan kartu dari card reader
        Parameters:
            card_uid: UID dari kartu yang dibaca
            reader_device: Nama perangkat pembaca
            location: Lokasi pembacaan
            status: Status pembacaan (success/failed/invalid)
        Returns:
            Record CardReading yang dibuat atau False jika kartu tidak ditemukan
        """
        card = self.env['carddd.card'].search([
            ('card_uid', '=', card_uid),
            ('is_active', '=', True)
        ], limit=1)
        
        if not card:
            # Jika kartu tidak ditemukan, buat record dengan status invalid
            return self.create({
                'card_uid': card_uid,
                'reading_time': datetime.now(),
                'reader_device': reader_device,
                'location': location,
                'status': 'invalid',
                'notes': 'Kartu tidak terdaftar dalam sistem'
            })
        
        # Buat record pembacaan
        reading = self.create({
            'card_id': card.id,
            'reading_time': datetime.now(),
            'reader_device': reader_device,
            'location': location,
            'status': status,
        })
        
        return reading

