# LOGIC OF KNOWLEDGE

"""Logical reasoning using existing knowledge"""


class Sentence:

    def symbols(self):
        """Prints the symbols present in the sentence"""
        return set()

    def evaluate(self, model):
        """Evaluates the logical sentence"""


class Symbol(Sentence):
    def __init__(self, name):
        self.name = name

    def symbols(self):
        return {self.name}

    def evaluate(self, model):
        try:
            return bool(model[self.name])
        except KeyError:
            pass


class And(Sentence):
    def __init__(self, *args):
        self.arguments = list(args)

    def symbols(self):
        return set.union(*[argument.symbols() for argument in self.arguments])

    def evaluate(self, model):
        return all(value.evaluate(model) for value in self.arguments)

    def add(self, *values):
        [self.arguments.append(value) for value in values]


class Or(Sentence):
    def __init__(self, *args):
        self.arguments = list(args)

    def symbols(self):
        return set.union(*[argument.symbols() for argument in self.arguments])

    def evaluate(self, model):
        return any(argument.evaluate(model) for argument in self.arguments)

    def add(self, *values):
        [self.arguments.append(value) for value in values]


class Not(Sentence):
    def __init__(self, argument):
        self.argument = argument

    def symbols(self):
        return self.argument.symbols()

    def evaluate(self, model):
        return not self.argument.evaluate(model)


class Implication(Sentence):
    def __init__(self, argument_1, argument_2):
        self.argument_1 = argument_1
        self.argument_2 = argument_2

    def symbols(self):
        return set.union(self.argument_1.symbols(), self.argument_2.symbols())

    def evaluate(self, model):
        return ((not self.argument_1.evaluate(model)) or
                self.argument_2.evaluate(model))


class Biconditional(Sentence):
    def __init__(self, argument_1, argument_2):
        self.argument_1 = argument_1
        self.argument_2 = argument_2

    def symbols(self):
        return set.union(self.argument_1.symbols(), self.argument_2.symbols())

    def evaluate(self, model):
        return ((self.argument_1.evaluate(model) and self.argument_2.evaluate(
            model)) or (not self.argument_1.evaluate(model) and not
        self.argument_2.evaluate(model)))


def model_check(basics, doubt):
    symbols = set.union(basics.symbols(), doubt.symbols())
    return model_allot(basics, doubt, symbols, dict())


def model_allot(knowledge, doubt, symbols, model):
    if not symbols:
        if knowledge.evaluate(model):
            return doubt.evaluate(model)
        return True

    remaining = symbols.copy()
    x = remaining.pop()

    module_true = model.copy()
    module_false = model.copy()
    module_true[x] = True
    module_false[x] = False

    return (model_allot(knowledge, doubt, remaining, module_true) and
            model_allot(knowledge, doubt, remaining, module_false))


# if __name__ == '__main__':
#     pass
# rain = Symbol("rain")
# hagrid = Symbol("hagrid")
# dumbledore = Symbol("dumbledore")
#
# knowledge = And(
#     Implication(Not(rain), hagrid),
#     Or(hagrid, dumbledore),
#     Not(And(hagrid, dumbledore)),
#     hagrid)
#
# print(model_check(knowledge, rain))
