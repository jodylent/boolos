import six
import random

from abc import ABCMeta, abstractmethod
from boolos.util import to_lie


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

    def evaluate(self, query, pantheon):
        """
        Answer (evaluate) a query with a boolen answer.
        ALWAYS RETURNS TRUE ANSWER--negation for F/R is done with boolos.util.to_lie()

        :param query: a yes/no question, in the form of a logical condition
        :type query: str
        :param pantheon: Pantheon instance by which to evaluate query
        :pantheon: boolos.model.Pantheon
        :return: boolean answer
        :rtype: bool
        """
        globals_d = {
            "Role": Role,
            "T_God": T_God,
            "F_God": F_God,
            "R_God": R_God,
            "Pantheon": Pantheon
        }
        return eval(query, globals_d, pantheon.to_dict())


class T_God(Role):

    def __init__(self):
        self.name = "true"

    def answer(self, query, pantheon):
        return self.evaluate(query, pantheon)


class F_God(Role):

    def __init__(self):
        self.name = "false"

    def answer(self, query, pantheon):
        return to_lie(self.evaluate(query, pantheon))


class R_God(Role):

    def __init__(self):
        self.name = "random"

    def answer(self, query, pantheon):
        if random.randint(0, 1):
            return pantheon._t_god.evaluate(query, pantheon)
        else:
            return pantheon._f_god.evaluate(query, pantheon)


class Pantheon(object):
    """
    """

    def __init__(self, force_order=False):
        """
        """
        self._t_god = T_God()
        self._f_god = F_God()
        self._r_god = R_God()
        self.force_order = force_order
        # Randomize words
        if random.randint(0, 1):
            self.yes = "ja"
            self.no = "da"
        else:
            self.yes = "da"
            self.no = "ja"
        g_list = [self._t_god, self._f_god, self._r_god]
        # Randomize assignment to A, B, C
        if not self.force_order:
            random.shuffle(g_list)
        # Assign exposed roles
        self.a = g_list[0]
        self.b = g_list[1]
        self.c = g_list[2]

    def to_dict(self):
        return {
            "t": self._t_god,
            "f": self._f_god,
            "r": self._r_god,
            "a": self.a.name,
            "b": self.b.name,
            "c": self.c.name
        }

    def __str__(self):
        return "<{0}: A={1}; B={2}; C={3}; Y='{4}'>".format(self.__class__.__name__,
                                                            self.a.name.title(),
                                                            self.b.name.title(),
                                                            self.c.name.title(),
                                                            self.yes)
