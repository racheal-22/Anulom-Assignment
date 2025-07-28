#Method 3: Reverse string program using recursive method

def reverse_recursive(s):
    if len(s) == 0:
        return ""
    return reverse_recursive(s[1:]) + s[0]

print("The Reverse String is: ",reverse_recursive("Interview"))
