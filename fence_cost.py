# Author: Caleb
# Date: 7/11/2025
# Version 1

# Calculate the cost of fencing using data given

'''width = float(input("Width: "))
length = float(input("Length: "))
cost_meter = float(input("Cost per meter: "))

perimeter = 2 * (width + length)
ovrl_cost = perimeter * cost_meter

print(f"\nThe perimeter is {perimeter}m")
print(f"The cost is ${ovrl_cost}. \nHave a nice day")'''

# Code creates error message when use inputs incorrect number (v2)

'''def fen_len_cos(question, min): # Create function
    error = "Whoops, that's not a number above 0!"

    while True:
        try:
            response = float(input(question))
            # If response is above 0...
            if min < response:
                break # ...stop the loop

            else:
                print(f"{error}")

        except ValueError:
            print(f"{error}")
    return response # This makes the response available to be used

width = fen_len_cos("Enter the width of your fence: ",0)
length = fen_len_cos("Enter the length of your fence: ",0)
cost_meter = fen_len_cos("Enter the cost of your fence /m: ",0)

perimeter = 2 * (width + length)
ovrl_cost = perimeter * cost_meter

print(f"\nThe perimeter is {perimeter}m")
print(f"The cost of your fencing is ${ovrl_cost}. \nHave a nice day!")'''

# Allows code to loop so that user can use it multiple times (v3)

def fen_len_cos(question, min): # Create function
    error = "Whoops, that's not a number above 0!"

    while True:
        try:
            response = float(input(question))
            # If response is above 0...
            if min < response:
                break # ...stop the loop

            else:
                print(f"{error}")

        except ValueError:
            print(f"{error}")
    return response # This makes the response available to be used

keep_going = ""
while keep_going == "": # Allows section of program to loop when required

    width = fen_len_cos("Enter the width of your fence: ",0)
    length = fen_len_cos("Enter the length of your fence: ",0)
    cost_meter = fen_len_cos("Enter the cost of your fence /m: ",0)

    perimeter = 2 * (width + length)
    ovrl_cost = perimeter * cost_meter

    # Displays perimeter and cost
    print(f"\nThe perimeter is {perimeter}m")
    print(f"The cost of your fencing is ${ovrl_cost}.")

    # Loops the code or stops it entirely
    keep_going = input("\nPress <ENTER> to do the calculator again, or any other key to quit. ")

print(f"\nHave a nice day!")