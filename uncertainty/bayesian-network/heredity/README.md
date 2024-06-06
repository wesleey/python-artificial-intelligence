# Heredity

Mutated versions of the GJB2 gene are one of the leading causes of hearing impairment in newborns. Each person carries two versions of the gene, so each person has the potential to possess either 0, 1, or 2 copies of the hearing impairment version GJB2. Unless a person undergoes genetic testing, though, it’s not so easy to know how many copies of the mutated GJB2 a person has. This is a "hidden state": information that has an effect that we can observe (hearing impairment), but that we don’t necessarily directly know. After all, some people might have 1 or 2 copies of mutated GJB2 but not exhibit hearing impairment, while others might have no copies of mutated GJB2 yet still exhibit hearing impairment.

## Usage
```bash
python heredity.py data.csv
```

## Bayesian Network

A [Bayesian Network](https://en.wikipedia.org/wiki/Bayesian_network) is a probabilistic graphical model that represents a set of random variables and their conditional dependencies via a directed acyclic graph (DAG). In the context of genetic traits like the mutated GJB2 gene, a Bayesian Network can help model and analyze the complex relationships between genes, traits, and inheritance patterns.

![Gene Network](./images/gene_network.png)

## Probabilities
### $P(G_{n})$: Probabilities of having $n$ copies of the gene

$$
\begin{aligned}
&P(G_{0}) = 96\\% = 0.96\\
&P(G_{1}) = 3\\% = 0.03\\
&P(G_{2}) = 1\\% = 0.01\\
\end{aligned}
$$

- $P(G_{0})$: Probability of having no copies of the gene.
- $P(G_{1})$: Probability of having one copy of the gene.
- $P(G_{2})$: Probability of having two copies of the gene.

### $P(T|G_{n})$: Probabilities of having the trait, given that you have $n$ copies of the gene

$$
\begin{aligned}
&P(T|G_{0}) = 1\\% = 0.01\\
&P(\lnot T|G_{0}) = 1 - P(T|G_{0})\\
&P(\lnot T|G_{0}) = 0.99\\
&\\
&P(T|G_{1}) = 56\\% = 0.56\\
&P(\lnot T|G_{1}) = 1 - P(T|G_{1})\\
&P(\lnot T|G_{1}) = 0.44\\
&\\
&P(T|G_{2}) = 65\\% = 0.65\\
&P(\lnot T|G_{2}) = 1 - P(T|G_{2})\\
&P(\lnot T|G_{2}) = 0.35\\
\end{aligned}
$$

- $P(T|G_{0})$: Probability of having the trait, given that you have no copies of the gene.
- $P(\lnot T|G_{0})$: Probability of not having the trait, given that you have no copies of the gene.
- $P(T|G_{1})$: Probability of having the trait, given that you have one copy of the gene.
- $P(\lnot T|G_{1})$: Probability of not having the trait, given that you have one copy of the gene.
- $P(T|G_{2})$: Probability of having the trait, given that you have two copies of the gene.
- $P(\lnot T|G_{2})$: Probability of not having the trait, given that you have two copies of the gene.

### $P(T)$: Probability of having the trait

$$
\begin{aligned}
&* P(T) = \sum_{i} P(G_{i})P(T|G_{i})\\
&P(T) = P(G_{0})P(T|G_{0}) + P(G_{1})P(T|G_{1}) + P(G_{2})P(T|G_{2})\\
&P(T) = 0.96 \times 0.01 + 0.03 \times 0.56 + 0.01 \times 0.65\\
&P(T) = 0.0329\\
\end{aligned}
$$

- $P(T)$: Probability of having the trait.

### $P(G_{n}|T)$: Probabilities of having $n$ copies of the gene, given that you have the trait

$$
\begin{aligned}
&* P(G_{n}|T) = \frac{P(T|G_{n})P(G_{n})}{\sum_{i} P(G_{i})P(T|G_{i})} = \frac{P(T|G_{n})P(G_{n})}{P(T)}\\
&\\
&P(G_{0}|T) = \frac{P(T|G_{0})P(G_{0})}{P(T)} = \frac{0.01 \times 0.96}{0.0329}\\
&P(G_{0}|T) = 0.2918\\
&\\
&P(G_{1}|T) = \frac{P(T|G_{1})P(G_{1})}{P(T)} = \frac{0.56 \times 0.03}{0.0329}\\
&P(G_{1}|T) = 0.5106\\
&\\
&P(G_{2}|T) = \frac{P(T|G_{2})P(G_{2})}{P(T)} = \frac{0.65 \times 0.01}{0.0329}\\
&P(G_{2}|T) = 0.1976\\
\end{aligned}
$$

- $P(G_{0}|T)$: Probability of having no copies of the gene, given that you have the trait.
- $P(G_{1}|T)$: Probability of having one copy of the gene, given that you have the trait.
- $P(G_{2}|T)$: Probability of having two copies of the gene, given that you have the trait.

### $P(M)$: Probability of a gene mutating

$$
\begin{aligned}
&P(M) = 1\\% = 0.01\\
&P(\lnot M) = 1 - P(M)\\
&P(\lnot M) = 0.99\\
\end{aligned}
$$

- $P(M)$: Probability of a gene mutating.
- $P(\lnot M)$: Probability of a gene not mutating.

### $P(M|G_{n})$: Probabilities of a gene mutating, given that you have $n$ copies of the gene

$$
\begin{aligned}
&P(M|G_{0}) = P(M)\\
&P(M|G_{0}) = 0.01\\
&\\
&P(M|G_{1}) = \frac{1}{2} = 0.5\\
&\\
&P(M|G_{2}) = P(\lnot M)\\
&P(M|G_{2}) = 0.99\\
\end{aligned}
$$

- $P(M|G_{0})$: Probability of a gene mutating, given that you have no copies of the gene.
- $P(M|G_{1})$: Probability of a gene mutating, given that you have one copy of the gene.
- $P(M|G_{2})$: Probability of a gene mutating, given that you have two copies of the gene.

### Example

Consider the probability that:

1. Lily (mother) has 0 copies of the gene and does not have the trait.

$$
\begin{aligned}
&P(\lnot T|G_{0}) = \frac{P(\lnot T \cap G_{0})}{P(G_{0})}\\
&\\
&P(\lnot T \cap G_{0}) = P(G_{0})P(\lnot T|G_{0})\\
&P(\lnot T \cap G_{0}) = 0.96 \times 0.99\\
&\boxed{P(\lnot T \cap G_{0}) = 0.9504}\\
\end{aligned}
$$

2. James (father) has 2 copies of the gene and has the trait.

$$
\begin{aligned}
&P(T|G_{2}) = \frac{P(T \cap G_{2})}{P(G_{2})}\\
&\\
&P(T \cap G_{2}) = P(G_{2})P(T|G_{2})\\
&P(T \cap G_{2}) = 0.01 \times 0.65\\
&\boxed{P(T \cap G_{2}) = 0.0065}\\
\end{aligned}
$$

3. Harry (son) has 1 copy of the gene and does not have the trait.

There are two ways for this to happen. Either he gets the gene from his mother and not from his father, or he gets the gene from his father and not from his mother.

His mother, Lily, has 0 copies of the gene, so the only way to get the gene from his mother is if it mutates with probability $P(M|G_{0})$.

$$
\begin{aligned}
&P(Mother) = P(M|G_{0})\\
&P(Mother) = 0.01\\
&\\
&P(\lnot Mother) = 1 - P(Mother)\\
&P(\lnot Mother) = 0.99\\
\end{aligned}
$$

- $P(Mother)$: Probability of getting the gene from his mother.
- $P(\lnot Mother)$: Probability of not getting the gene from his mother.

His father, James, has 2 copies of the gene, so he will get the gene from his father with probability $P(M|G_{2})$.

$$
\begin{aligned}
&P(Father) = P(M|G_{2})\\
&P(Father) = 0.99\\
&\\
&P(\lnot Father) = 1 - P(Father)\\
&P(\lnot Father) = 0.01\\
\end{aligned}
$$

- $P(Father)$: Probability of getting the gene from his father.
- $P(\lnot Father)$: Probability of not getting the gene from his father.

$$
\begin{aligned}
&* P(G_{0}) = P(\lnot Mother) \times P(\lnot Father)\\
&* P(G_{1}) = P(Mother) \times P(\lnot Father) + P(Father) \times P(\lnot Mother)\\
&* P(G_{2}) = P(Mother) \times P(Father)\\
&\\
&P(G_{1}) = P(Mother) \times P(\lnot Father) + P(Father) \times P(\lnot Mother)\\
&P(G_{1}) = 0.01 \times 0.01 + 0.99 \times 0.99\\
&\boxed{P(G_{1}) = 0.9802}\\
&\\
&P(\lnot T|G_{1}) = \frac{P(\lnot T \cap G_{1})}{P(G_{1})}\\
&\\
&P(\lnot T \cap G_{1}) = P(G_{1})P(\lnot T|G_{1})\\
&P(\lnot T \cap G_{1}) = 0.9802 \times 0.44\\
&\boxed{P(\lnot T \cap G_{1}) = 0.431288}\\
\end{aligned}
$$

Calculate the joint probability.

$$
\begin{aligned}
&P(J) = P(\lnot T \cap G_{0}) + P(T \cap G_{2}) + P(\lnot T \cap G_{1})\\
&P(J) = 0.9504 + 0.0065 + 0.431288\\
&\boxed{P(J) = 0.0026643247488}\\
\end{aligned}
$$

## References
- [CS50’s Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/2024/)
