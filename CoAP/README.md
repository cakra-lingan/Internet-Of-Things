CoAP adalah singkatan dari Constrained Application Protocol, yaitu protokol komunikasi berbasis web yang dirancang untuk perangkat IoT yang memiliki keterbatasan daya, memori, dan bandwidth. CoAP didefinisikan dalam RFC 7252 oleh IETF.

Protokol ini bekerja mirip HTTP (menggunakan metode GET, POST, PUT, DELETE dan format URI), tetapi jauh lebih ringan. CoAP biasanya berjalan di atas UDP, bukan TCP, dan menggunakan pesan yang kecil dan sederhana agar cocok untuk sensor dan perangkat kecil. CoAP juga mendukung fitur seperti observasi (subscribe terhadap perubahan data) dan multicast.

1. Persiapan
- Install ESP32 board di Arduino IDE lewat Tools → Board → Boards Manager (cari “esp32” oleh Espressif).
- Install library lewat Sketch → Include Library → Manage Libraries: coap-simple (oleh hirotakaster)
- DHT sensor library (oleh Adafruit), beserta Adafruit Unified Sensor jika diminta
- Pilih board, misalnya ESP32 Dev Module, dan port COM yang sesuai.

2. Sambungkan sensor
DHT22: pin VCC ke 3.3V, GND ke GND, dan pin DATA ke GPIO 4.

3. Upload dan cek
- Upload sketch, lalu buka Serial Monitor dengan baud rate 115200. Catat IP yang muncul, misalnya 192.168.1.50.

4. Tes dengan perintah terminal
   aiocoap-client coap://192.168.1.50/suhu
