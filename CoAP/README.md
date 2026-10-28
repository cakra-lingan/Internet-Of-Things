# CoAP Sensor DHT22 dengan ESP32

Project ini menjalankan server CoAP pada ESP32 untuk membaca suhu dan kelembapan dari sensor DHT22. Client Python mengirim permintaan GET dan menampilkan jawaban di terminal.

## Perangkat dan software

- ESP32 yang dapat terhubung ke jaringan Wi-Fi.
- Sensor DHT22.
- Arduino IDE atau PlatformIO dengan dukungan board ESP32.
- Library Arduino:
  - CoAP Simple (`coap-simple.h`)
  - DHT sensor library (`DHT.h`)
  - Jika diminta oleh library DHT, pasang juga Adafruit Unified Sensor.
- Python 3.
- Package Python `aiocoap`.

## Rangkaian sensor

Hubungkan DHT22 ke ESP32:

| DHT22 | ESP32 |
|---|---|
| VCC | 3V3 |
| GND | GND |
| DATA | GPIO 4 |

Kode menggunakan GPIO 4 dan tipe sensor DHT22. Jika menggunakan sensor tanpa modul, ikuti datasheet sensor untuk kebutuhan resistor pull-up pada jalur DATA.

## Konfigurasi Wi-Fi ESP32

Di `main.cpp`, isi `ssid` dan `password` dengan kredensial Wi-Fi yang digunakan ESP32. ESP32 dan komputer yang menjalankan client harus dapat berkomunikasi melalui jaringan yang sama.

Unggah `main.cpp` ke board ESP32. Buka Serial Monitor pada baud rate **115200**. Setelah berhasil, Serial Monitor akan menampilkan status Wi-Fi, alamat IP ESP32, dan port server CoAP (`5683`).

Catat alamat IP yang ditampilkan karena alamat IP dapat berubah setelah ESP32 tersambung ulang ke Wi-Fi.

## Menjalankan client Python

Buka terminal di folder project, lalu pasang dependency:

```powershell
py -m pip install aiocoap
```

Minta suhu:

```powershell
py coap_get.py coap://ALAMAT-IP-ESP32/temp
```

Minta kelembapan:

```powershell
py coap_get.py coap://ALAMAT-IP-ESP32/humidity
```

Ganti `ALAMAT-IP-ESP32` dengan IP yang terlihat di Serial Monitor. Contohnya, jika IP ESP32 adalah `192.168.18.124`:

```powershell
py coap_get.py coap://192.168.18.124/temp
py coap_get.py coap://192.168.18.124/humidity
```

Client menunggu respons maksimal 10 detik. Jika tidak ada respons, client menampilkan pesan timeout.

## Alur kerja

1. Client Python mengirim permintaan CoAP GET ke alamat ESP32 dan endpoint yang diminta.
2. ESP32 menerima permintaan melalui UDP port `5683` dan memilih callback berdasarkan path `temp` atau `humidity`.
3. Callback membaca nilai dari DHT22 menggunakan `dht.readTemperature()` atau `dht.readHumidity()`.
4. ESP32 mengirim nilai sensor sebagai teks. Jika pembacaan gagal, ESP32 mengirim pesan kegagalan.
5. Respons menyertakan kembali token CoAP dari permintaan agar client dapat mencocokkan respons dengan permintaannya.
6. Python menampilkan kode respons CoAP dan isi respons.

Token CoAP adalah penanda internal untuk menghubungkan request dan response. ESP32 tetap mengembalikan token tersebut, tetapi nilainya tidak ditampilkan karena bukan nilai sensor maupun kata sandi. Nilai sensor yang ditampilkan berasal dari pembacaan DHT22, bukan angka simulasi.

## Log dan troubleshooting

- **Tidak bisa terhubung / timeout**: pastikan IP pada URL sama dengan IP terbaru di Serial Monitor, ESP32 dan komputer berada di jaringan yang dapat saling berkomunikasi, dan UDP port `5683` tidak diblokir firewall atau fitur client isolation pada access point.
- **Request terlihat di Serial Monitor tetapi Python timeout**: pastikan firmware terbaru sudah diunggah. Serial Monitor mencatat endpoint yang menerima request serta percobaan pengiriman respons dan panjang token CoAP.
- **`Gagal membaca suhu` atau `Gagal membaca kelembapan`**: periksa sambungan VCC, GND, DATA ke GPIO 4, tipe sensor, dan kondisi sensor.
- **Endpoint tidak ditemukan**: gunakan path persis `/temp` atau `/humidity`.
