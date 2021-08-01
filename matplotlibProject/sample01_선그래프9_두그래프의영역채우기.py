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
y1=[1,4,9,16]
y2=[1,2,4,8]

plt.plot(x,y1)
plt.plot(x,y2)
plt.xlabel("X값")
plt.ylabel("Y값")
plt.axis([0,5,0,20])
plt.fill_between(x[1:3],y1[1:3], y2[1:3], alpha=0.3) # alpha값은 작을수록 투명해진다
plt.show()