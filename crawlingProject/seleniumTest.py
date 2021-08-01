'''
  다나와 사이트의 노트북
  1) URL은 변경되지 않는데.... 화면이 변경됨(Ajax)
  2) 숨겨져있는 버튼을 클릭하고 내용확인하여 보기- apple 제품
  3) 페이징 처리
'''

from selenium import webdriver
import time
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
#  webdriver 설정 - Headless 모드
browser = webdriver.Chrome('./webdriver/chrome/chromedriver.exe', options=chrome_options)
# browser = webdriver.Chrome('./webdriver/chrome/chromedriver.exe')

#  webdriver 설정 - 일반 모드
# browser = webdriver.Chrome('./webdriver/chrome/chromedriver.exe')

# 크롬 브라우저 내부 대기
browser.implicitly_wait(5)

# 브라우저 사이즈
browser.maximize_window()

# 페이지 이동:  다나와사이트의 노트북
browser.get("http://prod.danawa.com/list/?cate=112758&15main_11_02")

# 1차 페이지 내용
# print("Before Page Contents: {}".format(browser.page_source))

# 제조사벼 더 보기 클릭1
# 클릭하고자 하는 버튼등이 모두 랜더링 된후에 클릭 가능하도록  wait시간을 지정한다.
# Explicit wait => 최대 3초동안 기다리지만, 랜더링되면 바로 적용시킴
WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH,'//*[@id="dlMaker_simple"]/dd/div[2]/button[1]'))).click()
#//*[@id="dlMaker_simple"]/dd/div[2]/button[1]
# 제조사벼 더 보기 클릭 2
# Implicitly wait ==> 무조건 2초동안 wait한다.
# time.sleep(2)
# browser.find_element_by_xpath('//*[@id="dlMaker_simple"]/dd/div[2]/button[1]').click()


# 원하는 카테고리 선택 ==> apple 선택
WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="selectMaker_simple_priceCompare_A"]/li[12]/label'))).click()
#//*[@id="selectMaker_simple_priceCompare_A"]/li[16]/label
# 2차 페이지 내용
print("After Page Contents: {}".format(browser.page_source))

time.sleep(5) # ************** 반드시 필요 ( 없으면 apple 상품 아닌 다른 상품이 출력됨 )

# bs4
soup = BeautifulSoup(browser.page_source, 'html.parser')

# print(soup.prettify())

# 메인 상품 리스트 선택
pro_list = soup.select("div.main_prodlist.main_prodlist_list > ul > li")

# 상품 리스트 확인
# print(pro_list)

# 필요 정보 추출
for v in pro_list:
    # print(v)
    # if not v.find("div", class_="ad_header"):
    if not v.select("div.ad_header"):

        # 상품명, 이미지, 가격
        print("상품명:",v.select('p.prod_name > a')[0].text.strip())
        # print("src:", v.select('a.thumb_link > img')[0]['src'])
        # xxx = v.select('a.thumb_link > img')[0]
        # print(xxx.get('data-original'))
        if v.select('a.thumb_link > img')[0].get('data-original'):
            print("이미지:", v.select('a.thumb_link > img')[0]['data-original'])
        else:
            print("이미지:", v.select('a.thumb_link > img')[0]['src'])

        print("가격:", v.select('p.price_sect > a')[0].text.strip())
    print()

# 브라우저 종료
browser.quit()