%keep the csv containing the attribute values in same directory

name = 'tenfeature_averageVal.csv'
M = csvread(name,0,1)
idx = kmeans(M,3)
