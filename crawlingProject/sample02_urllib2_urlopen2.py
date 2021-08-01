'''
   웹 크롤링 (Crawling)
   1. 웹(web) 사이트의 문서(html)를
      파싱해서 원하는 데이터를 수집하는 작업 의미
   2. python 에서 사용가능한 네트워크 라이브러리
     가. urllib 라이브러리: 파이썬 내장
        - urlretrieve 함수: 다운로드 기능
        - urlopen 함수 : 요청해서  readXXX 함수로 데이터 읽기 가능
     나. requests 라이브러리: 외부에서 제공(아파치 재단 )
'''

from urllib.request import urlretrieve, urlopen

html_url= "http://python.org"

try:
   res = urlopen(html_url)
   for line  in res.readlines():
       print(line.decode("utf-8"), end="")

except Exception as e:
    print("error:", e)

print("end")



