# 패키지와 모듈 불러오기
from selenium import webdriver
import os, sys, time

# 웹페이지 자동 접속하기와 응용
# ("/Users/유저명/py_temp/chromedriver.exe") # 맥
driver = webdriver.Chrome("c:/py_temp/chromedriver.exe")
time.sleep(3)
driver.get("http://www.naver.com/")

# 창 크기 최대화
time.sleep(2)
driver.maximize_window()

# 엘리먼트 찾아 제어하기
time.sleep(2)
driver.find_element_by_id("query").send_keys("빅데이터"+"\n")

time.sleep(2)
driver.find_element_by_link_text("VIEW").click()

time.sleep(2)
driver.find_element_by_xpath('//*[@id="snb"]/div[1]/div/div[1]/a[2]').click()

time.sleep(5)
driver.close()

