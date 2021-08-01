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


n = np.arange(0,2, 0.2)

plt.subplot(3,1,1) # 앞의 두자리는 행렬의 모양, 마지막값은 보여줄 순서값
plt.plot(n, n, "bo", label="a")
plt.subplot(3,1,3) # 앞의 두자리는 행렬의 모양
plt.plot(n, n**2, linestyle="--", color="red" , label="b")
plt.subplot(3,1,2) # 앞의 두자리는 행렬의 모양
plt.plot(n, n**3, label="c")

plt.xlabel("X값")
plt.ylabel("Y값")
plt.legend()
plt.show()