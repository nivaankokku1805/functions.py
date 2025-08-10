def well_wishes():
    print("Hello") #} def - used to define function
    print("How are you ?")
    
well_wishes() # well_wishes() - calling the function     

#activity 2 - weather condition
def weather_condition():
    print("The weather is pleasant in:", spring)
    print("The weather is same in:", autumn)
    
spring = " spring - full of nature"
autumn = " autumn - full of dry leaves"    
weather_condition()

#activity 3 - calculator

def add(P , Q):
    # This function is used for adding two numbers
    return P + Q
def subtract(P , Q):
    # This function is used substracting two numbers
    return P - Q
def multiply(P,Q):
    #This function is used for multiplying two numbers
    return P * Q
def divide(P,Q):
    #This function is used for dividing tho numbers
    return P / Q

# Now we will take input from the user
print("Please select the operation.")
print("a. Add")
print("b. Substract")
print("c. Multiply")
print("a. Divide ")

choise = input("Please enter choise (a/b/c/d): ")

num_1 = int(input("Please enter the first number:"))
num_2 = int(input("Please enter the second number:"))

if choise == 'a':
    print(num_1, "+", num_2 ,"=", add(num_1,num_2))
    
elif choise == 'b':
    print(num_1, "-", num_2 ,"=", subtract(num_1,num_2))  

elif choise == 'c':
    print(num_1, "*", num_2 ,"=", multiply(num_1,num_2))   
    
elif choise == 'd':
    print(num_1, "/", num_2 ,"=", divide(num_1,num_2))    
    
else:
    print("This is an invalid input")       
 




