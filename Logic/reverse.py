#method one Brute force method 

def reverse_brute_force(s):
    result = ""
    for i in range(len(s)):
        result = s[i] + result
    return result

print(reverse_brute_force("Interview"))
