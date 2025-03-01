# l1=[1,2,3,4]
# l2=[5,6,7,8,]
# l1.extend(l2)
# print("new list=",l1)

# l1.insert(4,5)
# print("new list=",l1)

# l1.remove(1)
# print("new list=",l1)

# l2.pop(2)
# print("new list=",l2)
 
l1=[]
t1=()

for i in range(5):
    ele=int(input("Enter number: "))
    l1.append(ele)
    t1+=(ele,)

    print("new list=",l1)
    print("new tuple=",t1)















