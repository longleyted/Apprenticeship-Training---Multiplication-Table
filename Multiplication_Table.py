userInput = int(input("Please provide the first number for the multiplication table: "))
x = 0
answer =[]
for x in range (11):
    answer = userInput * x 
    print(x," * ", userInput, " = ",answer)
    x+=1
