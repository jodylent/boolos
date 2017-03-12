from abc import ABCMeta, abstractmethod

import six
import random

import .util


@six.add_metaclass(ABCMeta)
class Role(object):
    """
    Abstract base class for roles that use "logic" to return booleans
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def answer(self, query):
        """
        Answer (evaluate) a query with a boolen answer

        :param query: a yes/no question, in the form of a logical condition
        :type query: str
        :return: boolean answer
        :rtype: bool
        """
        pass

    def evaluate(self, query, globals_d={}, locals_d=locals()):
        """
        Answer (evaluate) a query with a boolen answer. ALWAYS RETURNS TRUE ANSWER

        :param query: a yes/no question, in the form of a logical condition
        :type query: str
        :return: boolean answer
        :rtype: bool
        """
        return eval(query, globals_d, locals_d)


class T_God(Role):

    def __init__(self):
        pass

    def answer(self, query, globals_d={}, locals_d=locals()):
        return self.evaluate(query, globals_d, locals_d)


class F_God(Role):

    def __init__(self):
        pass

    def answer(self, query, globals_d={}, locals_d=locals()):
        return to_lie(self.evaluate(query, globals_d, locals_d))


class R_God(Role):

    def __init__(self):
        pass

    def answer(self, query, globals_d={}, locals_d=locals()):
        if random.randint(0, 1):
            return self.evaluate(query, globals_d, locals_d)
        else:
            return to_lie(self.evaluate(query, globals_d, locals_d))
