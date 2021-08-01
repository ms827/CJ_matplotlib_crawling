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
  파이차트(pie plot)
  
'''
ratio= [34,32,16,18]
label=["Apple","Banana","Melon","Grapes"]
colors = ["GreenYellow","Khaki","DarkBlue","Blue"]

plt.pie(ratio,labels=label, autopct="%.1f%%",colors=colors, explode=[0, 0.2, 0, 0])
plt.show()