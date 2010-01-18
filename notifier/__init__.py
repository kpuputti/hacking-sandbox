from notifier.words import profanities

def is_profane(text):
    words = (s.lower() for s in text.split())
    for w in words:
        if w in profanities['en']:
            return True
        elif w in profanities['fi']:
            return True
        else:
            try:
                w = w.decode('utf-8')
            except UnicodeEncodeError:
                continue
            if w in profanities['fi']:
                return True
    return False
