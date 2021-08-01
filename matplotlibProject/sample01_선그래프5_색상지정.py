'''
    시각화
    1. matplotlib 패키지 사용
    2. pandas시각화 제공 ( matplotlib 기능 제공)

'''

import matplotlib.pyplot as plt
#한글설정
plt.rc("font", family="Malgun Gothic")
'''
    색상지정
    1) 'b','r',...
    2) 색상명
    3) 16진수 색상
'''

# plt.plot([1,2,3,4],[1,4,9,16],"r")
# plt.plot([1,2,3,4],[1,4,9,16],"MistyRose")
plt.plot([1,2,3,4],[1,4,9,16],"#e35F62")
plt.xlabel("X값")
plt.ylabel("Y값")
plt.axis([0,5,0,20])
plt.show()