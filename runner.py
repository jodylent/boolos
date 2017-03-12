from boolos.model import Pantheon
from boolos.util import test_query

p = Pantheon()
# q = "1 == 1"
q = "isinstance(a, F_God)"

test_query(p, q)
