#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 20:24:49 2017

@author: gprat
"""
import pandas as pd
import matplotlib.pyplot as plt
isigmas=[0,1,2,3]
for isigma in isigmas:
    
    f='C:\Users\xiaji\Google Drive\ccnss2017_students-master\module2\day3_miniprojects\Module2_RL_day3_psychophysics/trial_types_isigma'+str(isigma)+'.csv'
    df=pd.read_csv(f,sep=',')
    
    plt.plot(df['prob_left'],'r-')
    plt.plot(df['prob_right'],'b-')
    plt.ylim(0.2,0.8)
    plt.figure()
    
    