from PIL import ImageGrab
import time
import cv2
import pytesseract
import re
import pyautogui
import random

x1 = random.randint(105, 115)
y1 = random.randint(240, 260)
t1 = random.uniform(0.5, 0.11)
x2 = random.randint(320, 336)
y2 = random.randint(449, 481)
t2 = random.uniform(0.05, 0.11)

res = 0
i = 0

time.sleep(2)

pyautogui.moveTo(x1, y1, t1)
pyautogui.click(button='right')
pyautogui.moveTo(x2, y2, t2)
pyautogui.keyDown('shiftleft')


while res <= 65:
    res = 0
    i += 1
    pyautogui.moveTo(x2, y2, t2)
    pyautogui.click(button='left')
    # pyautogui.keyUp('shiftleft')
    # x1 = random.randint(105, 115)
    # y1 = random.randint(240, 260)
    # t1 = random.uniform(0.1, 0.17)
    # x2 = random.randint(320, 336)
    # y2 = random.randint(449, 481)
    # t2 = random.uniform(0.1, 0.17)
    pyautogui.size()
    # pyautogui.moveTo(x1, y1, t1)
    # pyautogui.click(button='right')
    # pyautogui.moveTo(x2, y2, t2)
    # pyautogui.click(button='left')

# Захват изображения
    harb_screen = ImageGrab.grab(bbox=(0, 150, 1000, 270))
    harb_screen.save('C:/Users/Forza/PycharmProjects/pythonProject6/BotPY/harb_screen.png')
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# Подключение фото
    img = cv2.imread('harb_screen.png')
    img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Получаем текст
    config = r'--oem 3 --psm 6'
    sch = (pytesseract.image_to_string(img, config=config))

    if re.search(r'\bHARBINGERS\b', sch):
        print(sch)
        res = 67

    #     nums = re.search(r"(?<=HAVE ).*?(?=% INCREASED)", sch).group(0)
    #     nums = int(nums)
    #     print(f'Army  {nums}')
    #     if nums > 65:
    #         print("It's OK.")
    #         res = nums
    #
    # elif re.search(r'\bTIMELESS\b', sch):
    #     print("Emblems")
    #     print(sch)
    #     nums = re.search(r"(?<=AREAS HAVE ).*?(?=% CHANCE)", sch).group(0)
    #     nums = float(nums)
    #     print(f'Emblem  {nums}')
    #     if nums > 0.07 and nums < 0.11:
    #         print('Emblems drop!')
    #         res = 67
pyautogui.keyUp('shiftleft')
