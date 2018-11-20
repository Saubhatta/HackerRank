input()

arr = str(input()).split(" ")
arr.reverse()

for num in arr:
    print(num + " ", end="")

'''
# Reversing a list using slicing technique
def Reverse(arr):
  new_lst = arr[::-1]
  return new_lst

#input()

arr = str(input()).split(" ")
#arr =  [1, 2, 7, 4, 5]

#print (Reverse(arr), end="")
for num in Reverse(arr):
  print (num + " ", end="")
'''