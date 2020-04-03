# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 11:38:49 2020

@author: currysesame
"""


import numpy as np
import copy

nphs = np.hstack
# create the work table
z0 = np.zeros((6,64))
#initialize the begining of each possible work.
for i in range(0, 32):
    z0[0,2*i] = 20
    z0[0,2*i+1] = 5
# plan sheet determine the site which is yellable or not
plan_sheet = np.zeros((32,5))
plan_sheet[:16,0] = 1
plan_sheet[:8,1] = 1
plan_sheet[16:24,1] = 1

for i in range(4):
    plan_sheet[8*i:8*(i+1)-4,2] = 1
for i in range(8):
    plan_sheet[4*i:4*(i+1)-2,3] = 1  
for i in range(16):
    plan_sheet[2*i:2*(i+1)-1,4] = 1  

plan_sheet_t = np.transpose(plan_sheet)
# fit all these work details
for j in range(0,32):
    gain = 80
    cost = 20
    for i in range(1, len(z0)):
        z0[i,2*j] = z0[i-1,2*j] + gain
        z0[i,2*j+1] = z0[i-1,2*j+1] + cost
        if i == 1:
            gain = 100
            cost = 25
            z0[i,2*j] = z0[i,2*j] + 20
            if plan_sheet[j,0] == 1:
                z0[i,2*j] = z0[i,2*j] + 40
                z0[i,2*j+1] = z0[i,2*j+1] + 20
        if i == 2:
            z0[i,2*j] = z0[i,2*j] + 40
            gain = 200
            cost = 100
            if plan_sheet[j,1] == 1:
                z0[i,2*j] = z0[i,2*j] + 80
                z0[i,2*j+1] = z0[i,2*j+1] + 40
        if i == 3:
            z0[i,2*j] = z0[i,2*j] + 60
            cost = 150
            if plan_sheet[j,2] == 1:
                z0[i,2*j] = z0[i,2*j] + 240
                z0[i,2*j+1] = z0[i,2*j+1] + 100
        if i == 4:
            z0[i,2*j] = z0[i,2*j] + 60
            cost = 200
            if plan_sheet[j,3] == 1:
                z0[i,2*j] = z0[i,2*j] + 240
                z0[i,2*j+1] = z0[i,2*j+1] + 100
        if i == 5:
            z0[i,2*j] = z0[i,2*j] + 60
            if plan_sheet[j,4] == 1:
                z0[i,2*j] = z0[i,2*j] + 300
                z0[i,2*j+1] = z0[i,2*j+1] + 120


collect = []
collect.append([z0[0,0],z0[0,1], 0, plan_sheet[0,0],plan_sheet[0,1],plan_sheet[0,2],plan_sheet[0,3],plan_sheet[0,4]])
for i in range(1,len(z0)):
    j = 2 ** i
    jump = np.int(64/j)
    jump_sec = np.int(32/j)
    for k in range(0,j):
        collect.append([z0[i,k*jump], z0[i,k*jump + 1], i, plan_sheet[k*jump_sec,0],plan_sheet[k*jump_sec,1],plan_sheet[k*jump_sec,2],plan_sheet[k*jump_sec,3],plan_sheet[k*jump_sec,4]])

collect = np.float32(np.asarray(collect))

go0 = sorted(range(len(collect[:,0])), key=lambda k: (collect[:,0])[k])
sort00 = collect[go0,0]
sort01 = collect[go0,1]
sort02 = collect[go0,2]
sort03 = collect[go0,3]
sort04 = collect[go0,4]
sort05 = collect[go0,5]
sort06 = collect[go0,6]
sort07 = collect[go0,7]
sort00 = sort00[:,np.newaxis]
sort01 = sort01[:,np.newaxis]
sort02 = sort02[:,np.newaxis]
sort03 = sort03[:,np.newaxis]
sort04 = sort04[:,np.newaxis]
sort05 = sort05[:,np.newaxis]
sort06 = sort06[:,np.newaxis]
sort07 = sort07[:,np.newaxis]

sort = nphs((nphs((nphs((nphs((nphs((nphs((nphs((sort00, sort01)),sort02)),sort03)),sort04)),sort05)),sort06)),sort07))

#same temp
temp_init = sort[0,:]
for i in range(1, len(sort)):
    temp = sort[i,:]
    if temp[0] == temp_init[0] and temp[1] == temp_init[1]:
        sort[i-1,0] = 0
        sort[i-1,1] = 0
    temp_init = temp
sort = sort[np.all(sort[:,0:2] != 0, axis=1)]  # delete the rows contain zero

#cost is larger
temp_init = sort[0,:]
for i in range(1, len(sort)):
    temp = sort[i,:]
    if temp[1] - temp_init[1] < 0:
        sort[i-1,0] = 0
        sort[i-1,1] = 0
    temp_init = temp
sort = sort[np.all(sort[:,0:2] != 0, axis=1)]  # delete the rows contain zero

#cost is larger
temp_init = sort[0,:]
for i in range(1, len(sort)):
    temp = sort[i,:]
    if temp[1] - temp_init[1] < 0:
        sort[i-1,0] = 0
        sort[i-1,1] = 0
    temp_init = temp
sort = sort[np.all(sort[:,0:2] != 0, axis=1)]  # delete the rows contain zero

#same cost diff gain
temp_init = sort[0,:]
for i in range(1, len(sort)):
    temp = sort[i,:]
    if temp[0] - temp_init[0] > 0 and temp[1] == temp_init[1]:
        sort[i-1,0] = 0
        sort[i-1,1] = 0
    temp_init = temp
sort = sort[np.all(sort[:,0:2] != 0, axis=1)]  # delete the rows contain zero
#same gain diff cost
temp_init = sort[-1,:]
for i in range((len(sort)-2),0,-1):
    temp = sort[i,:]
    if temp[0] == temp_init[0] and temp[1] - temp_init[1]<0:
        sort[i+1,0] = 0
        sort[i+1,1] = 0
    temp_init = temp
sort = sort[np.all(sort[:,0:2] != 0, axis=1)]  # delete the rows contain zero

sort_unique = sort
diff00 = sort_unique[1:,0] - sort_unique[0:-1,0]
diff01 = sort_unique[1:,1] - sort_unique[0:-1,1]

diff_real00 = np.zeros(len(sort_unique))
diff_real00[0] = diff00[0]
diff_real00[len(diff_real00) - 1] = diff00[len(diff00) - 1]
for i in range(1, (len(diff_real00)-1)):
    diff_real00[i] = (diff00[i-1] + diff00[i])/2

diff_real01 = np.zeros(len(sort_unique))
diff_real01[0] = diff01[0]
diff_real01[len(diff_real01) - 1] = diff01[len(diff01) - 1]
for i in range(1, (len(diff_real01)-1)):
    diff_real01[i] = (diff01[i-1] + diff01[i])/2
    


def gain(cases):
    sumation = 0
    for i in range(len(cases)):
        sumation += sort_unique[cases[i],0]
    return sumation

def cost(cases):
    sumation = 0
    for i in range(len(cases)):
        sumation += sort_unique[cases[i],1]
    return sumation

def cost_function(cases):
    return ((gain(cases) -10001)**2 + (cost(cases))**2) **(0.5)

def dcost_dx1(cases):
    dcost_cases = np.zeros(len(cases))
    for i in range(0, len(cases)):
        dcost_cases[i] =  2000*(-2)*(gain(cases) -10001)* diff_real00[cases[i]] -2*(cost(cases))*diff_real01[cases[i]] 
    return dcost_cases

def roundoff(values, low, high):
    for i in range(0, len(values)):
        if values[i]>=high:
            values[i] = high
        if values[i]<=low:
            values[i] = low
    return values
        
Mem = []
for j in range(0, 500):
    cases = np.random.randint(len(sort_unique), size=7)

    memory = []  
    for i in range(0, 250):
        
        print('===')
        print('case_init', cases)
        
        cfunction = cost_function(cases)
        gains = gain(cases)
        costs = cost(cases)
        print('gain', gains)
        print('cost', costs)
        print('2 cost', cfunction)
        if gains >= 1e4 and costs < 4200:
        
            memory.append(cases)
            memory.append(gains)
            memory.append(costs)
            memory.append(cfunction)
        
        dcost_dxs = dcost_dx1(cases)
        
        digits = 0
        while((abs(dcost_dxs[0])) >= 10):
            dcost_dxs = dcost_dxs /10
            digits += 1
        dcost_dxs_round = np.round(dcost_dxs)
        dcost_dxs_round = roundoff(dcost_dxs_round, -3, 3)
        print(dcost_dxs_round)
        cases_new = copy.copy(cases)
        cases_new[np.int(i%7)] += dcost_dxs_round[np.int(i%7)]
        print('new',cases_new)
        cases_new = roundoff(cases_new, 0, (len(sort_unique)-1))
        cases_new = cases_new.astype(int)
        
        cases = cases_new
    


    if len(memory) == 0:
        print('No result!!')
    result = [] 
    if len(memory)>0:
        for i in range(0, np.int(len(memory)/4)):
            case = memory[4*i]
            gain_sum = 0
            cost_sum = 0
            steps_sum = 0
            call1_sum = 0
            call2_sum = 0
            call3_sum = 0
            call4_sum = 0
            call5_sum = 0
            for i in range(0,len(case)):    
                box = sort[case[i],:]
                result.append(box)
                gain_sum += box[0]
                cost_sum += box[1]
                steps_sum += box[2]
                call1_sum += box[3]
                call2_sum += box[4]
                call3_sum += box[5]
                call4_sum += box[6]
                call5_sum += box[7]
            sum_result = []
            sum_result = [gain_sum, cost_sum, steps_sum, call1_sum, call2_sum, call3_sum, call4_sum, call5_sum]
            result.append(sum_result)
        result = np.asarray(result)
        Mem.append(result)
    
