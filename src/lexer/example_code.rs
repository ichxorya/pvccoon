//Example and pseudo code. Not comfirm of working, only for reference and describe

//hashmap for csv table reading

use std::collections::HashMap;

...
    // map create
    let mut map_state = HashMap::new();     //map for stete (row) 
    let mut map_key = HashMap::new();       //map for key (column)

    //insert to map_state
    for i in len(table) {      // len(table) = number of row && table format is 1...n as csv not 0,,n
        map_state.insert(table[1][i].to_string(), i)
    }

    //insert to map_key
    for i in len(table[1]) {      // len(table[1]) = number of column && table format is 1...n as csv not 0,,n
        map_key.insert(table[1][i].to_string(), i)
    }

    //get value at state 21 key "C"    
        tableơ[  map_state.get("21").copied().unwrap_or(0)  ][  map_key.get("C").copied().unwrap_or(0)  ]
        //The .get() method returns an Option<&V> 