import requests

url_to_morse = "https://api.funtranslations.com/translate/morse.json"

parameters_morse = {"text": input(
    "Please enter the text you want to translate into morse code: ")}

res_morse = requests.get(url_to_morse, params=parameters_morse)
print(f"Response status code is: {res_morse.status_code}")
trans = res_morse.json()
txt = trans["contents"]['text']
translatino = trans["contents"]['translated']
print(f'You wanted to translate {txt}')
print(f"Your result is {translatino}")

url_to_english = "http://api.funtranslations.com/translate/morse2english.json"
res_english = requests.get(url_to_morse, params=url_to_morse)
parameters_morse = {"text": input(
    "Please enter the text you want to translate into English: ")}
res_english = requests.get(url_to_english, params=parameters_morse)
print(f"Response status code is: {res_morse.status_code}")
trans = res_english.json()
txt = trans["contents"]['text']
translation = trans["contents"]['translated']
print(f'You wanted to translate {txt}')
print(f"Your result is {translation}")
