# start=int(input("Enter starting number: "))
# end=int(input("Enter ending number: "))

# for num in range(start, end+1):
#     if num % 2 == 0:
#         print(f"{num} is Even")
#     else:
#         print(f"{num} is Odd")

# #while example
# i=1
# while i<=10:
#     print(i)
#     i+=1

# while True:
#     num=int(input("Enter 3 to exit: "))
#     if num==3:
#         break

# while True:
#     print("Welcome to our caffe")
#     print()
    
#     print("Enter 1 to order coffee")
#     print("Enter 2 to order tea")
#     print("Enter 3 to order juice")
#     print("Enter 0 to exit")
#     print()
    
#     choice=int(input("Please enter your choise : "))
#     print()
    
#     if choice==1:
#         print("You have ordered coffee. Please wait...")
#     elif choice==2:
#         print("You have ordered tea. Please wait...")
#     elif choice==3:
#         print("You have ordered juice. Please wait...")
#     elif choice==0:
#         print("Thank you for visiting our caffe. Goodbye!")
#         break
#     else:
#         print("Invalide choice. Please try again." )
#     print()


# #pattern
for i in range(1,15):
    print("*"*i)

# #revese number    
for i in range(15,1,-1):
    print(i)
    
# #reverse
for i in range(5,0,-1):
    print("*"*i)

# # 1
# # 22
# # 333
# # 4444
# # 5555
# #str pateern
for i in range(1,6):
    print(str(i)*i)
print()
for i in range(5,0,-1):
    print(str(i)*i)
print() 
# #1
# #12
# #123
# #1234
# #12345
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
print()

for i in range(5,0,-1):
for item in range(1,i+1):
    print(item,end="")              
    print()
print()
        
# #patterns
# row=int(input("Enter Number of rows:"))
# for i in range(1,row+1):
#     print(" "*(row-i)+"*"*(2*i-1))

