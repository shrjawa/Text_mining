# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 15:20:56 2020

@author: cipher
"""
from operator import itemgetter
import os, json
import pandas as pd
import numpy as np
import sklearn 
import time

path_to_json = 'D:/covid-19/biorxiv_medrxiv/biorxiv_medrxiv'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
# print(json_files)
json_text=[]
ind=0
Key_list=["text","title"]

#This part below creates file with paper_id as name
# for index, js in enumerate(json_files):
#     with open(os.path.join(path_to_json, js)) as json_file:
#         print(json_file)
#         res=[]
#         # with open("%s.json" %json_file, "r") as outfile:  #at the moment a mistake btgood to know+
#         json_file=json.load(json_file)
#         for key1,values1 in json_file.items():
#             if key1=="paper_id":
#                 open("%s.txt"%values1,'w')
 #end

def list_extract(lst):
    # if len(lst)!=0:
    d = {}
    print(len(lst))
    try:    
        key, value = lst[1].keys(),lst[1].values()
        for ke1,val in zip(key,value):
            d.update({ke1:val})
    except IndexError:
        key, value = lst[0].keys(),lst[0].values()
        for ke1,val in zip(key,value):
            d.update({ke1:val})        

    # else:
    #     d=[]
    #output.append(key)
    
    return d



       
for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js)) as json_file:
        #print(json_file)
        res=[]
        # with open("%s.json" %json_file, "r") as outfile:  #at the moment a mistake btgood to know+
        json_file=json.load(json_file)
        for key1,values1 in json_file.items():
            res.append(key1)
            #print(key1)
            valu=[]
            if key1=="paper_id":
                F=open("%s.txt"%values1,'w+',encoding="utf-8")#creates file with paper id name
                #F.write('{')
            res1=[]
            try:
                lisst=list(json_file[key1].keys())   
                if(len(lisst)!=0):
                    for i in range(len(lisst)):
                        if lisst[i] in Key_list:
                            try:
                                val1=json_file[key1][lisst[i]]
                            except TypeError:
                                val1=[]
                                for iij in len(json_file[key1]):
                                    val1.append(json_file[key1][iij])
                            #dict=str(lisst[i]:val1)
                            F.write(str(lisst[i])+':'+str([val1])+',')
                        #for key2,value2 in json_file[key1][lisst[i]].items():
                        try:
                            list_2=list(json_file[key1][lisst[i]].keys())
                        except:
                            list_2=[]
                        if(list_2!=[]):
                            for j in range(len(list_2)):
                                if list_2[j] in Key_list:
                                    val2=json_file[key1][lisst[i]][list_2[j]]
                                    F.write(str(list_2[j])+':'+str([val2])+',')
                                try:
                                    list_3=list(json_file[key1][lisst[i]][list_2[j]].keys())
                                except:
                                    list_3=[]
                                if(list_3!=[]):
                                    for k in range(len(list_3)):
                                        if list_3[k] in Key_list:
                                            val3=json_file[key1][lisst[i]][list_2[j]][list_3[k]]
                                            F.write(str(list_3[k])+':'+str([val3])+',')
            except AttributeError:
                if (type(json_file[key1])==list) is True:
                    if len(json_file[key1])!=0:
                    #print(json_file[key1])
                        lisst=list_extract(json_file[key1])
                
                    print(lisst)

            # if(key1=="abstract"): to catch missing data
            #     print(lisst)
                    if(len(lisst)!=0):
                        #print(lisst)
                        for i in range(len(lisst)):
                            try:
                                lisst_keys=list(lisst.keys())
                                try:
                                   val1=json_file[key1][lisst_keys[i]] 
                                   F.write(str(lisst[i])+':'+str([val1])+',')
                                except TypeError:
                                    if lisst_keys[i] in Key_list:
                                        
                                        for iij in range(len(json_file[key1])):
                                            val1=json_file[key1][iij]
                                    #dict=str(lisst[i]:val1)
                                            F.write(str(lisst_keys[i])+':'+str([val1])+',')
                                #for key2,value2 in json_file[key1][lisst[i]].items():
                                try:
                                    list_2=list(json_file[key1][lisst[i]].keys())
                                except:
                                    list_2=[]
                                if(list_2!=[]):
                                    for j in range(len(list_2)):
                                        if list_2[j] in Key_list:
                                            val2=json_file[key1][lisst[i]][list_2[j]]
                                            F.write(str(list_2[j])+':'+str([val2])+',')
                                        try:
                                            list_3=list(json_file[key1][lisst[i]][list_2[j]].keys())
                                        except:
                                            list_3=[]
                                        if(list_3!=[]):
                                            for k in range(len(list_3)):
                                                if list_3[k] in Key_list:
                                                    val3=json_file[key1][lisst[i]][list_2[j]][list_3[k]]
                                                    F.write(str(list_3[k])+':'+str([val3])+',')
                            except AttributeError:
                                pass
                else:
                    lisst=[]            
        time.sleep(100)    #F.write('}')
        
        
F.close()

# for index, js in enumerate(json_files):
#     with open(os.path.join('D:/covid-19/biorxiv_medrxiv/biorxiv_medrxiv', js)) as json_file:
#         json_text.append(json.load(json_file))
    

# np_json_text=np.array(json_text) 
# print(np_json_text.shape)
# res=[]
# res1=[]
# for i in range(len(json_text)):
#     for key in json_text[i].keys():
#         res.append(key)
#         for j in range(len(res[i])):
#             try:
#                 lisst=json_text[i][res[j]].keys()    
#             except:
#                 lisst=[]
#             if(lisst!=[]):
#                 for k in lisst:
#                     res1.append(k)
                
    