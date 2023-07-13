def only_floats(a,b):
  if a.is_integer() and b.is_integer():
    return 2
  elif a.is_integer() == False or b.is_integer() == False:
    return 1
  else:
    return 0
  
print(only_floats(22,23))
