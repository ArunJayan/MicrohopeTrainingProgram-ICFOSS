#in this example we discuss hpow we read inputs from keyboard . 
#first we see how we use input() then we will move onto raw_input()

num1 = input("Enter num1 :: ")
#in the above step we read a integer and store it into variable num1
num2 = input("Enter num2 :: ")
#in the above step we read another integer and store it into variable num2
print "%d + %d = %d"%(num1,num2,num1+num2)

#we can do it single step 
print ((input("Enter num1"))+input("Enter num2"))