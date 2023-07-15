#data should be houarly 
data['leaf_wetness'] = (data['RH'] >= 85).astype(int)

LWD = data['leaf_wetness'].resample('D').sum()
LWD 
