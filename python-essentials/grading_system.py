while True:  # Loop continues endlessly until break statement is encountered
    marks = int(input())  # Taking input for marks

    # Checking the grade based on the marks
    if marks >= 90 and marks <= 100:
        print("A grade")
    elif marks >= 80 and marks < 90:
        print("B grade")
    elif marks >= 70 and marks < 80:
        print("C grade")
    elif marks >= 60 and marks < 70:
        print("D grade")
    elif marks < 60 and marks >= 0:  # Checking if marks are within valid range
        print("E grade")
    else:
        print("Invalid")  # Marks are out of valid range, end the loop
        break  # Exit the loop when an invalid mark is entered
