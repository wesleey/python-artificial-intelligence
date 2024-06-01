from logic import *

p = Symbol("p")
q = Symbol("q")
r = Symbol("r")
s = Symbol("s")

# p ∨ (q ∧ r), (p ∨ q) → s
knowledge = And(
    Or(p, And(q, r)),  # p ∨ (q ∧ r)
    Implication(Or(p, q), s)  # (p ∨ q) → s
)

print(knowledge.formula())

# p ∨ (q ∧ r), (p ∨ q) → s ⊢ p ∨ s
print(model_check(knowledge, Or(p, s)))

# p ∨ (q ∧ r), (p ∨ q) → s ¬⊢ p ∧ s
print(model_check(knowledge, And(p, s)))
