a: str = '0000000000'
for i in range(1, 6, 1):
    print(i, a)

i = 0
k = 0
while i < 10:
    inp_number = input("input number character  ")
    if inp_number.isdigit():
        inp_number = int(inp_number)
        i = i+1
        if(inp_number == 5):
            k = k+1
    else:
        print("It is not number")
        continue
print("the number 5 appeared ",k," times")

sum = 0
for i in range(1,101):
    sum +=i
print(sum)

product = 1
for i in range(1,11):
    product *=i
print(product)

int_num = 123456
while int_num > 0:
    print(int_num % 10)
    int_num = int_num//10

int_num = 123456
sum = 0
while int_num > 0:
    sum += int_num % 10
    int_num = int_num//10
print(sum)

int_num = 123456
prod = 1
while int_num > 0:
    prod *= int_num % 10
    int_num = int_num//10
print(prod)

int_num = 123467
while int_num > 0:
    if(int_num % 10 == 5):
        print("the number 5 appeared ")
        break
    else:
        int_num = int_num//10
        if(int_num <=0):
            print("the number 5 did not appear ")

int_num = 1239467
max = 0
while int_num > 0:
    numb = int_num % 10
    if(numb>max):
        max = numb
    else:
        int_num = int_num//10
print("the max number is ",max)

int_num = 1259467
num_of5 = 0
while int_num > 0:
    numb = int_num % 10
    if(numb == 5):
        num_of5 += 1
    int_num = int_num//10
print("number of 5 is ", num_of5)

