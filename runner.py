import argparse
import pdb

from boolos.model import Pantheon
from boolos.util import test_query

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--force-order", "-f",
                        action="store_true",
                        dest="force_order",
                        default=False,
                        help="force order: A:T, B:F, C:R")

    parser.add_argument("--query", "-q",
                        action="store",
                        dest="query",
                        type=str,
                        default=None,
                        help="Query")

    parser.add_argument("--god", "-g",
                        action="store",
                        dest="god",
                        type=str,
                        default="a",
                        help="God to query (default: A)")

    parser.add_argument("--interactive", "-i",
                        action="store_true",
                        dest="interactive",
                        default=False)

    args = parser.parse_args()

    # Generate a pantheon
    p = Pantheon(args.force_order)

    if args.interactive:
        pdb.set_trace()
        exit()

    # run the query
    if args.query:
        test_query(args.god, p, args.query)
    else:
        q = "isinstance(a, F_God)"
        print("RUNNING DEFAULT QUERY: {0}".format(q))
        test_query(args.god, p, q)
