# Identifier

## 🆔 Identifier - Optical Character Recognition (OCR) for Document Type Identification

**Identifier** is a Python-based OCR system that processes images and extracts text using Tesseract OCR. It identifies document types (e.g., ID cards, passports, certificates) by analyzing extracted text.

## 📌 Features
- Extracts text from images using Tesseract OCR
- Preprocesses images for better OCR accuracy
- Identifies document types like ID cards, passports, certificates, etc.
- Supports English and Turkish languages
- Configurable keyword matching for document identification
- Outputs results in structured JSON format

## 🚀 Installation
### 1️⃣ Install Dependencies
Ensure you have Python installed (Python 3.x recommended). Then install dependencies using:

```bash
pip install -r requirements.txt
```

### 2️⃣ Install Tesseract OCR
Download and install Tesseract OCR from [here](https://github.com/UB-Mannheim/tesseract/wiki). After installation, set its path in the script:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
```

### 3️⃣ Run the Script
Place an image in the specified directory and update the script accordingly:

```python
image_path = r"path_to_your_image.png"
```
Then, execute the script:

```bash
python identifier.py
```

## 🔧 Configuration
You can modify the document classification keywords by updating the `target_texts` dictionary in the script:

```python
target_texts = {
    "identity card": "kimlik",
    "national id": "kimlik",
    "passport": "pasaport",
    "document": "belge",
    "certificate": "sertifika",
    "driving license": "ehliyet",
    "student id": "öğrenci kartı"
}
```

To add or modify document types, simply update this dictionary.

## 📤 Output
The script returns a structured JSON output containing:

```json
{
    "content": "Extracted text from image",
    "success": true,
    "type": "passport"
}
```

## 📜 License
This project is open-source...

## ⭐ Contributions & Support
If you find this useful, give it a ⭐ on GitHub! Feel free to submit PRs or open issues for improvements.

---
**Happy Coding! 🚀**

