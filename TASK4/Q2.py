#Write a program to accept a string from the user and display characters, that are present at an even index number.

str = input("Enter a string ")
modified_string = str[::2]
print(modified_string)