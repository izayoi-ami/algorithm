##
from collections import deque
import operator

funcs = {
    "+": (2, operator.add),
    "-": (2, operator.sub),
    "*": (2, operator.mul),
    "/": (2, operator.truediv),
    "^": (2, operator.pow),
}
precedence = { # (precedence, is_right_associativity)
    "+": 10,
    "-": 10,
    "*": 20,
    "/": 20,
    "^": 30,
}
right_associative = {
    "^": True
}

def list_or_tuple(x):
    return isinstance(x, (list, tuple))

def flatten(seq, to_expand=list_or_tuple):
    iterators = [ iter(seq) ]
    res = []
    while iterators:
        for item in iterators[-1]: 
            if to_expand(item): 
                iterators.append(iter(item))
                break
            else: yield(item)
        else:
            iterators.pop()
    return res

class InfixExpr:
    def __init__(self, atoms):
        self.reset(atoms)

    def reset(self, atoms):
        self.atoms = atoms
        self._postfix = None
        self.ops = deque()
        self.vals = deque()

    def postfix(self):
        if self._postfix is not None: return self._postfix
        ops = self.ops
        vals = self.vals
        atoms = self.atoms

        for k in atoms:
            if k == "(": ops.append("(")
            elif k == ")":
                while ops[-1]!="(": self.operate()
                ops.pop()
            elif k not in precedence:
                vals.append(k)
            else:
                prec = precedence[k]
                while ops and ops[-1] in precedence and (prec < precedence[ops[-1]] or k not in right_associative and prec == precedence[ops[-1]]): self.operate()
                ops.append(k)

        while ops: self.operate()
        self._postfix = self.vals[-1]
        return self.vals[-1]

    def operate(self):
        op = self.ops.pop()
        num, _ = funcs[op]
        expr = [self.vals[-k-1] for k in reversed(range(num))] + [op]
        for _ in range(num): self.vals.pop()
        self.vals.append(expr)


class Calculator:

    def __init__(self, atoms=None):
        self.reset(atoms)

    def reset(self, atoms=None):
        self.atoms = atoms 
        self.ops = deque()
        self.vals = deque()

    def compute(self):
        atoms = self.atoms
        ops = self.ops
        vals = self.vals
        for k in atoms:
            if k == "(": ops.append("(")
            elif k == ")":
                while ops[-1] != "(": self.operate()
                ops.pop()
            elif k not in precedence:
                vals.append(k)
            else:
                prec = precedence[k]
                while len(ops)>0 and ops[-1] in precedence and (prec < precedence[ops[-1]] or k not in right_associative and prec == precedence[ops[-1]]): self.operate()
                ops.append(k)
        while len(ops) >0: self.operate()
        return vals[-1]

    def operate(self):
        op = self.ops.pop()
        num, func = funcs[op]
        args = [self.vals[-k-1] for k in reversed(range(num))]
        ans = func(*args)
        for _ in range(num): self.vals.pop()
        self.vals.append(ans)




        
##
