d={"tom":7334567867,"rob":1234567890,"joe":9876543210}
print(d)
d["eswar"]=2345678909
print(d)
del d['tom']
print(d)

for key in d:
    print("Key:",key," value:",d[key])

for k,v in d.items():
    print("key:",k," value:",v)

d.clear()  
d
