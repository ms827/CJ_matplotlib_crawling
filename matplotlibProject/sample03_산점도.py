'''
    시각화
    1. matplotlib 패키지 사용
    2. pandas시각화 제공 ( matplotlib 기능 제공)

'''

import matplotlib.pyplot as plt
import numpy as np
#한글설정
plt.rc("font", family="Malgun Gothic")
'''
  산점도(scatter plot)
  - 두 개의 값을 x와 y의 좌표를 점으로 표현하는 그래프이다.
  - 상관관계
  
'''
np.random.seed(1234)  # 랜덤값 고정
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
s_size = (30 * np.random.rand(50))**2
plt.scatter(x,y, c=colors, s=s_size, marker="^")
plt.show()