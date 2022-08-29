# stock-technical-analysis

Examining a strategy is so important for investors, but it seems not so easy. I used to make it with quantopian and zipline, they so great, but using them in China is so complicated. And i want to put some deep learning technology on stock analyzing and decision making. Here u can modify line 103 to change the condition of choose an action with different moving average lines. With some modification (line 95 to 103) u can put kdj or macd data. 

In traditional+kalman_ol_out.py some modification is added, so that kalman filter can be used. In order to find a good strategy to trade,
moving average lines are very important, we can consider the kalman filter as a moving average filter, we can also use it to draw our moving average line. Maybe here i should use online kalman filter, but i have some problem with 'filter_update'. 

Deep learning can help us a lot in real world problems, here some very easy supervised learning (regression) methodes were used, so we can predict the future value (t) with values (t-80:t-1). I trained the easy model (2 stacked LSTM and 1 FC), practically this job has no much 
meaning, but we can use it to draw line, just like moving average lines and kalman filter line. And traditional+kalman_dl_out.py works.
The result is shown in pic (mn-20), in the first subplot the stock price, MA20 (blue) and predicted price line (red) are displayed. In second subplot we can observe our portfolio under our policy (red) and the default policy: just holding long position all time (grey). Our policy can be even complicated, using different neural network models, using weights on different predicted results, and so on. Of course we can implement reinforcement learning ...


to train RL, maybe abundent seqence data is required. yes we can get data, but sequence data of tickers is not independ. if we use ticker data one by one, it is cheating. 
suppose i can find a good classifier, which can tell me the tickers with high possibilties go up. i can use the classifier to choose which to buy. the result of the classifier across all ticker can be think as value function. and our policy is choose the n highest values to buy.

i have programmed the back test, past 60 weeks, about 20% revenue. 
data for training and backtesting is huge, so i will put it somewhere later.

data for training:

3 classes (>15%,<-15%,abs<5%)
x_train shape: (134503, 200, 5)
134503 train samples
x_test shape: (11569, 200, 5)
11569 test samples

if d < pd.Timestamp(2020, 7, 1, 12):   
        train_data_list.append(img_tensor)  
        target_list.append(p)
      elif d < pd.Timestamp(2021, 7, 1, 12):
        test_data_list.append(img_tensor)  
        test_target_list.append(p)
        
model:

Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 conv1d_12 (Conv1D)          (None, 100, 32)           832       
                                                                 
 dropout_18 (Dropout)        (None, 100, 32)           0         
                                                                 
 conv1d_13 (Conv1D)          (None, 50, 64)            10304     
                                                                 
 dropout_19 (Dropout)        (None, 50, 64)            0         
                                                                 
 conv1d_14 (Conv1D)          (None, 25, 128)           41088     
                                                                 
 dropout_20 (Dropout)        (None, 25, 128)           0         
                                                                 
 bidirectional_4 (Bidirectio  (None, 32)               18560     
 nal)                                                            
                                                                 
 dropout_21 (Dropout)        (None, 32)                0         
                                                                 
 flatten (Flatten)           (None, 32)                0         
                                                                 
 dense_4 (Dense)             (None, 32)                1056      
                                                                 
 dropout_22 (Dropout)        (None, 32)                0         
                                                                 
 dense_5 (Dense)             (None, 3)                 99        
                                                                 
=================================================================
Total params: 71,939
Trainable params: 71,939
Non-trainable params: 0

result:
Epoch 1840: val_loss did not improve from 0.97957
526/526 [==============================] - 8s 15ms/step - loss: 0.8317 - accuracy: 0.6267 - val_loss: 1.0273 - val_accuracy: 0.5006




