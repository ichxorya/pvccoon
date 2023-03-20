#Example and pseudo code. Not comfirm of working, only for reference and describe

#hashmap for csv table reading

import csv

data = list(csv.reader(open('test_data.csv')))

emptyDict = {}

#map create
map_state = {}    #map for stete (row) 
map_key = {}      #map for key (column)

#insert to map_state
for i in range(len(data)):              #len(table) = number of row && table format is 1...n as csv not 0.
    map_state[data[i][0]] = i

#insert to map_key
for i in range(len(data[0])):          #len(table[1]) = number of column && table format is 1...n as csv not 0,,n
    map_key[data[0][i]] = i

#get value at state 21 key "C"    
print( data[ map_state['0']][map_key['+']] )
#The .get() method returns an Option<&V> 