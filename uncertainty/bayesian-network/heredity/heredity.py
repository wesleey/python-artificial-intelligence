import sys
import csv
import itertools

from typing import Dict, List, Set

P = {
    "G": {
        0: {True: 0.96, False: 0.04},
        1: {True: 0.03, False: 0.97},
        2: {True: 0.01, False: 0.99}
    },
    "T|G": {
        0: {True: 0.01, False: 0.99},
        2: {True: 0.65, False: 0.35},
        1: {True: 0.56, False: 0.44}
    },
    "M": {
        True: 0.01,
        False: 0.99
    },
    "M|G": {
        0: {True: 0.01, False: 0.99},
        1: {True: 0.5, False: 0.5},
        2: {True: 0.99, False: 0.01}
    }
}


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])
    probabilities = initialize_probabilities(people)
    calculate_probabilities(people, probabilities)
    print_probabilities(people, probabilities)


def load_data(filename: str) -> Dict[str, dict]:
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def initialize_probabilities(people: dict) -> Dict[str, dict]:
    return {
        person: {
            "gene": {
                0: 0,
                1: 0,
                2: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }


def calculate_probabilities(people: dict, probabilities: dict) -> None:
    """
    Calculate the probabilities for each person having a gene and/or trait.
    """
    names = set(people)
    for have_trait in powerset(names):
        # Check if current set of people violates known information
        if evidence_violated(people, have_trait):
            continue
        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):
                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)
    # Ensure probabilities sum to 1
    normalize(probabilities)


def powerset(s: Set[str]) -> List[Set[str]]:
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def evidence_violated(people: dict, trait: set) -> bool:
    """
    Check if the current set of people with the trait violates known information.
    """
    return any(people[person]["trait"] != (person in trait)
               for person in people
               if people[person]["trait"] is not None)


def joint_probability(people: dict, one_gene: set, two_genes: set, trait: set) -> float:
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    probability = 1

    for person in people:
        num_genes = 1 if person in one_gene else 2 if person in two_genes else 0
        have_trait = True if person in trait else False

        mother = people[person]["mother"]
        father = people[person]["father"]

        if not mother and not father:
            probability *= P["G"][num_genes][True] * P["T|G"][num_genes][have_trait]
        else:
            parents = dict()
            for parent in [mother, father]:
                n_genes = 2 if parent in two_genes else 1 if parent in one_gene else 0
                parents[parent] = P["M|G"][n_genes]

            if num_genes == 0:
                probability *= parents[mother][False] * parents[father][False]
            elif num_genes == 1:
                probability *= (
                    parents[mother][True] * parents[father][False] +
                    parents[father][True] * parents[mother][False]
                )
            else:
                probability *= parents[mother][True] * parents[mother][True]

            probability *= P["T|G"][num_genes][have_trait]

    return probability


def update(probabilities: dict, one_gene: set, two_genes: set, trait: set, p: float):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    for person in probabilities:
        num_genes = 1 if person in one_gene else 2 if person in two_genes else 0
        probabilities[person]["gene"][num_genes] += p
        probabilities[person]["trait"][person in trait] += p


def normalize(probabilities: dict) -> None:
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    for person in probabilities.copy():
        for field in probabilities[person]:
            total = sum(probabilities[person][field].values())
            for value in probabilities[person][field]:
                normalized = probabilities[person][field][value] / total
                probabilities[person][field][value] = normalized


def print_probabilities(people: dict, probabilities: dict) -> None:
    for person in people:
        print(person)
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


if __name__ == "__main__":
    main()
