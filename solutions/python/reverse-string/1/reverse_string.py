def reverse(text):
    if hasattr(text, 'decode'):
        text = text.decode()

    return text[::-1]
