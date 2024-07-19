# this dict is from online source: https://www.geeksforgeeks.org/morse-code-translator-python/#
eng_to_morse = {'A': '.-', 'B': '-...',
                'C': '-.-.', 'D': '-..', 'E': '.',
                'F': '..-.', 'G': '--.', 'H': '....',
                'I': '..', 'J': '.---', 'K': '-.-',
                'L': '.-..', 'M': '--', 'N': '-.',
                'O': '---', 'P': '.--.', 'Q': '--.-',
                'R': '.-.', 'S': '...', 'T': '-',
                'U': '..-', 'V': '...-', 'W': '.--',
                'X': '-..-', 'Y': '-.--', 'Z': '--..',
                '1': '.----', '2': '..---', '3': '...--',
                '4': '....-', '5': '.....', '6': '-....',
                '7': '--...', '8': '---..', '9': '----.',
                '0': '-----', ', ': '--..--', '.': '.-.-.-',
                '?': '..--..', '/': '-..-.', '-': '-....-',
                '(': '-.--.', ')': '-.--.-'}
morse_to_english = {v: k for k, v in eng_to_morse.items()}
print(morse_to_english)
method = input(
    "Please tell me which one do you want to translate into (enter English or Morse): ").lower()
if method == "morse":
    res = ''
    text = input(
        "Please enter what you want to translate into morse code:").upper()
    for letter in text:
        # print(letter)
        if letter in eng_to_morse:
            res += eng_to_morse[letter]
            res += " "
        else:
            res = "Sorry we cannot find some of the characters. We will keep updating to ensure better experience!"
    print(res)
elif method == "english":
    res = ''
    text = input(
        "Please enter what you want to translate into english:").upper()
    text = text.split(" ")
    print(text)
    for letter in text:
        if letter in morse_to_english:
            res += morse_to_english[letter]
            # res += " "
        else:
            res = "Sorry we cannot find some of the characters. We will keep updating to ensure better experience!"
    print(res)
