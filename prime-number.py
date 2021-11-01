a=int(input("Enter a number : "))
c=2
x=0
b=int(a**0.5)
while c!=b+1:
  if a%c == 0:
    c = b+1
    x = 1
  else:
    c = c + 1
if x == 1:
    print("It is not a prime number")
else:
    print("It is a prime number")
