import time as ttime
import pandas as pd
import numpy as np


try:
    for i in range(100):
        fp = open('test.txt', 'w')
        d = pd.DataFrame(np.array([[i]*3]*3), columns=['a', 'b', 'c'])
        d.to_csv(fp)
        fp.flush()
        ttime.sleep(1)
except Exception as e:
    fp.close()
    print(e)
finally:
    fp.close()
