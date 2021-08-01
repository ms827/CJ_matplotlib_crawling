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
   3. 브라우저에서 요청시 서버에서 반환하는 데이터 타입 종류
     가. html ( html 파싱(검색) 용이하도록 제공하는 라이브러리: Beautiful Soup (bs4)
     나. json ( import json, json.loads() 필요)
     다, xml
     라. etc(
   4. 매우 중요하다.
    ==> 웹브라우저가 html을 보여줄 때, html을 특별한 구조로 생성한다. ( DOM 트리)
      DOM: Document Object Model
    ==> html 태그를 트리(tree) 구조로 만든다.
   5. CSS 선택자(selector) 이용하여 DOM 트리를 참조할 수 있다.
     - CSS 선택자는 CSS,Javascript,bs4 에서 활용된다.
   6. bs4 DOM 트리를 참조하는 방법은 2가지 이다.
     가. find(태그명) :  1개 반환
        find_all(태그명): 전부 반환
        예>
            find(name=태그명") : 일치하는 첫번째 태그 반환
            find_all(name=태그명") : 일치하는 모든 태그 반환 ( 리스트로 반환 )
            find_all(태그명") : 일치하는 모든 태그 반환 ( 리스트로 반환 )
            find_all({태그명","태그명2"}) : 멀티 태그 반환 ( 리스트로 반환 )
    나. select_one(CSS 선택자) : 1개 반환
        select(CSS 선택자) : 전부 반환
'''
# pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup

html_str = '''
      <html>
        <head>
           <title>The Dormouse's story</title>
        </head>  
       <body>
          <h1>this is h1 area</h1>
          <h2>this is h2 areaAAA</h2>
          <h2>this is h2 areaBBB</h2>
          <p class="title"><b>The Dormouse's story</b></p>
       </body>
    </html>
'''
# 1. bs4 초기화
soup = BeautifulSoup(html_str, "html.parser")
h1_tag = soup.find(name="h1")
print(h1_tag, h1_tag.string)

h2_tag = soup.find_all("h2")
print(h2_tag)
for d in h2_tag:
    print(d.string)

h1_h2_tag = soup.find_all({"h1","h2"})
print(h1_h2_tag)





