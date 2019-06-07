import time as ttime
import pandas as pd
import numpy as np


for i in range(100):
    with open('test.txt', 'w') as fp:
        d = pd.DataFrame(np.array([[i]*3]*3), columns=['a', 'b', 'c'])
        d.to_csv(fp)
        # fp.write(f'iteration {i+1}\n')
        ttime.sleep(1)

