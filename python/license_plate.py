'''
License Plate
Traveling through Europe one needs to pay attention to how the license plate in 
the given country is displayed. When crossing the border you need to park on the 
shoulder, unscrew the plate, re-group the characters according to the local 
regulations, attach it back and proceed with the journey.

Create a solution that can format the dmv number into a plate number with 
correct grouping. The function input consists of a string s and group length n. 
The output has to be upper case characters and digits. The new count_groups are made 
from right to left and connected by -. The original order of the dmv number is 
preserved.

Examples
license_plate("5F3Z-2e-9-w", 4) ➞ "5F3Z-2E9W"

license_plate("2-5g-3-J", 2) ➞ "2-5G-3J"

license_plate("2-4A0r7-4k", 3) ➞ "24-A0R-74K"

license_plate("nlj-206-fv", 3) ➞ "NL-J20-6FV"
'''

def license_plate(s, n):
    count_groups = len(s.replace('-', '')) // n
    groups = [[] for i in range(count_groups)]
    cursor = 1
    
    for group in range(count_groups):
        while True:
            if cursor <= n:
                if s[-1] != '-':
                    groups[group].append(s[-1])
                    s = s.strip(s[-1])
                    cursor += 1
                else:
                    s = s.strip(s[-1])
            else:
                cursor = 1
                break
    if not s:
        for group in groups[::-1]:
            for char in group[::-1]:
                s += char.upper()
            s += '-'
    
    elif s[-1] == '-':
        for group in groups[::-1]:
            for char in group[::-1]:
                s += char.upper()
            s += '-'
    
    else:
        s += '-'
        for group in groups[::-1]:
            for char in group[::-1]:
                s += char.upper()
            s += '-'

    return s[:-1]


print(license_plate("5F3Z-2e-9-w", 4))
print(license_plate("2-5g-3-J", 2))