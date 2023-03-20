import csv

# import transition_table
data = list(csv.reader(open('transition_table.dat')))

#map create
map_state = {}    # map for stete (row) 
map_key = {}      # map for key (column)

# insert to map_state
for i in range(len(data)):             # len(table) = number of row && table format is 1...n as csv not 0.
    map_state[data[i][0]] = i

# insert to map_key
for i in range(len(data[0])):          # len(table[1]) = number of column && table format is 1...n as csv not 0,,n
    map_key[data[0][i]] = i

# get value at state 0 key "+"    
print( data[ map_state['0']][map_key['+']] )

# aAccess data guide: data[ map_state['0']][map_key['+']] 
# State is string (very stupid but can ez change to int)
# key is string