# Task(I)
print("!WELCOME TO MSEB ")
n = input("Enter your name:")
u = int(input("Enter your units:"))
def light():
 if u >= 0 and u <= 100:
  return u*3
 elif u >= 101 and u <= 300:
  return u*5
 elif u >= 301 and u <= 500:
  return u*7
 elif u > 501:
  return u*10
 else:
  print("invalid.")
light()
print(f" Hello {n} your total bill of electricity is:", light())

# output=
# WELCOME TO MSEB 
# Enter your name:kk
# Enter your units:200
# Hello kk your total bill of electricity is: 1000

#Task(II)
t1 = [1, 2, 3, 4, 'NITS', 0, 7, 24.00, 'Nashik', 8, 9,]
print(t1)
print(t1[0:10:2])
print(t1[2:10])
print(t1[-3:-10])
print(t1[1:11:3])
print(t1[0:11:1])

# output
# [1, 2, 3, 4, 'NITS', 0, 7, 24.0, 'Nashik', 8, 9]
# [1, 3, 'NITS', 7, 'Nashik']
# [3, 4, 'NITS', 0, 7, 24.0, 'Nashik', 8]
# []
# [2, 'NITS', 24.0, 9]
# [1, 2, 3, 4, 'NITS', 0, 7, 24.0, 'Nashik', 8, 9]