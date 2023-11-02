# import requests
# from bs4 import BeautifulSoup

# base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
# keyword = input("검색어를 입력하세요 : ")

# search_url = base_url + keyword
# res = requests.get(search_url)

# soup = BeautifulSoup(res.text, "html.parser")

# print(soup)
# # items = soup.select(".api_txt_lines.total_tit")
# # for i, item in enumerate(items, 1):
# #     print(f"{i} : [제목] {item.text} [url] {item.get('href')} ")
