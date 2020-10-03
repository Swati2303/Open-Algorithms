'''
find the sum of n natural numbers
'''
def sum(num):    #recursive function
	if num==1:
		return 1
	else:
		return sum(num-1)+num  #function calls itself

num=int(input("Enter the number:"))
'''
To check whether the number inputted is natural number or not
'''
while num<0:
	print("Enter a natural number !")
	num=int(input("Enter the number:"))
'''
function calling
'''	
x=sum(num)
print("Sum of n natural numbers is:",x)