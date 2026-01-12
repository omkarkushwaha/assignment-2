#   Task 1
number=int(input("Enter a number: "))
if number%2==0:
    print(f'{number} is an even number.')
else:
    print(f'{number} is an odd number.')
    
    
#    Task 2

sum=0
for i in range(51):
    sum+=i
print(f'The sum of numbers from 1 to 50 is: {sum}')