'''
    시각화
    1. matplotlib 패키지 사용
    2. pandas시각화 제공 ( matplotlib 기능 제공)

'''

import matplotlib.pyplot as plt
#한글설정
plt.rc("font", family="Malgun Gothic")
'''
  
'''
x=[1,2,3,4]
y=[1,4,9,16]
plt.plot(x,y)
plt.xlabel("X값")
plt.ylabel("Y값")
plt.axis([0,5,0,20])
plt.fill_between(x[1:3],y[1:3], alpha=0.3) # alpha값은 작을수록 투명해진다
plt.show()