# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
import json
from datetime import datetime


class CardReaderController(http.Controller):
    """
    Controller untuk menerima data dari card reader
    Endpoint: /carddd/read
    """
    
    @http.route('/carddd/read', type='json', auth='public', methods=['POST', 'GET'])
    def card_read(self, **kwargs):
        """
        Endpoint untuk membaca kartu
        
        Parameters (JSON):
        {
            'card_uid': 'UID_KARTU',
            'reader_device': 'NAMA_DEVICE',
            'location': 'LOKASI'
        }
        
        Returns:
        {
            'status': 'success/failed',
            'message': 'pesan',
            'data': {...}
        }
        """
        try:
            # Ambil data dari request
            data = request.jsonrequest if request.content_type == 'application/json' else kwargs
            
            card_uid = data.get('card_uid', '')
            reader_device = data.get('reader_device', 'DEFAULT_READER')
            location = data.get('location', '')
            
            if not card_uid:
                return {
                    'status': 'error',
                    'message': 'Card UID tidak diberikan'
                }
            
            # Buat record pembacaan
            reading = request.env['carddd.card_reading'].create_from_reader(
                card_uid=card_uid,
                reader_device=reader_device,
                location=location
            )
            
            if reading.status == 'invalid':
                return {
                    'status': 'invalid',
                    'message': 'Kartu tidak terdaftar',
                    'card_uid': card_uid
                }
            
            return {
                'status': 'success',
                'message': f'Kartu berhasil dibaca: {reading.holder_name}',
                'reading_id': reading.id,
                'card_name': reading.card_id.card_name,
                'holder_name': reading.holder_name,
                'card_type': reading.card_id.card_type,
                'reading_time': reading.reading_time.isoformat() if reading.reading_time else ''
            }
        
        except Exception as e:
            return {
                'status': 'error',
                'message': f'Terjadi kesalahan: {str(e)}'
            }
    
    @http.route('/carddd/status', type='json', auth='public')
    def card_status(self, **kwargs):
        """
        Endpoint untuk mengecek status sistem
        """
        try:
            card_count = request.env['carddd.card'].search_count([('is_active', '=', True)])
            reading_count = request.env['carddd.card_reading'].search_count([])
            
            return {
                'status': 'online',
                'active_cards': card_count,
                'total_readings': reading_count,
                'timestamp': datetime.now().isoformat()
            }
        except Exception as e:
            return {
                'status': 'error',
                'message': str(e)
            }
    
    @http.route('/carddd/list-cards', type='json', auth='public')
    def list_cards(self, **kwargs):
        """
        Endpoint untuk mendapatkan daftar kartu aktif
        """
        try:
            cards = request.env['carddd.card'].search([('is_active', '=', True)])
            
            card_list = []
            for card in cards:
                card_list.append({
                    'card_uid': card.card_uid,
                    'card_name': card.card_name,
                    'holder_name': card.holder_name,
                    'card_type': card.card_type,
                })
            
            return {
                'status': 'success',
                'count': len(card_list),
                'cards': card_list
            }
        except Exception as e:
            return {
                'status': 'error',
                'message': str(e)
            }
