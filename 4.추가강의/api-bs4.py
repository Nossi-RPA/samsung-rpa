import requests
from bs4 import BeautifulSoup
import xlwings as xw

wb = xw.Book()
ws = wb.sheets[0]
a1_cell = ws.range("A1")
b1_cell = ws.range("B1")

res = requests.get(url="https://finance.naver.com/")

soup = BeautifulSoup(res.text, "html.parser")
tbody_element = soup.find("tbody", id="_topItems2")
a_tags = tbody_element.find_all("a")
for i, a_tag in enumerate(a_tags):
    code = a_tag.get("href").split("=")[1]
    print(a_tag.text, code)

    a1_cell.offset(i, 0).value = a_tag.text
    b1_cell.offset(i, 0).number_format = "000000"
    b1_cell.offset(i, 0).value = str(code)
