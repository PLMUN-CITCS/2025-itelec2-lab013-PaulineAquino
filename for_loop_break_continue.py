# Define a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Iterate over each number using a for loop
for num in numbers:
    # Skip the number 3 using continue
    if num == 3:
        continue  # Skip the rest of this iteration
    
    # If the number is 7, exit the loop using break
    if num == 7:
        break  # Exit the loop completely
    
    # Print the current number
    print(num)
