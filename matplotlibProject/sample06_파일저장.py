'''
    시각화
    1. matplotlib 패키지 사용
    2. pandas시각화 제공 ( matplotlib 기능 제공)

'''

import matplotlib.pyplot as plt
import numpy as np
#한글설정
import pandas as pd

plt.rc("font", family="Malgun Gothic")
'''
  box
  
'''
np.random.seed(1234)
df = pd.DataFrame(np.random.random(10))
print(df)
plt.boxplot(df)
file = plt.gcf()  # 파일에 저장할 준비
plt.show()
file.savefig("test.png")