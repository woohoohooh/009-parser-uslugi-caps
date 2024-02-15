import pyautogui
import time

number = []

with open('tmp_phones.txt', 'r', encoding='utf8') as f:
    for i in f:
        number.append(i.strip())

for hi in number:
    # клик по полю телефона
    pyautogui.moveTo(312, 336)
    pyautogui.click()
    # ввод телефона
    time.sleep(1)
    pyautogui.write(hi)
    # клик по кнопке
    time.sleep(1)
    pyautogui.moveTo(313, 429)
    pyautogui.click()
    time.sleep(4)
    # сохранение капчи
    pyautogui.moveTo(287, 391)
    time.sleep(1)
    pyautogui.rightClick()
    time.sleep(1)
    pyautogui.moveTo(322, 434)
    pyautogui.click()
    time.sleep(1)
    # save click
    pyautogui.moveTo(460, 611)
    pyautogui.click()
    time.sleep(2)
    pyautogui.hotkey('f5')
    time.sleep(5)

