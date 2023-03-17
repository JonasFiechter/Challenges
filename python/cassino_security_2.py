'''
Casino Security
You're head of security at a casino that has money being stolen from it. 
You get the data in the form of strings and you have to set off an alarm if a 
thief is detected.

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

def security(cassino_str):
    thief_sight = False
    money_sight = False
    for char in cassino_str:
        if char == 'T':
            thief_sight = True
        elif char == '$':
            money_sight = True

        if money_sight and thief_sight:
            return "ALARM!"
        
        elif char == 'G':
            money_sight = False
            thief_sight = False
    
    return "Safe"


if __name__ == '__main__':
    print(security("xxxxTTxGxx$xxTxxx"))
    print(security("xxTxxG$xxxx$xGTx"))
    print(security("TTxxxx$xxGxx$Gxxx"))