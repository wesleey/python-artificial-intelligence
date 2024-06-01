import sys
import os
import re
import random


DAMPING = 0.85
SAMPLES = 10000
ACCURACY = 0.001


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")

    corpus = crawl(sys.argv[1])

    print(f"Results from Sampling (n = {SAMPLES})")
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    for page in sorted(ranks, key=ranks.get, reverse=True):
        print(f"  {page}: {ranks[page]:.4f}")

    print("Results from Iteration")
    ranks = iterate_pagerank(corpus, DAMPING, ACCURACY)
    for page in sorted(ranks, key=ranks.get, reverse=True):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory: str) -> dict:
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            with open(os.path.join(directory, filename)) as file:
                contents = file.read()
                links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
                pages[filename] = set(links) - {filename}

    for filename in pages:
        pages[filename] = set(link for link in pages[filename] if link in pages)

    return pages


def transition_model(corpus: dict, page: str, damping_factor: float) -> dict:
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    distribution = dict()

    links = corpus[page]
    num_pages = len(corpus)

    if not links:
        for link in corpus:
            distribution[link] = 1 / num_pages
    else:
        num_links = len(links)
        for link in corpus:
            distribution[link] = (1 - damping_factor) / num_pages
            if link in links:
                distribution[link] += damping_factor / num_links

    return distribution


def sample_pagerank(corpus: dict, damping_factor: float, n: int) -> dict:
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pagerank = {page: 0 for page in corpus}
    pages = list(pagerank.keys())

    sample = random.choice(pages)
    pagerank[sample] += 1

    for _ in range(n):
        distribution = transition_model(corpus, sample, damping_factor)
        samples = list(distribution.keys())
        weights = list(distribution.values())
        sample = random.choices(samples, weights, k=1)[0]
        pagerank[sample] += 1

    for page in pagerank:
        pagerank[page] /= n

    return pagerank


def iterate_pagerank(corpus: dict, damping_factor: float, accuracy: float) -> dict:
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    num_pages = len(corpus)
    old_dict = {page: 1 / num_pages for page in corpus}
    new_dict = dict()

    while True:
        for page in corpus:
            result = 0
            for i in corpus:
                links = corpus[i]
                if not links:
                    result += old_dict[i] / num_pages
                elif page in links:
                    num_links = len(links)
                    result += old_dict[i] / num_links
            result *= damping_factor
            result += (1 - damping_factor) / num_pages
            new_dict[page] = result

        difference = max([abs(old_dict[i] - new_dict[i]) for i in old_dict])

        if difference < accuracy:
            break
        else:
            old_dict = new_dict.copy()

    return old_dict


if __name__ == "__main__":
    main()
