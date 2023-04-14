# Median of Three Values
# Write a function that takes three numbers as parameters, and returns the median value of those parameters 
# as its result. Include a main program that reads three values from the user and displays their median. 

def median():
    myList = [];
    num1 = float(input("Input your first number: "));
    myList.append(num1);
    num2 = float(input("Input your second number: "));
    myList.append(num2);
    num3 = float(input("Input your third number: "));
    myList.append(num3);
    myList.sort();
    print(f"The median value of {num1}, {num2}, {num3} is: " + str(myList[1]));

median();

# th nhập lỗi

# # Cách khác
# def median(num1, num2, num3):
#     median_num = sorted([num1, num2, num3])[1]
#     return median_num

# def result():
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
#     num3 = float(input("Enter the third number: "))

#     median_num = median(num1, num2, num3)

#     print(f"The median of {num1} , {num2} , {num3} is {median_num}")

# result();