num=int(input ("Enter the number:  "))
answer = 1
count = 0
for count in range(num,1,-1):
    answer = answer * count
print (answer, " is factorial of ", num)
