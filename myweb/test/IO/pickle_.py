
import pickle

_dict = {'name':'bob','age':21}

with open('pick.txt', 'w') as f:
    pickle.dump(_dict, f)

with open('pick.txt', 'r') as f:
    d = pickle.load(f)
    print d