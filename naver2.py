from bs4 import BeautifulSoup
from selenium import webdriver
import time, sys, math

#필요한 정보를 입력 받습니다
query_txt = input("검색어는? : ")
cnt = int(input("몇 건 수집할까요? : "))
s_date = input("시작날짜(ex. 20210101) : ")
e_date = input("종료날짜(ex. 20210501) : ")
page_cnt = math.ceil(cnt / 50)  # 크롤링 할 페이지 수 
f_name = "c:\\py_temp\\" + str(e_date) + "_naver.txt"

#Step 2. 크롬 드라이버로 웹 브라우저를 실행 후 수집대상까지 접근합니다.
driver = webdriver.Chrome("c:/py_temp/chromedriver.exe")
query_link = "https://search.naver.com/search.naver?where=view&query=" +query_txt+ "&sm=tab_opt&nso="
query_link += "so%3Ar%2Cp%3Afrom" +str(s_date)+ "to" +str(e_date)+ "%2Ca%3Aall&mode="
query_link += "normal&main_q=&st_coll=&topic_r_cat="

driver.get(query_link)
time.sleep(2)

def scroll_down(driver):
  driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
  time.sleep(5)

i = 1
while (i <= page_cnt):
      scroll_down(driver) 
      i += 1

soup = BeautifulSoup(driver.page_source, 'html.parser')
view_list = soup.find('ul', class_='lst_total _list_base').find_all('li') 

for i in view_list:
    f = open(f_name, 'a', encoding='UTF-8')

    contents = i.find('div', 'total_wrap api_ani_send').get_text().replace("\n","")                                  
    f.write(": 내용 :" + str(contents) + "\n")
    print(contents)
    f.close( )

       
    print("\n")
    time.sleep(1) 

driver.close()


