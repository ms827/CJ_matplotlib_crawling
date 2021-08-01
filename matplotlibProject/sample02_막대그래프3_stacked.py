'''
  시각화
  1. matplotlib 패키지 사용
  2. pandas 시각화 제공 ( matplotlib 기능 일부분 제공 )
  3. matplotlib  +seaborn 패키지
  설치
  pip install matplotlib
'''
import matplotlib.pyplot as plt
import numpy as np
# 한글설정
plt.rc("font", family="Malgun Gothic")

men =[20,35,30,35,27]
woman = [25, 32, 34, 20, 25]

x = np.arange(5)

bar1 = plt.bar(x, men, label="남")
bar2 = plt.bar(x, woman, bottom=men, label="여")
plt.title("학년별 성별 비율")
plt.xticks(x, ["1학년","2학년","3학년","4학년","5학년"])
plt.legend()
plt.show()


