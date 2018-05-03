# stock-technical-analysis

Examining a strategy is so important for investors, but it seems not so easy. I used to make it with quantopian and zipline, they so great, but using them in China is so complicated. And i want to put some deep learning technology on stock analyzing and decision making. Here u can modify line 103 to change the condition of choose an action with different moving average lines. With some modification (line 95 to 103) u can put kdj or macd data. 

In traditional+kalman_ol_out.py some modification is added, so that kalman filter can be used. In order to find a good strategy to trade,
moving average lines are very important, we can consider the kalman filter as a moving average filter, we can also use it to draw our moving average line. Maybe here i should use online kalman filter, but i have some problem with 'filter_update'. 

Deep learning can help us a lot in real world problems, here some very easy supervised learning (regression) methodes were used, so we can predict the future value (t) with values (t-80:t-1). I trained the easy model (2 stacked LSTM and 1 FC), practically this job has no much 
meaning, but we can use it to draw line, just like moving average lines and kalman filter line. And traditional+kalman_dl_out.py works.
The result is shown in pic (mn-20), in the first subplot the stock price, MA20 (blue) and predicted price line (red) are displayed. In second subplot we can observe our portfolio under our policy (red) and the default policy :just holding long position all time (grey). Our policy can be even complicated, using different neural network models, using weights on different predicted results, and so on. Of course we can implement reinforcement learning ...

more details will be added soon ...
