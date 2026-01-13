# Card Reader System - API Documentation

## Deskripsi Sistem

Sistem pembacaan kartu fisik dengan card reader untuk Odoo 18. Sistem ini memungkinkan:

- Manajemen data kartu fisik (Card UID)
- Pencatatan setiap pembacaan kartu dari card reader
- API untuk card reader devices
- Monitoring dan log aktivitas pembacaan

---

## Model Data

### 1. Model: card.card (Kartu Fisik)

Menyimpan data kartu fisik yang dapat dibaca oleh card reader.

**Fields:**

- `card_uid` (Char, Required, Unique): Nomor unik kartu (dari card reader)
- `card_name` (Char, Required): Nama/deskripsi kartu
- `card_type` (Selection): Tipe kartu
  - `access`: Akses
  - `employee`: Karyawan
  - `visitor`: Pengunjung
  - `other`: Lainnya
- `holder_name` (Char): Nama pemegang kartu
- `holder_email` (Char): Email pemegang
- `is_active` (Boolean): Status aktivasi kartu
- `created_date` (Datetime): Tanggal pembuatan
- `notes` (Text): Catatan tambahan
- `reading_ids` (One2many): Relasi ke log pembacaan
- `reading_count` (Integer, Computed): Jumlah kali dibaca

---

### 2. Model: card.card_reading (Log Pembacaan Kartu)

Mencatat setiap kali kartu dibaca oleh card reader.

**Fields:**

- `card_id` (Many2one): Referensi ke kartu yang dibaca
- `card_uid` (Char, Related, Stored): UID dari kartu
- `holder_name` (Char, Related, Stored): Nama pemegang
- `reading_time` (Datetime, Required): Waktu pembacaan
- `reader_device` (Char): Nama/ID perangkat pembaca (default: 'DEFAULT_READER')
- `location` (Char): Lokasi pembacaan
- `status` (Selection): Status pembacaan
  - `success`: Berhasil
  - `failed`: Gagal
  - `invalid`: Tidak valid (kartu tidak terdaftar)
- `notes` (Text): Catatan

---

## API Endpoints

### 1. POST /card/read

Endpoint untuk membaca kartu dari card reader.

**Request Body (JSON):**

```json
{
    "card_uid": "UID_001234567890",
    "reader_device": "READER_MAIN_GATE",
    "location": "Pintu Utama"
}
```

**Parameters:**

- `card_uid` (Required): UID kartu yang dibaca
- `reader_device` (Optional): Nama perangkat pembaca (default: 'DEFAULT_READER')
- `location` (Optional): Lokasi pembacaan

**Response Success:**

```json
{
    "status": "success",
    "message": "Kartu berhasil dibaca: Ahmad Wijaya",
    "reading_id": 123,
    "card_name": "Kartu Akses Utama",
    "holder_name": "Ahmad Wijaya",
    "card_type": "employee",
    "reading_time": "2026-01-09T08:30:00"
}
```

**Response Invalid Card:**

```json
{
    "status": "invalid",
    "message": "Kartu tidak terdaftar",
    "card_uid": "UID_UNKNOWN"
}
```

**Response Error:**

```json
{
    "status": "error",
    "message": "Card UID tidak diberikan"
}
```

---

### 2. GET /card/status

Endpoint untuk mengecek status sistem card reader.

**Response:**

```json
{
    "status": "online",
    "active_cards": 3,
    "total_readings": 25,
    "timestamp": "2026-01-09T10:30:45"
}
```

---

### 3. GET /card/list-cards

Endpoint untuk mendapatkan daftar semua kartu aktif.

**Response:**

```json
{
    "status": "success",
    "count": 3,
    "cards": [
        {
            "card_uid": "UID_001234567890",
            "card_name": "Kartu Akses Utama",
            "holder_name": "Ahmad Wijaya",
            "card_type": "employee"
        },
        {
            "card_uid": "UID_098765432101",
            "card_name": "Kartu Pengunjung",
            "holder_name": "Budi Santoso",
            "card_type": "visitor"
        },
        {
            "card_uid": "UID_556677889900",
            "card_name": "Kartu Akses Gudang",
            "holder_name": "Siti Nurhaliza",
            "card_type": "access"
        }
    ]
}
```

---

## Cara Menggunakan

### 1. Membuat Kartu Baru

- Buka menu "Card Reader System" > "Kartu"
- Klik "Create"
- Isi field:
  - **Card UID**: Nomor unik dari kartu (dari card reader, misal: UID_001234567890)
  - **Card Name**: Nama kartu (misal: "Kartu Akses Utama")
  - **Card Type**: Pilih tipe
  - **Holder Name**: Nama pemegang
  - **Holder Email**: Email pemegang
  - **Is Active**: Centang untuk mengaktifkan
  - **Notes**: Catatan tambahan
- Klik "Save"

### 2. Membaca Kartu (Menggunakan Card Reader)

Card reader akan mengirim HTTP POST request ke:

```http
http://YOUR_ODOO_URL/card/read
```

Dengan format JSON:

```json
{
    "card_uid": "UID_KARTU",
    "reader_device": "NAMA_DEVICE",
    "location": "LOKASI"
}
```

Sistem akan otomatis menciptakan record pembacaan dan mengembalikan response.

### 3. Melihat Log Pembacaan

- Buka menu "Card Reader System" > "Log Pembacaan"
- Anda dapat melihat semua history pembacaan kartu
- Filter berdasarkan:
  - Status (Berhasil, Tidak Valid, Gagal)
  - Perangkat pembaca
  - Tanggal pembacaan

### 4. Analisis dan Monitoring

- Gunakan **Graph View** untuk visualisasi statistik pembacaan
- Gunakan **Pivot View** untuk analisis berdasarkan device dan status

---

## Method Penting

### Method: CardReading.create_from_reader()

Method untuk membuat record pembacaan dari card reader.

**Syntax:**

```python
reading = env['card.card_reading'].create_from_reader(
    card_uid='UID_KARTU',
    reader_device='READER_NAME',
    location='LOKASI',
    status='success'
)
```

**Parameters:**

- `card_uid`: UID kartu yang dibaca (Required)
- `reader_device`: Nama device (default: 'DEFAULT_READER')
- `location`: Lokasi pembacaan
- `status`: Status (default: 'success')

**Returns:**

- Record CardReading yang dibuat
- Jika kartu tidak ditemukan, akan dibuat dengan status 'invalid'

---

## Integrasi dengan Card Reader Device

### Contoh: Arduino + NFC Reader

```python
import requests
import json

# Data dari NFC Reader
card_uid = "UID_001234567890"
reader_device = "ARDUINO_GATE_1"
location = "Pintu Utama"

# Kirim ke Odoo
url = "http://192.168.1.100:8069/card/read"
data = {
    "card_uid": card_uid,
    "reader_device": reader_device,
    "location": location
}

response = requests.post(url, json=data)
result = response.json()

if result['status'] == 'success':
    print(f"Akses diberikan ke: {result['holder_name']}")
else:
    print(f"Akses ditolak: {result['message']}")
```

---

## Security & Access Control

### Permissions

- **User**: Dapat membaca data kartu dan log pembacaan
- **System Administrator**: Dapat membaca, edit, create, dan delete

### Public Access

- Endpoint `/card/read` accessible dengan `auth='public'` (untuk card reader)
- Endpoint `/card/status` dan `/card/list-cards` juga public

---

## Troubleshooting

### Problem: "Kartu tidak terdaftar"

**Solution:**

1. Pastikan card UID sudah didaftarkan di sistem
2. Pastikan kartu memiliki status "Aktif"
3. Check field `card_uid` - harus exact match dengan input dari card reader

### Problem: Error "Card UID tidak diberikan"

**Solution:**

1. Pastikan card reader mengirim parameter `card_uid`
2. Check format request JSON

### Problem: Multiple Card Readers tidak terrekam dengan benar

**Solution:**

1. Set unique `reader_device` untuk setiap perangkat
2. Gunakan naming convention yang konsisten (misal: READER_GATE_1, READER_GATE_2, dll)

---

## Demo Data

Sistem sudah dilengkapi dengan data demo:

- 3 kartu contoh dengan UID berbeda
- 3 log pembacaan untuk testing

Aktifkan demo saat install module untuk melihat contohnya.
