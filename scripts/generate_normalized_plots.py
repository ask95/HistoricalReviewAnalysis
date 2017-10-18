import collections
import json
from os import listdir
from os.path import isfile, join
import csv

import matplotlib.pyplot as plt
from numpy import *

file_list = [f for f in listdir('/Users/anikeshkamath/sentiment-analysis/normalized_polarity') if
             isfile(join('/Users/anikeshkamath/sentiment-analysis/normalized_polarity', f))]
try:
    file_list.remove('.DS_Store')  # .DS_Store can exist some times while using PyCharm.
except:
    pass


with open('/Users/anikeshkamath/sentiment-analysis/results/ten_feature_3clusters.csv', mode='r') as infile:
    reader = csv.reader(infile)
    mydict = dict((rows[0],rows[1]) for rows in reader)


for j in range(len(file_list)):
    with open('/Users/anikeshkamath/sentiment-analysis/normalized_polarity/' + str(file_list[j])) as f:
        data = json.load(f, object_pairs_hook=collections.OrderedDict)
    x_data = data.keys()
    y_data = data.values()
    x_data[:] = [float(x) for x in x_data]
    file_no = 0
    try:
        file_no = int(mydict[str(file_list[j])])
    except:
        pass

    if file_no == 1:
        plt.plot(x_data, y_data, color = 'lightgreen', marker = 'D')
    elif file_no == 2:
        plt.plot(x_data, y_data, color = 'skyblue', marker = 'o')
    elif file_no == 3:
        plt.plot(x_data, y_data, color = 'yellow', marker = '^')
    else:
        plt.plot(x_data, y_data, color = 'black')


plt.xlabel('Normalized Time Range')
plt.ylabel('Normalized Cumulative Polarity Score')
plt.show()
