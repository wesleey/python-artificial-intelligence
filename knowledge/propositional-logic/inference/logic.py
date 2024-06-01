from typing import Set, List, Dict
from abc import ABC, abstractmethod


class Sentence(ABC):
    @abstractmethod
    def evaluate(self, model: object) -> bool:
        """Evaluates the logical sentence."""

    @abstractmethod
    def formula(self) -> str:
        """Returns string formula representing logical sentence."""

    @abstractmethod
    def symbols(self) -> Set[str]:
        """Returns a set of all symbols in the logical sentence."""

    @classmethod
    def validate(cls, sentence: object) -> None:
        if not isinstance(sentence, Sentence):
            raise TypeError("Must be a logical sentence.")

    @classmethod
    def parenthesize(cls, expression: str) -> str:
        """Parenthesizes an expression if not already parenthesized."""
        def balanced(string: str) -> bool:
            """Checks if a string has balanced parentheses."""
            count = 0
            for char in string:
                if char == "(":
                    count += 1
                elif char == ")":
                    if count <= 0:
                        return False
                    count -= 1
            return count == 0

        def parenthesized(string: str) -> bool:
            """Check if a string is in parentheses."""
            return string.startswith("(") and string.endswith(")")

        def empty(string: str) -> bool:
            """Check if a string is empty."""
            return not len(string)

        if empty(expression) or expression.isalpha() or (
            parenthesized(expression) and balanced(expression[1:-1])
        ):
            return expression
        else:
            return f"({expression})"


class Symbol(Sentence):
    def __init__(self, name: str) -> None:
        self.name = name

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Symbol) and self.name == other.name

    def __hash__(self) -> hash:
        return hash(("symbol", self.name))

    def __repr__(self) -> str:
        return self.name

    def evaluate(self, model: object) -> bool:
        try:
            return bool(model[self.name])
        except KeyError:
            raise Exception(f"Variable {self.name} not in model.")

    def formula(self) -> str:
        return self.name

    def symbols(self) -> Set[str]:
        return set(self.name)


class Not(Sentence):
    def __init__(self, operand: Sentence) -> None:
        self.operand = operand

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Not) and self.operand == other.operand

    def __hash__(self) -> hash:
        return hash(("not", hash(self.operand)))

    def __repr__(self) -> str:
        return f"Not({self.operand})"

    @property
    def operand(self) -> Sentence:
        return self._operand

    @operand.setter
    def operand(self, operand: Sentence) -> None:
        Sentence.validate(operand)
        self._operand = operand

    def evaluate(self, model: object) -> bool:
        return not self.operand.evaluate(model)

    def formula(self) -> str:
        return "¬" + Sentence.parenthesize(self.operand.formula())

    def symbols(self) -> Set[str]:
        return self.operand.symbols()


class And(Sentence):
    def __init__(self, *conjuncts: Sentence) -> None:
        self.conjuncts = conjuncts

    def __eq__(self, other: object) -> bool:
        return isinstance(other, And) and self.conjuncts == other.conjuncts

    def __hash__(self) -> hash:
        return hash(
            ("and", tuple(hash(conjunct) for conjunct in self.conjuncts))
        )

    def __repr__(self) -> str:
        conjunctions = ", ".join(
            [str(conjunct) for conjunct in self.conjuncts]
        )
        return f"And({conjunctions})"

    @property
    def conjuncts(self) -> List[Sentence]:
        return self._conjuncts

    @conjuncts.setter
    def conjuncts(self, conjuncts: List[Sentence]) -> None:
        for conjunct in conjuncts:
            Sentence.validate(conjunct)
        self._conjuncts = list(conjuncts)

    def add(self, conjunct: Sentence) -> None:
        Sentence.validate(conjunct)
        self.conjuncts.append(conjunct)

    def evaluate(self, model: object) -> bool:
        return all(conjunct.evaluate(model) for conjunct in self.conjuncts)

    def formula(self) -> str:
        if len(self.conjuncts) == 1:
            return self.conjuncts[0].formula()
        return " ∧ ".join([Sentence.parenthesize(conjunct.formula())
                           for conjunct in self.conjuncts])

    def symbols(self) -> Set[str]:
        return set.union(*[conjunct.symbols() for conjunct in self.conjuncts])


class Or(Sentence):
    def __init__(self, *disjuncts: Sentence) -> None:
        self.disjuncts = disjuncts

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Or) and self.disjuncts == other.disjuncts

    def __hash__(self) -> hash:
        return hash(
            ("or", tuple(hash(disjunct) for disjunct in self.disjuncts))
        )

    def __repr__(self) -> str:
        disjuncts = ", ".join([str(disjunct) for disjunct in self.disjuncts])
        return f"Or({disjuncts})"

    @property
    def disjuncts(self) -> List[Sentence]:
        return self._disjuncts

    @disjuncts.setter
    def disjuncts(self, disjuncts: List[Sentence]):
        for disjunct in disjuncts:
            Sentence.validate(disjunct)
        self._disjuncts = list(disjuncts)

    def evaluate(self, model: object) -> bool:
        return any(disjunct.evaluate(model) for disjunct in self.disjuncts)

    def formula(self) -> str:
        if len(self.disjuncts) == 1:
            return self.disjuncts[0].formula()
        return " ∨ ".join([Sentence.parenthesize(disjunct.formula())
                           for disjunct in self.disjuncts])

    def symbols(self) -> Set[str]:
        return set.union(*[disjunct.symbols() for disjunct in self.disjuncts])


class Implication(Sentence):
    def __init__(self, antecedent: Sentence, consequent: Sentence) -> None:
        self.antecedent = antecedent
        self.consequent = consequent

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Implication) and (
            self.antecedent == other.antecedent and
            self.consequent == other.consequent
        )

    def __hash__(self) -> hash:
        return hash(("implies", hash(self.antecedent), hash(self.consequent)))

    def __repr__(self) -> str:
        return f"Implication({self.antecedent}, {self.consequent})"

    @property
    def antecedent(self) -> Sentence:
        return self._antecedent

    @property
    def consequent(self) -> Sentence:
        return self._consequent

    @antecedent.setter
    def antecedent(self, antecedent: Sentence) -> None:
        Sentence.validate(antecedent)
        self._antecedent = antecedent

    @consequent.setter
    def consequent(self, consequent: Sentence) -> None:
        self._consequent = consequent

    def evaluate(self, model: object) -> bool:
        return not self.antecedent.evaluate(model) or (
            self.consequent.evaluate(model)
        )

    def formula(self) -> str:
        antecedent = Sentence.parenthesize(self.antecedent.formula())
        consequent = Sentence.parenthesize(self.consequent.formula())
        return f"{antecedent} → {consequent}"

    def symbols(self) -> Set[str]:
        return set.union(self.antecedent.symbols(), self.consequent.symbols())


class Biconditional(Sentence):
    def __init__(self, left: Sentence, right: Sentence) -> None:
        self.left = left
        self.right = right

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Biconditional) and (
            self.left == other.left and self.right == other.right
        )

    def __hash__(self) -> hash:
        return hash(("biconditional", hash(self.left), hash(self.right)))

    def __repr__(self) -> str:
        return f"Biconditional({self.left}, {self.right})"

    @property
    def left(self) -> Sentence:
        return self._left

    @property
    def right(self) -> Sentence:
        return self._right

    @left.setter
    def left(self, left: Sentence) -> None:
        Sentence.validate(left)
        self._left = left

    @right.setter
    def right(self, right: Sentence) -> None:
        Sentence.validate(right)
        self._right = right

    def evaluate(self, model: object) -> bool:
        return self.left.evaluate(model) and self.right.evaluate(model) or (
            not self.left.evaluate(model) and not self.right.evaluate(model)
        )

    def formula(self) -> str:
        left = Sentence.parenthesize(str(self.left))
        right = Sentence.parenthesize(str(self.right))
        return f"{left} ↔ {right}"

    def symbols(self) -> Set[str]:
        return set.union(self.left.symbols(), self.right.symbols())


def model_check(knowledge: Sentence, query: Sentence) -> bool:
    """Checks if knowledge base entails query."""

    def check_all(knowledge, query, symbols, model):
        """Checks if knowledge base entails query, given a particular model."""

        # If model has an assignment for each symbol.
        if not symbols:
            # If knowledge base is true in model, then query must also be true.
            if knowledge.evaluate(model):
                return query.evaluate(model)
            return True
        else:
            # Choose one of the remaining unused symbols.
            remaining: Set[str] = symbols.copy()
            symbol = remaining.pop()

            # Create a model where the symbol is true.
            model_true: Dict[str, bool] = model.copy()
            model_true[symbol] = True

            # Create a model where the symbol is false.
            model_false: Dict[str, bool] = model.copy()
            model_false[symbol] = False

            # Ensure entailment holds in both models.
            return (check_all(knowledge, query, remaining, model_true) and
                    check_all(knowledge, query, remaining, model_false))

    # Get all symbols in both knowledge and query.
    symbols = set.union(knowledge.symbols(), query.symbols())

    # Check that knowledge entails query.
    return check_all(knowledge, query, symbols, dict())
