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

plt.plot([1,2,3,4],[1,4,9,16],marker="^",linestyle="--",color="violet")
plt.xlabel("X값")
plt.ylabel("Y값")
plt.axis([0,5,0,20])
plt.show()