print("question 1")
def reverse(string):
    if len(string) == 1:
        return string
    else:
        return string[-1:] + reverse(string[:-1])
str_input = str(input("enter string to take its reverse : "))
print(reverse(str_input))    
