
import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from itertools import count
import pandas as pd
from numpy import array

global tr_date
tr_date = '2015/3/25'
##tr_date = '2005/1/7'
##tr_date = '2017/1/5'

global hist
hist = 100

name='300'
stock_fath = '000'+name+'bis.csv'

df = pd.read_csv(stock_fath, parse_dates=True)
def load_csv_data(df,col):  
    data_pandas = df[col]
    data = data_pandas .as_matrix()
    result = data
    return result


class stock_env:
    def __init__(self):
        print ("init")
        self.price1 = load_csv_data(df,'close')
        self.price2 = load_csv_data(df,'open')
        self.dates = df['date']
        self.hist = hist
        self.test_episode = len(self.price1) - self.hist - 2
        self.train_done = False
        self.test_done = False
        self.budget = 10000
        self.num_stocks = 0
        self.tr = 50/100000   #25

    def reset(self):   
        global steps_done
        steps_done = 0
        self.budget = 10000
        self.num_stocks = 0
        self.train_done = False
        self.test_done = False
        
        state =self.price1[steps_done:steps_done+self.hist]
        return state

    def step(self, action): 
        global steps_done
        steps_done += 1

        if steps_done > self.test_episode:
            self.test_done = True
        

        pre_price = float(self.price2[steps_done + self.hist-1+1])
        pre_portfolio = self.budget + self.num_stocks * pre_price
        pre_date = self.dates[steps_done + self.hist-1+1]
        if action == 0 and pre_price >0: #buy
                    
            while self.budget >= pre_price*(1+self.tr):           
                self.budget -= pre_price *(1+self.tr)
                self.num_stocks += 1
        elif action == 1 and pre_price >0:       #sell
           
            while self.num_stocks > 0:       
                self.budget += pre_price*(1-self.tr)
                self.num_stocks -= 1
        else:
            pass

        try:

            state = self.price1[steps_done:steps_done+self.hist]
            price = float(self.price2[steps_done + self.hist+1])
            portfolio = self.budget + self.num_stocks * price
            date = self.dates[steps_done + self.hist+1]
            if date == tr_date:
                self.train_done = True

        except:
            pass
        return (state,self.train_done,self.test_done,pre_price,pre_portfolio,pre_date)

######################################################################

def select_action(state):
    state1 = state.copy()
    m1 = state1[-1]
    m5 = state1[-5:].mean()
    m10 = state1[-10:].mean()
    m13 = state1[-13:].mean()
    m20 = state1[-20:].mean()
    m30 = state1[-30:].mean()
    m60 = state1[-60:].mean()

    if m5 > m30:
        idx = 0
    else:
        idx = 1
    return idx


######################################################################
env = stock_env()

results = []
profits = []

benchresults = []
dates = []
colors = []


######################################################################
# Initialize the environment and state
state = env.reset()
tr_done = False
ts_done = False
record = False

for t in count(1):    
    action = select_action(state) 
    if action == 0: #buy
        color = 1.0
    else :
        color = 0.0
    next_state,  tr_done, ts_done,price,portfolio,date = env.step(action)
    if t == 0:
        zero_portfolio = portfolio
        zero_value = price
    if date == tr_date:
        ref_portfolio = portfolio
        ref_value = price
        record = True
    if record is True:            
        tt = ref_portfolio * price/ref_value        
        results.append(portfolio)
        benchresults.append(tt)
        dates.append(date)
        colors.append(color)           
    if ts_done:
        action = select_action(next_state)
        if action == 0: #buy
            advise = 'Buy'
        else :
            advise = 'Sell'
        break
            
    state = next_state
######################################################################  


#Plots
import matplotlib.cm as cm       
dates = pd.to_datetime(dates)
ax1 = plt.subplot2grid((20,1), (0,0), rowspan=18, colspan=1)
##ax1.set_yscale("log")
plt.title('U could '+advise+' 000'+name+'.SH at next opening.')
plt.ylabel('Portfolio ')

plt.grid(True)
ax2 = plt.subplot2grid((20,1), (19,0), rowspan=1, colspan=1, sharex=ax1)
plt.ylabel('Long') 
plt.grid(True)

ax1.plot(dates, benchresults, 'grey',label='benchmark')   
ax1.plot(dates, results, 'red',label='agent')   

ax2.fill_between(dates, colors, 0)

plt.show()

print('Complete : next opening U should', advise)
