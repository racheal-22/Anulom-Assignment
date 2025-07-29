#Reverse string using 2 pointer method 
def reverse_two_pointer(s):
    chars = list(s)
    left = 0
    right = len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    reversed_str = ""
    for ch in chars:
        reversed_str += ch
    return reversed_str

print("The Reversed String is ", reverse_two_pointer("Interview"))
