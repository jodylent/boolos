import argparse

from boolos.model import Pantheon
from boolos.util import test_query

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--query", "-q",
                        action="store",
                        dest="query",
                        type=str,
                        default=None,
                        help="query")
    args = parser.parse_args()

    # Generate a pantheon
    p = Pantheon()

    # run the query
    if args.query:
        test_query(p, args.query)
    else:
        print("RUNNING DEFAULT QUERY")
        q = "isinstance(a, F_God)"
        test_query(p, q)
