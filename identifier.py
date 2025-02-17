import pytesseract
from PIL import Image
import cv2, json
import numpy as np

# Tesseract'ı web sitesinden kur ve tam yolunu ayarla
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Yüklenen görüntüyü oku (OpenCV) - BACKEND için INPUT KISMI
image_path = r"c:\Users\Akif\Downloads\1.png"
image = cv2.imread(image_path)

# 1️⃣ Gri tona çevir (Siyah-beyaz yapmak için)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 2️⃣ Gürültü azaltma (Gaussian Blur)
gray = cv2.GaussianBlur(gray, (5,5), 0)

# 3️⃣ Kontrast artırma (Adaptive Thresholding)
processed_image = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2
)

# 4️⃣ Keskinleştirme (Kenarları belirginleştirme)
kernel = np.array([[0, -1, 0], [-1, 5,-1], [0, -1, 0]])  # Keskinleştirme filtresi
processed_image = cv2.filter2D(processed_image, -1, kernel)

# 5️⃣ OCR ile metni oku (Türkçe + İngilizce desteği)
extracted_text = pytesseract.image_to_string(processed_image, lang="tur+eng").lower().strip()

# 6️⃣ Aranacak kelimeler ve döndürülecek tipler
target_texts = {
    "identity card": "kimlik",
    "national id": "kimlik",
    "passport": "pasaport",
    "document": "belge",
    "certificate": "sertifika",
    "driving license": "ehliyet",
    "student id": "öğrenci kartı"
}

# 7️⃣ Metnin bulunup bulunmadığını kontrol et
found_type = None  # Başlangıçta eşleşme yok

for key, value in target_texts.items():
    if key in extracted_text:
        found_type = value
        break  # İlk eşleşmeyi bulunca durdur

# 8️⃣ JSON formatında sonuç döndür
result = {
    "content": extracted_text,  # OCR çıktısı
    "success": found_type is not None,  # Eşleşme bulundu mu?
    "type": found_type  # Eşleşen belge türü (kimlik, belge, pasaport vb.)
}

print(json.dumps(result, ensure_ascii=False, indent=4))
