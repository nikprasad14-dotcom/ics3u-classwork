# Create a loop that will add the numbers from 5 to 20 but not any multiples of 3. Use modulus.
total = 0
number = 4
while number < 20:
    number +=1
    if number % 3 == 0:
        continue
    total += number
print(total)