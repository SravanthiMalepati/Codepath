def shortest_unsorted_array(arr):
  pnt1 = 0
  pnt2 = len(arr)-1
  # start = 0
  # end = len(arr)-1
  while pnt1 < pnt2:
    if arr[pnt1] <= arr[pnt1+1]:
      pnt1 += 1
    else:
      # start = pnt1 #break
      break
  while 0 < pnt2:
    if arr[pnt2] >= arr[pnt2-1]:
      pnt2 -=1
    else:
      break

  min_sub = float('inf') #
  max_sub = -float('inf')
#11, 2, 0, -1 
  for k in range(pnt1,pnt2+1):
    min_sub = min(min_sub,arr[k]) #-1
    max_sub = max(max_sub,arr[k]) #11

  while pnt1 > 0 and arr[pnt1-1] > min_sub:
    pnt1 -= 1 
  while pnt2 < len(arr) - 1 and arr[pnt2+1] < max_sub:
    pnt2 += 1
  
  return pnt2-pnt1+1 


def main():
  arr =[1, 2, 5, 3, 7, 10, 9, 12]
  print(shortest_unsorted_array(arr) == 5)

  arr2=[1, 11, 2, 0, -1, 7, 10] # => 4-1+1 = 4 X ; 7-0+1 = 8 
#       p1           p2  
  [-1,0,1,2,7,10,11]
  print(shortest_unsorted_array(arr2)==7)
  arr3=[2,3,3,2,4]
  print(shortest_unsorted_array(arr3)==3)

main()