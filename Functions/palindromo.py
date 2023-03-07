def invert_text(text):
    text_without_spaces = remove_spaces(text)
    inverted_text = ""
    for txt in text_without_spaces:
        inverted_text = txt + inverted_text
    print(inverted_text.lower() == text_without_spaces.lower())


def remove_spaces(text):
    new_text = ""
    for txt in text:
        if (txt != " "):
            new_text += txt
    return new_text


invert_text("moom")
