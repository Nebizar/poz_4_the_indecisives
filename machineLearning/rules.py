# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 20:21:17 2019

@author: apasi
"""

import csv
from apyori import apriori

def read_data():
    with open('shopping-data.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        output = list(reader)
    
        readFile.close()
    #print(type(output))    
    return output

def compute_rules(transactions):
    rules = apriori(transactions, min_support = round((len(transactions)**(1/1024)) - 1 , 3),
                    min_confidence = .2, min_lift = 3, min_length = 2)
    results = list(rules)
    return results

def add_new_data(new_data):
    with open('shopping-data.csv', 'a', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_data)
        
    csvFile.close()
    
def create_rules():
    data = read_data()
    rules = compute_rules(data)
    #print(type(rules))
    results_list = []
    for i in range(0, len(rules)):
        results_list.append(list(rules[i][0]))
    return results_list

