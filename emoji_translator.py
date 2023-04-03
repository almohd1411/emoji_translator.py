import emoji

def translate_to_emoji(text):
    emoji_text = ""
    for char in text:
        if char.isalpha():
            emoji_char = ":regional_indicator_" + char.lower() + ":"
            emoji_text += emoji.emojize(emoji_char)
        elif char == " ":
            emoji_text += "    "
        else:
            emoji_text += char
    return emoji_text

input_text = input("Enter text to translate: ")
print(translate_to_emoji(input_text))
