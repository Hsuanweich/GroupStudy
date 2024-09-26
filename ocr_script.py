from PIL import Image
import pytesseract

def replace_l_with_1(input_string):
    # 使用 replace() 方法將 'l' 替換為 '1'
    return input_string.replace('l', '1')

def charOCR(locate):
    # 指定 Tesseract 安裝路徑 (你電腦tesseract.exe的位置)
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    # 開啟圖像路徑
    image = Image.open(locate)

    # 獲取圖片的寬度和高度
    width, height = image.size
    # 計算裁剪邊緣的像素
    crop_width = int(width * 0.08)
    crop_height = int(height * 0.15)
    # 定義裁剪區域 (左, 上, 右, 下)
    left = crop_width
    top = crop_height
    right = width - crop_width
    bottom = height - crop_height
    # 裁剪圖片
    cropped_image = image.crop((left, top, right, bottom))

    # 設定比例
    scale = 75/cropped_image.width  
    # 計算新尺寸
    new_size = (int(cropped_image.width * scale), int(cropped_image.height * scale))
    # 等比例放大縮小圖片
    resized_img = cropped_image.resize(new_size, Image.LANCZOS)

    resized_img.show()

    # 使用 Tesseract 進行 OCR 辨識
    text = pytesseract.image_to_string(resized_img)

    # 'l' 替換為 '1'
    textreplace1 = replace_l_with_1(text)

    # 回傳辨識字串
    return textreplace1

# 測試圖像路徑
locate = "C:\\photo_ptcg\\twhk_SVK.png"
text=charOCR(locate)
print(text)