# a = [6,8,1,3,0,5]
# [6,8,1,3,0,5] 6>8
# [6,1,8,3,0,5] 8>1
# [6,1,3,8,0,5] 8>3
# [6,1,3,8,0,5] 8>0
# [6,1,3,0,5,8] 8>5

# [1,6,3,0,5,8] 6>1
# [1,3,6,0,5,8] 6>3
# [1,3,0,6,5,8] 6>0
# [1,3,0,5,6,8] 6>5
# [1,3,0,5,6,8] 6>8

# [1,3,0,5,6,8] 1>3
# [1,0,3,5,6,8] 3>0
# [1,0,3,5,6,8] 3>5
# [1,0,3,5,6,8] 5>6
# [1,0,3,5,6,8] 6>8

# [0,1,3,5,6,8] 1>0
# [0,1,3,5,6,8] 1>3
# [0,1,3,5,6,8] 3>5
# [0,1,3,5,6,8] 5>6
# [0,1,3,5,6,8] 6>8

# the worst case list would be a list in descending order. 
# Swapping
# temp = a
# a  = b
# b = temp

# Algorithm

# For the first iteration, compare all the elements (n). For the subsequent runs, compare (n-1) (n-2) and so on.
# Compare each element with its right side neighbor.
# Swap the smallest element to the left.
# Keep repeating steps 1-3 until the whole list is covered.

def bubble_sort(a):
  #Setting the range for comparison (first round: n, second round: n-1  and so on)
  for i in range(len(a)-1,0,-1):
    #Comparing within set range
    for j in range(i):
      #Comparing element with its right side neighbor
      if a[j] > a[j+1]:
        # Swapping
        temp = a[j]
        a[j]=a[j+1]
        a[j+1]=temp
   return a
   
bubble_sort([6,8,1,3,0,5])

# O(n^2)
