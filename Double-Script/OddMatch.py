def double_set_times(start_num, target, times):
    steps = [start_num]  # Store the sequence

    # Ensure the starting number is odd
    if start_num % 2 == 0:
        print("Error: Start number must be odd.")
        return
    
    # Double the number a set number of times
    for _ in range(times):
        start_num *= 2
        steps.append(start_num)

        # Stop if the number is within the matching range
        if start_num in {target, target - 1, target + 1}:
            break

    # Print the steps in reverse order
    for step in reversed(steps):
        print(step)

    # Indicate if the final number is a match
    if start_num == target:
        print(f"{start_num} match")
    elif start_num == target + 1:
        print(f"{start_num} match (1 above)")
    elif start_num == target - 1:
        print(f"{start_num} match (1 below)")
    else:
        print(f"{start_num} (no match)")


# Get user input
start_num = int(input("Enter an odd starting number: "))
target = int(input("Enter the target number: "))
times = int(input("Enter the number of times to double: "))

double_set_times(start_num, target, times)
