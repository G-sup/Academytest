import numpy as np
import pandas as pd
import tensorflow.keras.backend as K


# x = []
# for i in range(1,2):
#     df = pd.read_csv(f'./dacon-data/submission_{i}.csv', index_col=0, header=0)
#     data = df.to_numpy()
#     x.append(data)

# x = np.array(x)

# df = pd.read_csv(f'./dacon-data/submission_{i}.csv', index_col=0, header=0)
# for i in range(7776):
#     for j in range(9):
#         a = []
#         for k in range(1):
#             a.append(x[k,i,j].astype('float32'))
#         a = np.array(a)
#         df.iloc[[i],[j]] = (pd.DataFrame(a).astype('float32').quantile(0.5,axis = 0)[0]).astype('float32')
        
# y = pd.DataFrame(df, index = None, columns = None)
# y.to_csv('./dacon-data/submission_ex.csv')  