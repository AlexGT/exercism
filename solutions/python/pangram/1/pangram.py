from re import sub as re_sub


def is_pangram(sentence):
    cleaned_text = re_sub(r'[^a-zA-Z]', '', sentence).lower()
    return True if len(set(cleaned_text)) == 26 else False
