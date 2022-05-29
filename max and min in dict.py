a={'x':500,'y':6768,'z':355}
max=max(a.keys(),key=(lambda k:a[k]))
min=min(a.keys(),key=(lambda k:a[k]))
print('maxvalue:',a[max])
print('minvalue:',a[min])
