'''
Casino Security
You're head of security at a casino that has money being stolen from it. You get the data in the 
form of strings and you have to set off an alarm if a thief is detected.

If there is no guard between thief and money, return "ALARM!"
If the money is protected, return "Safe"
String Components
x - Empty Space
T - Thief
G - Guard
$ - Money
Examples
security("xxxxTTxGxx$xxTxxx") ➞ "ALARM!"

security("xxTxxG$xxxx$xxxx") ➞ "Safe"

security("TTxxxx$xxGxx$Gxxx") ➞ "ALARM!"
Notes
Money at the extremes are safe.
'''

class CassinoHead:
    def __init__(self, data):
        self.data = data
        self.safe = True
        self.money_indexes = [n for n, i in enumerate(self.data) if i == '$']

    def check_direction(self, position):
        right = self.data[position+1::]
        left = self.data[:position:]

        for i in right:
            if i == 'G' or i == '$':
                self.safe = True
                break
            elif i == 'T':
                self.safe = False
                break

        for i in left[::-1]:
            if i == 'G' or i == '$':
                self.safe = True
                break
            elif i == 'T':
                self.safe = False
                break

    def security(self):
        for p in self.money_indexes:
            self.check_direction(position=p)
        if self.safe:
            print('Safe')
            return 'Safe'
        else:
            print('ALARM!')
            return 'ALARM!'

if __name__ == '__main__':
    a = "xxxxTTxGxx$xxTxxx"
    b = "xxTxxG$xxxx$xxxx"

    situation_1 = CassinoHead(a)
    situation_1.security()

    situation_2 = CassinoHead(b)
    situation_2.security()