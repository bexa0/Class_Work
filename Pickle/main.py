import pickle

# a = [
#     ('strange_one', 'stange_two', 'stange_three'),
#     ('box_one', 'box_two', 'box_three'),
#     ('cage_one', 'cage_two', 'cage_three')
# ]
#
# paper = open('text.bin', 'wb')
# pickle.dump(a,paper)
# paper.close()




# filename = 'student.dat'
#
# name = 'bexa'
# age = 16
#
# with open(filename, 'wb') as file:
#     pickle.dump(name,file)
#     pickle.dump(age, file)
#
# with open(filename, 'rb') as file:
#     name = pickle.load(file)
#     age = pickle.load(file)
#     print('Name: ', name, 'Age: ', age)


import struct
import sys


print(struct.pack('I3c', 123, b'a', b'b', b'c'))
print(struct.unpack("I3c", b'{\x00\x00\x00abc'))

print('Utstep', sys.byteorder)
