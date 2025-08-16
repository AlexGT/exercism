def response(hey_bob):
    hey_bob = hey_bob.strip()
    msg = "Whatever."
    
    if not hey_bob:
        return "Fine. Be that way!"
    elif hey_bob[-1] == "?":
        if hey_bob.isupper():
            msg = "Calm down, I know what I'm doing!"
        else:
            msg = "Sure."
    elif hey_bob.isupper():
        msg = "Whoa, chill out!"
    return msg
