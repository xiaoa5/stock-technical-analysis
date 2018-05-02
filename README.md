# stock-technical-analysis

Examining a strategy is so important for investors, but it seems not so easy. I used to make it with quantopian and zipline, they so great, but using them in China is so complicated. And i want to put some deep learning technology on stock analyzing and decision making. Here u can modify line 103 to change the condition of choose an action with different moving average lines. With some modification (line 95 to 103) u can put kdj or macd data. 

In traditional+kalman_ol_out.py some modification is added, so that kalman filter can be used. In order to find a good strategy to trade,
moving average lines are very important, we can consider the kalman filter as a moving average filter, we can also use it to draw our moving average line. Maybe here i should use online kalman filter, but i have some problem with 'filter_update'. 

more details will be added soon ...
