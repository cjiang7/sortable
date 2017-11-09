"""
" Sortable Chanllenge
" The code is based on Python 2.7.10
"""

import json
from collections import OrderedDict

list_dic = {}

with open("listings.txt") as f:
  list_data_file = f.readlines();

for line in list_data_file:
    list_data = json.loads(line, object_pairs_hook=OrderedDict)
    manufacturer = list_data["manufacturer"].lower()
    if manufacturer in list_dic:
       list_dic[manufacturer].append(list_data)
    else:
       manu_product = [list_data]
       list_dic[manufacturer] = manu_product

with open("products.txt") as f:
  product_data_file = f.readlines()

result_dic = {}
for line in product_data_file:
    product_data = json.loads(line)
    product_name = product_data["product_name"].lower()
    manufacturer = product_data["manufacturer"].lower()
    if manufacturer in list_dic:
       model = product_data["model"].lower()
       family = ""
       if "family" in product_data:
          family = product_data["family"].lower()
       for listing in list_dic[manufacturer]:
           if model in listing["title"].lower() and family in listing["title"].lower():
              if product_name not in result_dic:
                 result_list = [listing]
                 result_dic[product_name] = result_list
              else:
                 result_dic[product_name].append(listing)
    else:
       result_list = []
       result_dic[product_name] = result_list

with open('result.txt', 'w') as f:
    for key, value in result_dic.items():
        obj = OrderedDict()
        obj["product_name"] = key
        obj["listings"] = value
        f.write(json.dumps(obj))
        f.write('\n')

