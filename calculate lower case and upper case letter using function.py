def string_test(s):
     d={"upper":0,"lower":0}
     for c in s:
          if c.isuper():
               d["upper"]+=1
          elif c.islower():
               d["lower"]+=1
          else:
               pass
      print("original string :",s)
      print("no of upper case:",d["upper"])
      print("no of lower case:",d["lower"])
 string_test('the quick brown box')     
