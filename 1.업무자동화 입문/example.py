import pyautogui
import xlwings as xw
import time
import random

# -- 엑셀파일 만들기 -- #
wb = xw.Book("example.xlsx")
ws = wb.sheets.active

names = ["Noh jeongho", "Park", "John", "Nick"]
departments = ["MKT", "HR", "Eng"]

for i in range(1, 101):
    ws.range(f"A{i}").value = i
    ws.range(f"B{i}").value = random.choice(departments)
    ws.range(f"C{i}").value = random.choice(names)
wb.save()

# -- 엑셀 -> ppt 데이터 옮기기 -- #
wb = xw.Book("example.xlsx")
ws = wb.sheets.active

# ppt 클릭하여 활성화
pyautogui.click(x=2808, y=234)

for i in range(1, 6):
    num = str(int(ws.range(f"A{i}").value))
    part = ws.range(f"B{i}").value
    name = ws.range(f"C{i}").value

    # 번호
    pyautogui.click(x=2785, y=478)
    # pyautogui.hotkey("ctrl", "a")
    time.sleep(0.3)
    pyautogui.write(num)

    # 소속
    pyautogui.click(x=2465, y=773)
    # pyautogui.hotkey("ctrl", "a")
    time.sleep(0.3)
    pyautogui.write(part)

    # 이름
    pyautogui.click(x=3059, y=770)
    # pyautogui.hotkey("ctrl", "a")
    time.sleep(0.3)
    pyautogui.write(name)

    time.sleep(0.3)
    # 다음 페이지로 옮겨가기
    pyautogui.click(x=2808, y=234)
    pyautogui.press("down")
