# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 21:43:37 2019

@author: Krzysztof Pasiewicz
"""
categories_dict = {
        "myszki": "4575",
        "klawiatury": "4566",
        "zestaw klawiatura i mysz": "9189",
        "pady": "4569",
        "piloty": "16641",
        "joysticki": "4565",
        "tablety graficzne": "4570",
        "monitory": "260041",
        "dyski zewnetrzne i przenosne": "77939",
        "pendrive": "257960",
        "sledzie": "4739",
        "kamery internetowe": "260021",
        "zestawy i kamery do wideokonferencji": "260023",
        "gogle VR": "260043",
        "mikrofony i sluchawki": "259422",
        "glosniki": "259434"
        }

def get_items_from_json():
    import ast

    with open('dane.json','r', encoding="utf8") as json_file:
        s = json_file.read()
        s = s.replace("\'", "\"")
        data = ast.literal_eval(s)
    
    json_file.close()
    items = data["items"]
    all_items = items["promoted"] + items["regular"]
    
    return all_items


def get_items_from_api(data):
    items = data["items"]
    all_items = items["promoted"] + items["regular"]
    return all_items
