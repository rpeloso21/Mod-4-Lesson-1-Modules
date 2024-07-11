import text_utils as tu

string = input("Please provide the original string:  ")

print(f"Your string in reverse is:  \n{tu.reverse_string(string)}\n")

print(f"Your string in all caps is: \n{tu.capitalize_string(string)}\n")

print(f"Your string in all lowercase is: \n{tu.lowercase_string(string)}\n")

print(f"The number of characters in your string is:  {tu.count_string(string)}")
