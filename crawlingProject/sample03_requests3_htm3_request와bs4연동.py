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
         * CSS 선택자
         1. 태그명
         2. id 속성: #id값
            ==> 하나의 html파일안에서 유일한 값으로 설정해야 된다.
         3. class 속성:  .class값
            => 나의 html파일안에서  중복 값으로 설정가능하다.
         4. 계층구조
            자식:  부모 > 자식
            자손:  부모  자손(자식포함)
         5. 형제
            바로뒤형제:  기준태그 + 태그
            뒤의 형제들: 기준태그 ~ 태그
         6. 속성 :
           - [속성명], 태그명[속성명]
           -[속성명=값]   ==> 값이 정확하게 일치
           -[속성명^=값]  ==> 값으로 시작하는
           -[속성명$=값]  ==> 값으로 끝나는
         7. n번째 반환 :  nth-child(n)
         8. selenium

           ==> 크롤링 자동화
           ==> 가상의 웹 브라우저 활용
'''
# pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup

url = "http://www.daum.net"
res = requests.get(url)
print(res.text)

soup = BeautifulSoup(res.text, "html.parser")
tag = soup.select(".list_mainsvc > li > a > span")
for d in tag:
    print(d.string)
