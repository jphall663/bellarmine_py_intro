@profile
def biglist():
 list_ = []
 for i in range(0, 1000000):
  list_.append(i)
 return list_
biglist()