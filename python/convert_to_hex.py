'''
Convert to Hex

Create a function that takes a string's characters as ASCII and returns each 
character's hexadecimal value as a string.
Examples

convert_to_hex("hello world") ➞ "68 65 6c 6c 6f 20 77 6f 72 6c 64"

convert_to_hex("Big Boi") ➞ "42 69 67 20 42 6f 69"

convert_to_hex("Marty Poppinson") ➞ 
    "4d 61 72 74 79 20 50 6f 70 70 69 6e 73 6f 6e"

Notes

    Each byte must be seperated by a space.
    All alpha hex characters must be lowercase.
'''

class HexConverter:
    def __init__(self, entry) -> None:
        self.entry = entry
        self.result = ''
        self.dict = {
                '0000': 0,
                '0001': 1,
                '0010': 2,
                '0011':	3,
                '0100': 4,
                '0101': 5,
                '0110':	6,
                '0111':	7,
                '1000':	8,
                '1001':	9,
                '1010':	'A',
                '1011':	'B',
                '1100':	'C',
                '1101':	'D',
                '1110':	'E',
                '1111':	'F'
                }

    def convert_to_hex(self, letter):
        temp = bin(ord(letter))[2:].zfill(8)
        a, b = temp[:4], temp[4:]

        for i in self.dict:
            if a == i:
                a = self.dict[i]
            elif b == i:
                b = self.dict[i]

        temp = str(a) + str(b)
        return temp

    def convert_all(self):
        for i in self.entry:
            self.result += ' ' + self.convert_to_hex(letter=i)
        
        return self.result


if __name__ == '__main__':
    test = HexConverter("hello horld")
    print(test.convert_all())
    test = HexConverter("Marty Poppinson")
    print(test.convert_all())

    
    