import pickle

my_list = ['zero', 'first', 'second', 'three', 'four']

pickle_file = open('test.pkl', 'wb')
pickle.dump(my_list, pickle_file)
pickle_file.close()

pickle_file = open('test.pkl', 'rb')
pickle_content = pickle.load(pickle_file)
print(pickle_content)
for each in pickle_content:
    print(each)

