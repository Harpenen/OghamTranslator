import pyperclip as cb
ogham={
    " ":" ",

    "ng":"ᚍ",
    "or":"ᚖ",
    "ui":"ᚗ",
    "ea":"ᚕ",
    "ia":"ᚘ",
    "ae":"ᚙ",

    "a":"ᚐ",
    "b":"ᚁ",
    "c":"ᚉ",
    "d":"ᚇ",
    "e":"ᚓ",
    "f":"ᚃ",
    "g":"ᚌ",
    "h":"ᚆ",
    "i":"ᚔ",
    
    "l":"ᚂ",
    "m":"ᚋ",
    "n":"ᚅ",
    "o":"ᚑ",
    "p":"ᚚ",
    "q":"ᚊ",
    "r":"ᚏ",
    "s":"ᚄ",
    "t":"ᚈ",
    "u":"ᚒ",
    
    "z":"ᚎ",


    "j":"ᚌ",
    "k":"ᚊ",

    "v":"ᚃ",
    "w":"ᚒᚒ",
    "x":"ᚎ",
    "y":"ᚔ"
}

while True:
    text=(input("Enter ASCII to encode or ogham to decode\n")).lower()

    if text.isascii()==True:
        for key in ogham.keys():
            text=text.replace(key, str(ogham[key]))
        cb.copy("᚛"+text+"᚜")
        print("Text was automatically copied to clipboard")

    else:
        for key in ogham.keys():
            text=text.replace(str(ogham[key]), key)
        text=(text.rstrip("᚜")).lstrip("᚛")
        print(text)