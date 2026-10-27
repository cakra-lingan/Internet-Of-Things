ESP32 membaca DHT22, lalu menjalankan web server kecil yang mengembalikan suhu dalam format JSON. Setelah itu bisa dibuka dari browser atau aplikasi lain lewat HTTP.

Wiring:
DHT22 VCC → 3.3V
DHT22 GND → GND
DHT22 DATA → GPIO 4 (bisa diganti, sesuaikan di kode)
Pasang resistor pull-up 10kΩ antara DATA dan VCC jika modul kamu belum punya resistor

Install library di Arduino IDE: “DHT sensor library” dan “Adafruit Unified Sensor” (lewat Library Manager).

Cara pakai:
- Upload kode, lalu buka Serial Monitor (115200 baud) untuk melihat IP ESP32.
- Buka http://IP_ESP32/temp di browser. Hasilnya kira-kira seperti ini:
  {"suhu":28.5,"kelembapan":65.2}
Dari program lain, cukup lakukan HTTP GET ke alamat yang sama.

Catatan: DHT22 hanya bisa dibaca sekitar 2 detik sekali. Kalau request terlalu sering, hasilnya bisa NaN. Jika sering gagal, cek kabel DATA dan resistor pull-up.
