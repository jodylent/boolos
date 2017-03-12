FALSY_LIST = ["false", "no", "0", "none"]


def ask(god, query, pantheon={}):
    return to_god_lang(god.answer(query, pantheon), pantheon)


def to_lie(val):
    if isinstance(val, bool):
        if val:
            return False
        return True
    if isinstance(val, basestring):
        if val.lower() in FALSY_LIST:
            return True
        return False


def to_god_lang(val, pantheon):
    if val:
        return pantheon.yes
    else:
        return pantheon.no


def test_query(g, p, q):
    """
    Tests a query and prints out full run details

    :param g: God to query [ A | B | C ]
    :type g: str
    :param p: Pantheon to test
    :type p: boolos.model.Pantheon
    :param q: Query string to be processed by boolos.model.Role.evaluate()
    :type q: str
    """
    god = getattr(p, g)
    evl_val = god.evaluate(q, p)
    eng_val = god.answer(q, p)
    god_val = ask(god, q, p)

    test_string = """
    QUERY {0}: {1}
    EVAL TO: {2}
    ENGLISH: {3}
    GOD-ESE: {4}
    GODS:    {5}
    """

    print(test_string.format(g, q, evl_val, eng_val, god_val, p))
