class NoComparisonAvailableException(Exception):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs


class ComparisonMemory:
    def __init__(self, initial_state):
        self.state = set(initial_state) if initial_state else set()

    def lt(self, lhs, rhs):
        if (lhs, rhs) in self.state:
            return True
        if (rhs, lhs) in self.state:
            return False
        raise NoComparisonAvailableException(lhs, rhs)

    def gt(self, lhs, rhs):
        return self.lt(rhs, lhs)

    def add_lt(self, lhs, rhs):
        self.state.add((lhs, rhs))


class ComparisonMemoryElement:
    def __init__(self, value, memory):
        self.value = value
        self.memory = memory

    def __lt__(self, other):
        return self.memory.lt(self.value, other.value)

    def __gt__(self, other):
        return self.memory.gt(self.value, other.value)

    def __repr__(self):
        return "CME({})".format(self.value)
