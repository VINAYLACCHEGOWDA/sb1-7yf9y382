"""
N-gram generation utilities for text comparison.
"""
from typing import List, Set

def generate_ngrams(tokens: List[str], n: int) -> Set[str]:
    """Generate n-grams from a list of tokens."""
    ngrams = set()
    for i in range(len(tokens) - n + 1):
        ngram = ' '.join(tokens[i:i + n])
        ngrams.add(ngram)
    return ngrams