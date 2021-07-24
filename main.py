import random
import calculator

rand_list = []


for i in range(20):
    number1 = random.randint(0, 100)
    rand_list.append(number1)

num1 = random.choice(rand_list)
num2 = random.choice(rand_list)
num_of_user = int(input())
sum_list = []

for i in range(num_of_user):
    num = random.choice(rand_list)
    sum_list.append(num)

print(sum_list)
sub = calculator.Substraction()
add = calculator.Addition()
div = calculator.Div()
mul = calculator.Mult()
sub = sub.sub(num1, num2)
div = div.div(num1, num2)
mul = mul.mult(num1, num2)

add = add.add(sum(sum_list))
print(add)
print(sub)
print(div)
print(mul)