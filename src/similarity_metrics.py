"""
Different similarity metrics for text comparison.
"""
from typing import Set

def jaccard_similarity(set1: Set[str], set2: Set[str]) -> float:
    """Calculate Jaccard similarity between two sets."""
    if not set1 or not set2:
        return 0.0
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union

def containment_measure(set1: Set[str], set2: Set[str]) -> float:
    """Calculate containment measure (useful for different-sized texts)."""
    if not set1 or not set2:
        return 0.0
    intersection = len(set1.intersection(set2))
    return intersection / len(set1)