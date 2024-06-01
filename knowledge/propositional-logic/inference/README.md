# Inference
In propositional logic, inference refers to the process of deriving new logical conclusions or propositions from existing ones using valid rules of inference. It involves applying logical reasoning to determine the truth or falsity of statements based on established logical principles.

## Propositional Logic
Propositional logic is a formal system that deals with atomic propositions, logical operators, and their combinations to represent states of truth or falsity.

### Fundamental Elements
- **Atomic Propositions:** Simple statements that can be either true or false, represented by propositional letters such as $p$, $q$, $r$, etc.
- **Logical Operators:** Symbols that combine propositions to form compound propositions.
  - **Negation ($\lnot$):** Represents the negation of a proposition. **Example:** $\lnot p$ means $\text{not p}$.
  - **Conjunction ($\land$):** Represents the conjunction of two propositions. **Example:** $p \land q$ means $\text{p and q}$.
  - **Disjunction ($\lor$):** Represents the disjunction of two propositions. **Example:** $p \lor q$ means $\text{p or q}$.
  - **Conditional ($\rightarrow$):** Represents the implication between two propositions. **Example:** $p \rightarrow q$ means $\text{if p, then q}$.
  - **Biconditional ($\leftrightarrow$):** Represents the biconditionality between two propositions. **Example:** $p \leftrightarrow q$ means $\text{p if and only if q}$.

## Usage
```bash
python inference.py
```

## Example
### True
1. $p \lor (q \land r), (p \lor q) \rightarrow s \vdash p \lor s$

<div align="center">

| $p$ | $q$ | $r$ | $s$ | $(p \lor (q ∧ r)) \land ((p \lor q) \rightarrow s)$ | $p \lor s$ |
|:-:|:-:|:-:|:-:|:-:|:-:|
| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} F}$	|
| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} V}$	| ${\color{gray} F}$	| ${\color{gray} V}$	|
| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} V}$	| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} F}$	|
| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} V}$	| ${\color{gray} V}$	| ${\color{gray} F}$	| ${\color{gray} V}$	|
| ${\color{gray} F}$	| ${\color{gray} V}$	| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} F}$	|
| ${\color{gray} F}$	| ${\color{gray} V}$	| ${\color{gray} F}$	| ${\color{gray} V}$	| ${\color{gray} F}$	| ${\color{gray} V}$	|
| ${\color{gray} F}$	| ${\color{gray} V}$	| ${\color{gray} V}$	| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} F}$	|
| ${\color{gray} F}$	| ${\color{gray} V}$	| ${\color{gray} V}$	| ${\color{gray} V}$	| ${\color{lime} V}$	| ${\color{lime} V}$	|
| ${\color{gray} V}$	| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} V}$	|
| ${\color{gray} V}$	| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} V}$	| ${\color{lime} V}$	| ${\color{lime} V}$	|
| ${\color{gray} V}$	| ${\color{gray} F}$	| ${\color{gray} V}$	| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} V}$	|
| ${\color{gray} V}$	| ${\color{gray} F}$	| ${\color{gray} V}$	| ${\color{gray} V}$	| ${\color{lime} V}$	| ${\color{lime} V}$	|
| ${\color{gray} V}$	| ${\color{gray} V}$	| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} V}$	|
| ${\color{gray} V}$	| ${\color{gray} V}$	| ${\color{gray} F}$	| ${\color{gray} V}$	| ${\color{lime} V}$	| ${\color{lime} V}$	|
| ${\color{gray} V}$	| ${\color{gray} V}$	| ${\color{gray} V}$	| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} V}$	|
| ${\color{gray} V}$	| ${\color{gray} V}$	| ${\color{gray} V}$	| ${\color{gray} V}$	| ${\color{lime} V}$	| ${\color{lime} V}$	|

</div>

### False
2. $p \lor (q \land r), (p \lor q) \rightarrow s \vdash p \land s$

<div align="center">

| $p$ | $q$ | $r$ | $s$ | $(p \lor (q ∧ r)) \land ((p \lor q) \rightarrow s)$ | $p \land s$ |
|:-:|:-:|:-:|:-:|:-:|:-:|
| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} F}$	|
| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} V}$	| ${\color{gray} F}$	| ${\color{gray} F}$	|
| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} V}$	| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} F}$	|
| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} V}$	| ${\color{gray} V}$	| ${\color{gray} F}$	| ${\color{gray} F}$	|
| ${\color{gray} F}$	| ${\color{gray} V}$	| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} F}$	|
| ${\color{gray} F}$	| ${\color{gray} V}$	| ${\color{gray} F}$	| ${\color{gray} V}$	| ${\color{gray} F}$	| ${\color{gray} F}$	|
| ${\color{gray} F}$	| ${\color{gray} V}$	| ${\color{gray} V}$	| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} F}$	|
| ${\color{gray} F}$	| ${\color{gray} V}$	| ${\color{gray} V}$	| ${\color{gray} V}$	| ${\color{lime} V}$	| ${\color{red} F}$	|
| ${\color{gray} V}$	| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} F}$	|
| ${\color{gray} V}$	| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} V}$	| ${\color{lime} V}$	| ${\color{lime} V}$	|
| ${\color{gray} V}$	| ${\color{gray} F}$	| ${\color{gray} V}$	| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} F}$	|
| ${\color{gray} V}$	| ${\color{gray} F}$	| ${\color{gray} V}$	| ${\color{gray} V}$	| ${\color{lime} V}$	| ${\color{lime} V}$	|
| ${\color{gray} V}$	| ${\color{gray} V}$	| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} F}$	|
| ${\color{gray} V}$	| ${\color{gray} V}$	| ${\color{gray} F}$	| ${\color{gray} V}$	| ${\color{lime} V}$	| ${\color{lime} V}$	|
| ${\color{gray} V}$	| ${\color{gray} V}$	| ${\color{gray} V}$	| ${\color{gray} F}$	| ${\color{gray} F}$	| ${\color{gray} F}$	|
| ${\color{gray} V}$	| ${\color{gray} V}$	| ${\color{gray} V}$	| ${\color{gray} V}$	| ${\color{lime} V}$	| ${\color{lime} V}$	|

</div>

## References
- [CS50’s Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/2024/)
