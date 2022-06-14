'''
Create a function that takes a string as an argument and returns the Morse code equivalent.
Examples

encode_morse("EDABBIT CHALLENGE") ➞ ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. ."

encode_morse("HELP ME !") ➞ ".... . .-.. .--.   -- .   -.-.--"

This dictionary can be used for coding:

char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}

Notes

    Ouput should be International Morse Code, and use the standard conventions for symbols 
    not defined inside the ITU recommendation (see Resources).
    Input value can be lower or upper case.
    Input string can have digits.
    Input string can have some special characters (e.g. comma, colon, apostrophe, period, 
    question mark, exclamation mark).
    One space " " is expected after each character, except the last one.
'''

class MorseTranslate:
    def __init__(self, message) -> None:
        self.message = message
        self.dictionary = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}

    def translate_for_char(self):
        message_words = self.message.split('   ')
        new_word = ''
        translated = ''

        for word in message_words:
            word_letters = word.split(' ')
            for letter in word_letters:
                for letter_char in self.dictionary:
                    if letter == self.dictionary[letter_char]:
                        new_word += letter_char
            translated += ' ' + new_word
            new_word = ''

        return translated

    def translate_for_morse(self):
        message_words = self.message.split(' ')
        new_word = ''
        translated = ''

        for word in message_words:
            for letter in word:
                for letter_char in self.dictionary:
                    if letter.upper() == letter_char:
                        new_word += ' ' + self.dictionary[letter_char]
            translated += '   ' + new_word
            new_word = ''
        return translated

if __name__ == '__main__':
    message1 = MorseTranslate(". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. .")
    message2 = MorseTranslate(".... . .-.. .--.   -- .   -.-.--")
    print(message1.translate_for_char(), message2.translate_for_char())
    print(f'type of message 1: {type(message1.translate_for_char())},  '
          f'type of message 2: {type(message2.translate_for_char())}')

    message3 = MorseTranslate("EdAbBiT ChALLeNGE")
    message4 = MorseTranslate("HELP ME !")
    print(f'{message3.translate_for_morse()}, \n {message4.translate_for_morse()}')