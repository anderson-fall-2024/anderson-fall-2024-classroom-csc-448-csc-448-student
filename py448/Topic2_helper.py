def score(s1,s2):
    s = 0
    # YOUR SOLUTION HERE
    ## BEGIN SOLUTION
    for i in range(min(len(s1),len(s2))):
        if s1[i] == s2[i]:
            s += 1
    ## END SOLUTION
    return s

def score2(s1,s2):
    s = 0
    # YOUR SOLUTION HERE
    ## BEGIN SOLUTION
    for ix1 in range(len(s1)):
        if s1[ix1] != '-':
            break
    for ix2 in range(len(s1[::-1])):
        if s1[len(s1)-ix2-1] != '-':
            break
    ix2 = len(s1)-ix2
    for jx1 in range(len(s2)):
        if s2[jx1] != '-':
            break
    #print(s2[::-1])
    for jx2 in range(len(s2[::-1])):
        if s2[len(s2)-jx2-1] != '-':
            break
    jx2 = len(s2) - jx2
    #print(jx1,ix1)
    #print(jx2,ix2)
    for i in range(max(jx1,ix1),min(jx2,ix2)):
        if s1[i] == s2[i]:
            s += 1
        elif s1[i] == '-' or s2[i] == '-':
            s -= 0.5
        #else:
        #    s -= 0.5
    ## END SOLUTION
    return s

import numpy as np

def min_num_coins(money,coins):
    min_coins = np.inf
    ## BEGIN SOLUTION
    if money == 0:
        return 0
    for c in coins:
        if money >= c:
            num_coins = min_num_coins(money-c,coins)
            if num_coins+1 < min_coins:
                min_coins = num_coins+1
    ## END SOLUTION
    # YOUR SOLUTION HERE
    return min_coins

def min_num_coins_dynamic(money,coins):
    min_coins = {0:0} # Base case, no coins needed for no money
    ## BEGIN SOLUTION
    for m in range(1,money):
        min_coins[m] = np.inf
        for c in coins:
            if m >= c:
                if min_coins[m-c] + 1 < min_coins[m]:
                    min_coins[m] = min_coins[m-c] + 1
    ## END SOLUTION
    # YOUR SOLUTION HERE
    return min_coins[m]

import pandas as pd
import numpy as np
def align(s1,s2):
    # Below are the exact base cases that I want you to use
    if len(s1) == 0:
        aligned_s1 = "".join(["-" for i in range(len(s2))])
        return 0,aligned_s1,s2
    if len(s2) == 0: # no way to match
        aligned_s2 = "".join(["-" for i in range(len(s1))])
        return 0,s1,aligned_s2
    
    # You don't have to use my dataframe that helps with the choices, but ... I recommend it
    choices_df = pd.DataFrame({
        "remainder(s1)":[s1[1:],s1[1:],s1],
        "remainder(s2)":[s2[1:],s2,s2[1:]],
        "s1_part":[s1[0],s1[0],"-"],
        "s2_part":[s2[0],"-",s2[0]],
        "score(s1_part,s2_part)":[int(s1[0]==s2[0]),0,0]})
    max_score = -np.inf
    aligned_s1 = None
    aligned_s2 = None
    for i,choice in choices_df.iterrows():
        # here is how to get these values into base Python
        rem_s1,rem_s2,s1_part,s2_part,score = choice.values
        # YOUR SOLUTION HERE
        # print(rem_s1,rem_s2)
        ## BEGIN SOLUTION
        new_score,new_aligned_s1,new_aligned_s2 = align(rem_s1,rem_s2)
        if new_score + score > max_score:
            max_score = new_score + score
            aligned_s1 = s1_part + new_aligned_s1
            aligned_s2 = s2_part + new_aligned_s2
        ## END SOLUTION
    return max_score,aligned_s1,aligned_s2

def align_dynamic(s1,s2):
    scores = pd.DataFrame(index=["-"]+[s1[:i+1] for i in range(len(s1))],columns=["-"]+[s2[:i+1] for i in range(len(s2))])
    for s2_part in scores.columns:
        scores.loc["-",s2_part] = 0
    for s1_part in scores.index:
        scores.loc[s1_part,"-"] = 0
    
    nrows,ncols = scores.shape
    for i in range(1,nrows):
        for j in range(1,ncols):
            # What are our three options
            opt1_s1 = scores.index[i-1] # remember the rows are representative of s1
            opt1_s2 = scores.columns[j-1] # remember the columns are representative of s2
            score_opt1 = -np.inf # FIX THIS!
            ## BEGIN SOLUTION
            score_opt1 = scores.loc[opt1_s1,opt1_s2] + int(scores.index[i][-1]==scores.columns[j][-1])
            ## END SOLUTION
            
            opt2_s1 = scores.index[i-1]
            opt2_s2 = scores.columns[j]
            score_opt2 = -np.inf # FIT THIS!
            ## BEGIN SOLUTION
            score_opt2 = scores.loc[opt2_s1,opt2_s2]
            ## END SOLUTION
            
            opt3_s1 = scores.index[i]
            opt3_s2 = scores.columns[j-1]
            score_opt3 = -np.inf # FIT THIS!
            ## BEGIN SOLUTION
            score_opt2 = scores.loc[opt3_s1,opt3_s2]
            ## END SOLUTION
            
            scores.loc[scores.index[i],scores.columns[j]] = max(score_opt1,score_opt2,score_opt3)
            
    return scores.loc[s1,s2]

def align_dynamic2(s1,s2,verbose=False):
    scores = pd.DataFrame(index=["-"]+[s1[:i+1] for i in range(len(s1))],columns=["-"]+[s2[:i+1] for i in range(len(s2))])
    aligned = pd.DataFrame(index=["-"]+[s1[:i+1] for i in range(len(s1))],columns=["-"]+[s2[:i+1] for i in range(len(s2))])
    for s2_part in scores.columns:
        scores.loc["-",s2_part] = 0
        if s2_part == "-":
            aligned.loc["-","-"] = ("","")
        else:
            aligned.loc["-",s2_part] = ("".join(["-" for i in range(len(s2_part))]),s2_part)
    for s1_part in scores.index:
        scores.loc[s1_part,"-"] = 0
        if s1_part == "-":
            aligned.loc["-","-"] = ("","")
        else:
            aligned.loc[s1_part,"-"] = (s1_part,"".join(["-" for i in range(len(s1_part))]))
    if verbose:
        display(aligned)
    
    nrows,ncols = scores.shape
    for i in range(1,nrows):
        for j in range(1,ncols):
            # What are our three options
            opt1_s1 = scores.index[i-1] # remember the rows are representative of s1
            opt1_s2 = scores.columns[j-1] # remember the columns are representative of s2
            score_opt1 = -np.inf # FIX THIS!
            s1_aligned_opt1 = "" # FIX THIS!
            s2_aligned_opt1 = "" # FIX THIS!
            ## BEGIN SOLUTION
            score_opt1 = scores.loc[opt1_s1,opt1_s2] + int(scores.index[i][-1]==scores.columns[j][-1])
            s1_aligned_opt1 = aligned.loc[opt1_s1,opt1_s2][0] + scores.index[i][-1]
            s2_aligned_opt1 = aligned.loc[opt1_s1,opt1_s2][1] + scores.columns[j][-1]
            ## END SOLUTION
            
            opt2_s1 = scores.index[i-1]
            opt2_s2 = scores.columns[j]
            score_opt2 = -np.inf # FIT THIS!
            s1_aligned_opt2 = "" # FIX THIS!
            s2_aligned_opt2 = "" # FIX THIS!
            ## BEGIN SOLUTION
            score_opt2 = scores.loc[opt2_s1,opt2_s2]
            s1_aligned_opt2 = aligned.loc[opt2_s1,opt2_s2][0] + scores.index[i][-1]
            s2_aligned_opt2 = aligned.loc[opt2_s1,opt2_s2][1] + "-"
            ## END SOLUTION
            
            opt3_s1 = scores.index[i]
            opt3_s2 = scores.columns[j-1]
            score_opt3 = -np.inf # FIT THIS!
            s1_aligned_opt3 = "" # FIX THIS!
            s2_aligned_opt3 = "" # FIX THIS!
            ## BEGIN SOLUTION
            score_opt3 = scores.loc[opt3_s1,opt3_s2]
            s1_aligned_opt3 = aligned.loc[opt3_s1,opt3_s2][0] + "-"
            s2_aligned_opt3 = aligned.loc[opt3_s1,opt3_s2][1] + scores.columns[j][-1]
            ## END SOLUTION
            
            scores.loc[scores.index[i],scores.columns[j]] = max(score_opt1,score_opt2,score_opt3)
            if max(score_opt1,score_opt2,score_opt3) == score_opt1:
                aligned.loc[scores.index[i],scores.columns[j]] = (s1_aligned_opt1,s2_aligned_opt1)
            elif max(score_opt1,score_opt2,score_opt3) == score_opt2:
                aligned.loc[scores.index[i],scores.columns[j]] = (s1_aligned_opt2,s2_aligned_opt2)
            else:
                aligned.loc[scores.index[i],scores.columns[j]] = (s1_aligned_opt3,s2_aligned_opt3)
    if verbose:
        display(scores)
        display(aligned)
    return scores.loc[s1,s2],aligned.loc[s1,s2][0],aligned.loc[s1,s2][1]