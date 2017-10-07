numbers = []
for number in range(1,1000):
    if number%3 ==0 or if number%5 ==0:
        numbers.append(number)
    else:
        continue
print(sum(numbers))
