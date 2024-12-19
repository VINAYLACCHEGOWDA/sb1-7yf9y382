"""
Main plagiarism detection module.
"""
from typing import Dict, Tuple

from src.text_preprocessor import clean_text, tokenize
from src.ngram_generator import generate_ngrams
from src.similarity_metrics import jaccard_similarity, containment_measure

class PlagiarismDetector:
    def __init__(self, ngram_size: int = 3):
        self.ngram_size = ngram_size

    def prepare_text(self, text: str) -> set:
        """Prepare text for comparison by cleaning, tokenizing, and generating n-grams."""
        cleaned_text = clean_text(text)
        tokens = tokenize(cleaned_text)
        return generate_ngrams(tokens, self.ngram_size)

    def compare_texts(self, text1: str, text2: str) -> Dict[str, float]:
        """Compare two texts and return similarity scores."""
        ngrams1 = self.prepare_text(text1)
        ngrams2 = self.prepare_text(text2)

        return {
            'jaccard_similarity': jaccard_similarity(ngrams1, ngrams2),
            'containment_measure': containment_measure(ngrams1, ngrams2)
        }