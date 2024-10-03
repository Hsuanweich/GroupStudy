from PIL import Image
import pytesseract
import os

def replace_l_with_1(input_string):
    # 使用 replace() 方法將 'l' 替換為 '1'
    return input_string.replace('l', '1')

def convert_nonwhite_to_black(image):
    # 獲取圖片的像素數據
    pixels = image.load()

    # 逐像素處理圖片
    unit = 150
    for i in range(image.size[0]):  # 對每一列
        for j in range(image.size[1]):  # 對每一行
            # 根據圖像模式獲取顏色值
            r, g, b = pixels[i, j][:3]  # 只獲取前3個通道
            # 如果不是白色 (判斷 RGB 值接近 255)，則將其設為黑色
            if r < unit or g < unit or b < unit:  # 可以根據需求調整這裡的閾值
                pixels[i, j] = (0, 0, 0)  # 設為黑色
            else:
                pixels[i, j] = (255, 255, 255)  # 設為白色（確保白色保持不變）

def remove_trailing_pipe(input_string):
    return input_string.replace("|", "")

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

    # 將非白色部分轉為黑色
    #convert_nonwhite_to_black(cropped_image)

    # 設定比例
    scale = 50/cropped_image.width  
    # 計算新尺寸
    new_size = (int(cropped_image.width * scale * 2), int(cropped_image.height * scale))
    # 等比例放大縮小圖片
    resized_img = cropped_image.resize(new_size, Image.LANCZOS)

    # 計算新的圖像尺寸
    new_width = image.width + 100
    new_height = image.height + 100

    # 創建一個新的黑色背景圖片
    new_image = Image.new("RGB", (new_width, new_height), (0, 0, 0))

    # 將原圖像貼在新圖像的中心
    new_image.paste(resized_img, (30, 50))

    new_image.show()

    # 使用 Tesseract 進行 OCR 辨識
    text = pytesseract.image_to_string(new_image)

    # 'l' 替換為 '1'
    textreplace1 = replace_l_with_1(text)
    # '|' 替換為 ''
    textreplace2 = remove_trailing_pipe(textreplace1)

    # 回傳辨識字串
    return textreplace2

# 測試圖像路徑
folder_path = "C:\\Users\\張軒偉\\OneDrive\\桌面\\專題\\ocr\\mark"
locate = "C:\\Users\\張軒偉\\OneDrive\\桌面\\專題\\ocr\\mark\\mark40.png"

text=charOCR(locate)
print(text)
