import xlwings as xw
import os
import pyautogui
import time
import pyscreeze
import PIL

os.chdir(
    "/Users/nossi/Desktop/samsung-rpa/auto_mail"
)
print(os.getcwd())

__PIL_TUPLE_VERSION = tuple(int(x) for x in PIL.__version__.split("."))
pyscreeze.PIL__version__ = __PIL_TUPLE_VERSION

app = xw.App(visible=False)

wb = app.books.open("auto_mail.xlsx")
ws = wb.sheets["total"]

name_list = ws.range("A2: A7").value
email_list = ws.range("B2: B7").value
tf_list = ws.range("C2: C7").value


def capture_image(image):
    img_capture = pyautogui.locateCenterOnScreen(image, confidence=0.7)
    x, y = img_capture
    return x / 2, y / 2


def get_mail_text(name, tf):
    mail_text = [
        f"Dear {name}, Thank you for participating in our company's interview."
    ]
    if tf == "T":
        mail_text.append(
            "WOWWOWOW, CONGRATULATION!!!!! We have decided on your final acceptance based on the results of the last interview."
        )
        mail_text.append("We sincerely congratulate you on your final passing.")
    else:
        mail_text.append(
            "T.T Despite your outstanding capabilities, we are unable to deliver good news due to limited recruitment."
        )
        mail_text.append("Thank you for your support.")
    return mail_text


def write_mail(mail_text):
    for text in mail_text:
        pyautogui.write(text, interval=0.01)
        pyautogui.press("enter")


x, y = capture_image("mail.png")
pyautogui.moveTo(x, y)
time.sleep(0.1)
pyautogui.click()
time.sleep(0.1)

for i, name in enumerate(name_list):
    mail_text = get_mail_text(name, tf_list[i])

    x, y = capture_image("mail.png")
    pyautogui.click(x, y)
    time.sleep(0.1)

    x, y = capture_image("receiver.png")
    pyautogui.click(x + 100, y)
    pyautogui.write(email_list[i], interval=0.01)
    pyautogui.moveTo(x + 300, y + 300)

    # x, y = capture_image("title.png")
    # pyautogui.click(x, y)

    pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.write(f"Dear {name}", interval=0.01)

    pyautogui.press("tab")
    write_mail(mail_text)

    x, y = capture_image("send.png")
    pyautogui.click(x, y)


xw.apps.active.quit()
