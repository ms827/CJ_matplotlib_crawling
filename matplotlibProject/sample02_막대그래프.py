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

x = np.arange(4)
y = [100,300,400,150]
plt.bar(x,y)
plt.xticks(x, ["2002","2003","2004","2005"])
plt.show()



