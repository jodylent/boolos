FALSY_LIST = ["false", "no", "0", "none"]


def ask(god, self, query):
    return to_god_lang(god.answer(query))


def to_lie(val):
    if isinstance(val, bool):
        if val:
            return False
        return True
    if isinstance(val, basestring):
        if val.lower() in FALSY_LIST:
            return True
        return False


def to_god_lang(val, yes_word="ja", no_word="da"):
    if val:
        return yes_word
    else:
        return no_word
