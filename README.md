# SmartMotionCam

## Türkçe
Python ile geliştirilmiş akıllı hareket algılama ve güvenlik kamerası sistemi.  
Hareket algılandığında video kaydı yapar, ekranda uyarı gösterir ve bip sesi çıkarır.  

### Özellikler
- Hareket algılandığında **ekran uyarısı + bip sesi**  
- **Hareket videoları otomatik olarak kaydedilir** (`motion_videos/` klasörü)  
- Her hareket **ayrı klasör ve dosya** olarak kaydedilir, tarih ve saat etiketi ile  
- Arduino veya ekstra donanım gerekmez, sadece PC ve webcam yeterli  

### Kurulum
```bash
git clone https://github.com/kullaniciadi/SmartMotionCam.git
cd SmartMotionCam
pip install -r requirements.txt
```

### Kullanım
```bash
python motion_cam.py
```
- Hareket algılandığında ekranda "HAREKET ALGILANDI!" gösterilir ve bip sesi çıkar.  
- Hareket bitince "HAREKET BITTI" yazısı görünür.  
- Videolar `motion_videos/` klasöründe kaydedilir.  
- Çıkmak için pencereyi açın ve **q** tuşuna basın.

---

## English
SmartMotionCam is a Python-based smart motion detection and security camera system.  
It records video when motion is detected, shows alerts on screen, and plays a beep sound.

### Features
- **Screen alert + beep sound** on motion detection  
- **Automatic video saving** in `motion_videos/` folder  
- Each motion is saved in **separate folder and file**, with timestamp  
- No Arduino or extra hardware required, only PC & webcam  

### Installation
```bash
git clone https://github.com/username/SmartMotionCam.git
cd SmartMotionCam
pip install -r requirements.txt
```

### Usage
```bash
python motion_cam.py
```
- "MOTION DETECTED!" appears on screen and beep plays.  
- "MOTION CLEARED" appears when movement ends.  
- Videos are stored in `motion_videos/` folder.  
- Press **q** to exit the application.
