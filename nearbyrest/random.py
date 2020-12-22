import pandas as pd
import numpy as np
np.random.seed(1)
data4 =pd.DataFrame({"X"  : np.random.choice(range(1,5), 20, replace=True),
                     "X1" : np.where(np.random.normal(0.0, 1.0, size=20)<=0,0,1)})