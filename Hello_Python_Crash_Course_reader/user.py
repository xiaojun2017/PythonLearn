user_0 = {
    'username': "efermi",
    'first': "enrico",
    'last': 'fermi'
}

for key, value in user_0.items():
    print("key:" + key + "  value:" + value)

for k in user_0.keys():
    print("k:" + k.title() + " v:" + user_0[k].title())

for v in user_0.values():
    print("v:" + v.title())
