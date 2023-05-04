import sys

import pandas as pd
import requests
from newspaper import Article
from konlpy.tag import Okt
from collections import Counter, OrderedDict
import matplotlib
import matplotlib.pyplot as plt
from wordcloud import WordCloud

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

df = pd.DataFrame()
totalDataList = list()
l = list()

# 수집하려는 키워드와 페이지 추출
data_keyword = input("수집하고자 하는 키워드를 입력해주세요.: ")
data_page = input("수집하고자 하는 페이지를 입력해주세요.: ")

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(1)
driver.get("https://www.naver.com")
time.sleep(2)

# 검색창에 키워드 입력
form_elements = driver.find_elements(By.CLASS_NAME, "input_text")
form_elements[0].send_keys(data_keyword)
time.sleep(2)

# 키워드 입력후 버튼 클릭
driver.find_elements(By.CLASS_NAME, "btn_submit")[0].click()
time.sleep(2)

# 창 전환 후 뉴스탭 클릭
form_elements = driver.find_elements(By.CLASS_NAME, "menu")
for i in range(len(form_elements)):
    if form_elements[i].text == "뉴스":
        form_elements[i].click()
        time.sleep(2)

# 뉴스탭 이동 후 해당 페이지 클릭
for i in range(1, data_page + 1):
    page_xpath = f'//*[@id="main_pack"]/div[2]/div/div/a[{data_page}]'
    driver.find_element(By.XPATH, page_xpath).click()
    time.sleep(2)

    # 뉴스 기사 제목, 내용
    new_title = driver.find_elements(By.CSS_SELECTOR, 'a.news_tit')

    for i in new_title:
        news_href_ = i.get_attribute("href")

        article = Article(news_href_, language="ko")

        try:
            article.download()
            article.parse()
        except:
            continue

        articleList = l.append(article)

# 주소값 추출
# get_attribute

driver.close()
