import numpy as np
import pandas as pd
import time as ttime


for i in range(100):
    with open('test.txt', 'w') as fp:
        d = pd.DataFrame(np.array([[i]*3]*3), columns=['a', 'b', 'c'])
        d.to_csv(fp)
        fp.flush()
        ttime.sleep(1)
