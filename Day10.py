n = int(input())
a = []
while (n > 0):
  digit = n % 2
  a.append(digit)
  n = n // 2

a.reverse()

longest = 0
current = 0


for i in a:
  if i == 1:
    current += 1
  else:
    longest = max(longest, current)
    current = 0

print (max(longest, current))