#Marks
marks=int(input("Enter your marks: "))
print("Marks: ",marks,end=" ( ")
if marks>=90:
    print('Distinction )')
elif marks>=80:
    print('Very Good )')
elif marks>=70:
    print('Good )')   
elif marks>=60:
    print('Average )')
else:
    print('Failed )')
print("\n")

#Days

day=int(input("Enter day(1-7): "))
print("Its's",end=" ")
if day==1:
    print("Monday")
elif day==2:
    print("Tuesday")
elif day==3:
    print("Wednesday")
elif day==4:
    print("thursday")
elif day==5:
    print("Friday")
elif day==6:
    print("Saturday")
elif day==7:
    print("Sunday")
else:
    print("Invalid day number!")
print("\n")

#temprature
temp=int(input("Enter temperature in Celsius: "))

if temp<0:
    print("It's a cold day")
elif temp>=0 and temp<10:
    print("It's cold!")
elif temp>=10 and temp<20:
    print("It's Cool")
elif temp>=20 and temp<30:
    print("It's warm")
else:
    print("It's hot")
print("\n")
    
#Age
age=int(input("Enter Your age: "))
print("You are a ",end=" ")
if age<=12:
    print("child")
elif age>12 and age<=19:
    print("teenager")
elif age>19 and age<=35:
    print("adult")
elif age>35 and age<=60:
    print("middle aged")
else:
    print("senior citizen")   
print("\n") 

# 3 largest
a=int(input("Enter First Number: "))
b=int (input("Enter Second Number:"))
c=int(input("Enter Third Number: "))

if a>=b:
    if a>=c:
        print(f"{a} is the largest Number")
    else:
        print(f"{c} is the largest Number")
else:
    if b>=c:
        print(f"{b} is largest Number")
    else:
        print(f"{c} is the Largest Number")
print("\n")

#turnory operator
age=78

valid="yes" if age>=18 else "no"
print(f"Is age valid for voting? {valid}")
print("\n")

#multiple turnory operator
valide="yes" if age>=18 else "May be" if age>=16 else "no"
print(f"Is age valid for voting? {valide}")
print("\n")

#result Count
math=int(input("Enter Math Marks: "))
english=int(input("Enter English Marks: "))
science=int(input("Enter Science Marks: "))

if math>=60:
    if english>=60:
        if science>=60:
            print("You have passed in all subjects.")
        else:
            print("You have failed in science.")
    else:
        print("You have failed in english")
else:
    print("You have failed in math")

result="pass" if math>=60 and english>=60 and science>=60 else "Fail"
print(f"You have {result}ed in the exam")

print("\n")

#discount
amount=float(input("Enter the amount: "))
if amount>=5000:
    discount=amount*0.20
    print(f"You have get 20% discount: {discount}")
elif amount>=2000:
    discount=amount*0.10
    print(f"You have get 10% discount:{discount}")
elif amount>=1000:
    discount=amount*0.05
    print(f"You have get 5% discount: {discount}")
else:
    discount=0
    print("You have no discount")
    
final=amount-discount
print(f"Final amount to be paid:{final}")

print("\n")

#nested if else to classify a number as positive, negative or zero and further chaeck if it's even or odd
num=int(input("ENter a Number: "))

if num>0:
    if num%2==0:
        print(f"{num} is positive even")
    else:
        print(f"{num} is positive odd")
elif num<0:
    if num%2==0:
        print(f"{num} is negative even")
    else:
        print(f"{num} is negative odd")
else:
    print(f"{num} is zero")
print("\n")
    
    
#macimum of four numbers
a=int(input("Enter First Number: "))
b=int(input("Enter second Number: "))
c=int(input("Enter Third Number: "))
d=int(input("Enter Fourth Number: "))

if a>=b and a>=c and a>=d:
    print(f"{a} is the largest Number")
elif b>=a and b>=c and b>=d:
    print(f"{b} is the largest Number")
elif c>=a and c>=b and c>=d:
    print(f"{c} is the largest Number")
elif d>=a and d>=b and d>=c:
    print(f"{d} is the largest Number")
elif a==b and a==c and a==d:
    print("All numbers are equal")
print("End of program")
print("\n")