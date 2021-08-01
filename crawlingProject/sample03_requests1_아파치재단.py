  
'''
   웹 크롤링 (Crawling)
   1. 웹(web) 사이트의 문서(html)를
      파싱해서 원하는 데이터를 수집하는 작업 의미
   2. python 에서 사용가능한 네트워크 라이브러리
     가. urllib 라이브러리: 파이썬 내장
        - urlretrieve 함수: 다운로드 기능
        - urlopen 함수 : 요청해서  readXXX 함수로 데이터 읽기 가능
     나. requests 라이브러리: 외부에서 제공(아파치 재단 )
         import requests
'''

import requests

html_url= "http://python.org"
res = requests.get(html_url)
print(dir(res))
'''
'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed',
 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 
 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status',
  'raw', 'reason', 'request', 'status_code', 'text', 'url']
'''
print(res.text) # 전체 html 문서
print(res.url) # https://www.python.org/
print(res.headers) # 헤더 정보:
print(res.status_code) # 200 ( 모두 성공 )