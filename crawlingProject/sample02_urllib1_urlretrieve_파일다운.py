'''
   웹 크롤링 (Crawling)
   1. 웹(web) 사이트의 문서(html)를
      파싱해서 원하는 데이터를 수집하는 작업 의미
   2. python 에서 사용가능한 네트워크 라이브러리
     가. urllib 라이브러리: 파이썬 내장
        - urlretrieve 함수: 다운로드 기능
     나. requests 라이브러리: 외부에서 제공(아파치 재단 )
'''

from urllib.request import urlretrieve

img_url = "https://t1.daumcdn.net/daumtop_chanel/op/20200723055344399.png"
html_url= "http://python.org"

save_img_path = r"c:\daum.gif"
save_html_path = r"c:\python.html"


try:
    urlretrieve(img_url, save_img_path)
    urlretrieve(html_url, save_html_path)

except Exception as e:
    print("error:", e)

print("end")


