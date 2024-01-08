
morse_dict = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '.---',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----',
        '?': '..--..',
        '!': '-.-.--',
        '.': '.-.-.-',
        ',': '--..--',
        ';': '-.-.-.',
        ':': '---...',
        '+': '.-.-.',
        '-': '-....-',
        '/': '-..-.',
        '=': '-...-',
        ' ': '   '
    }

def encode(text):
    cap_text = list(text.upper())
    morse_code = ''
    for letter in cap_text:
        if letter != ' ':
            morse_code += morse_dict[letter] + ' '
        else:
            morse_code += ' '

    return morse_code


def decode(code):
    text = ''
    split_list = code.split('   ')
    strip_list = [item.strip().split() for item in split_list]
    spaced_list = [e for i in strip_list for e in [i, [' ']]][:-1]
    for morse_word in spaced_list:
        for morse_letter in morse_word:
            if morse_letter == ' ':
                    text += ' '
            else:
                for key, value in morse_dict.items():
                    if morse_letter == value:
                        text += key
    return text

test_string = 'This is a test'
test_morse = '- .... .. ...     .. ...     .-     - . ... -'

print(encode('This is a secret message'))
print(decode(test_morse))