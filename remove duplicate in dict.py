a={'gfg':10,'is':15,'best':20,'for':10}
print("the original dictionary is :" +str(a))
temp={val: key for key , val in a.items()}
res={val: key for key, val in temp.items()}
print("the dictionary after values removal:" +str(res))















