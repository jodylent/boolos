FALSY_LIST = ["false", "no", "0", "none"]


def ask(god, query, pantheon={}):
    return to_god_lang(god.answer(query, pantheon))


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


def test_query(p, q):
    """
    Tests a query and prints out full run details

    :param p: Pantheon to test
    :type p: boolos.model.Pantheon
    :param q: Query string to be processed by boolos.model.Role.evaluate()
    :type q: str
    """
    eng_val = p.a.answer(q, p)
    god_val = ask(p.a, q, p)

    test_string = """
    QUERY:   {0}
    ENGLISH: {1}
    GOD-ESE: {2}
    GODS:    {3}
    """

    print(test_string.format(q, eng_val, god_val, p))
