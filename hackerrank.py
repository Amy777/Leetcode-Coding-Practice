def pq():
  q = []
  arr = [(100,"red"),(-4,"blue"),(10,"green")]
  arr2 = [11,2,3]
  
  for i in arr:
    heapq.heappush(q,i)
  print((100,"red") in q)
  s = heapq.heappop(q)
  print (heapq.heapreplace([500,"blue"], [s]))
  #heapq.heapreplace([1000],q)
  N =5 
  col=["red","green","blue","red","white"]

  hp = []
  res=0
  for i in range(N) :
    if len(hp)>3:
      temp = heapq.heappop(hp)
      res += temp[0]
      heapq.heappush(hp,(1000,col[i]))
    else:
      for j in hp:
        if(j[1]==col[i]):
          print("yes")
      else: #add this color
        heapq.heappush(hp,(1000,col[i]))