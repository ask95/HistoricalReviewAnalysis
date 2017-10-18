import json
import multiprocessing

from joblib import Parallel, delayed

import functions as fn

count = 0
j = 1
num_cores = multiprocessing.cpu_count()
while count < 10000:
    with open('/home/meet/sentiment-analysis/json 2/hotel' + str(j) + '.json') as file:
        data = json.load(file)
    if len(data['Reviews'])>=250:
        results = Parallel(n_jobs=num_cores)(delayed(fn.generate_sentiment)(data['Reviews'][i]) for i in range(len(data['Reviews'])))
        with open('/home/meet/sentiment-analysis/output_json/output_hotel_' + str(j) + '.json', 'w') as outfile:
            json.dump(results,outfile)
        count = count + 1
        print "count is now " + str(count)
    j = j + 1
print "final value of j is :" + str(j)