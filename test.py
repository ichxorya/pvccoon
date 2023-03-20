from utils import Utils

utils = Utils("example/simple.vc")

n_i = utils.get_next_state("0", "i")
print(n_i)
n_in = utils.get_next_state(n_i, "n")
print(n_in)
n_int = utils.get_next_state(n_in, "t")
print(n_int)
n_int_space = utils.get_next_state(n_int, " ")
print(n_int_space)
n_int_space_i = utils.get_next_state(n_int_space, "i") # Key Error
print(n_int_space_i)
n_int_space_i_space = utils.get_next_state(n_int_space_i, " ")
print(n_int_space_i_space)
n_int_space_i_space_assign = utils.get_next_state(n_int_space_i_space, "=")
print(n_int_space_i_space_assign)
n_int_space_i_space_assign_space = utils.get_next_state(n_int_space_i_space_assign, " ")
print(n_int_space_i_space_assign_space)
n_int_space_i_space_assign_space_1 = utils.get_next_state(n_int_space_i_space_assign_space, "1")
print(n_int_space_i_space_assign_space_1)