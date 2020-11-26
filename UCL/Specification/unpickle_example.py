import pickle

with open('data.pickle', 'rb') as infile:
    # The protocol version used is detected automatically
    list2= pickle.load(infile)

print(list2)