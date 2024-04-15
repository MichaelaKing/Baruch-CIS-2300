"""myString1="Hello"
myString1[0]="P"
print(myString1)"""


"""myString1="INternational"

print(myString1[2:7:2])"""

"""myString="4657382 nmk"

print(myString.isalpha())
print(myString.isdigit())
print(myString.islower())
print(myString.isspace())"""

"""myString = input("Enter yes or no\n")

if myString.lower == "Yes":
    print("Correct")
else:
    print("Not correct")"""
    
    
myString="  program  "
print(len(myString))
s =myString.strip()
print(len(s))
print(s)
print(s.isdigit())
print(s.isalpha())
print(s.islower())
print(s.endswith('ram'))
print(s.startswith('pro'))
print(s.replace("pro",'high'))
print(s)

input_string=input("Enter the Substring you are looking for\n")
if s.find(input_string)==-1:
    

