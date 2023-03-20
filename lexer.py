# Import libraries.
from utils import Utils

# Initialize the utils.
utils = Utils("example/simple.vc")

# get value at state 12 key "C"
# print(data[map_state["0"]][map_key["c"]])
# The .get() method returns an Option<&V>

print(utils.source_code)