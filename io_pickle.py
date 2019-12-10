import pickle

shoplistfile = 'shoplist.data'

shoplist = ['apple', 'mango', 'carrot']

f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)
f.close()

del shoplist

# print('shoplist:{} '.format(shoplist))
# print(shoplist)

f = open(shoplistfile, 'rb')
storedList = pickle.load(f)
print('list : {}'.format(storedList))
print('list: ', storedList)
