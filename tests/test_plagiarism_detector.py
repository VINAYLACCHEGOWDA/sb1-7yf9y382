"""
Unit tests for the plagiarism detection system.
"""
import unittest
from src.text_preprocessor import clean_text, tokenize
from src.ngram_generator import generate_ngrams
from src.similarity_metrics import jaccard_similarity, containment_measure
from src.plagiarism_detector import PlagiarismDetector

class TestPlagiarismDetector(unittest.TestCase):
    def setUp(self):
        self.detector = PlagiarismDetector(ngram_size=3)

    def test_clean_text(self):
        text = "Hello, World!"
        cleaned = clean_text(text)
        self.assertEqual(cleaned, "hello world")

    def test_tokenize(self):
        text = "hello world"
        tokens = tokenize(text)
        self.assertEqual(tokens, ["hello", "world"])

    def test_generate_ngrams(self):
        tokens = ["the", "quick", "brown", "fox"]
        ngrams = generate_ngrams(tokens, 2)
        expected = {"the quick", "quick brown", "brown fox"}
        self.assertEqual(ngrams, expected)

    def test_identical_texts(self):
        text = "The quick brown fox"
        results = self.detector.compare_texts(text, text)
        self.assertEqual(results['jaccard_similarity'], 1.0)
        self.assertEqual(results['containment_measure'], 1.0)

    def test_different_texts(self):
        text1 = "The quick brown fox"
        text2 = "The lazy dog sleeps"
        results = self.detector.compare_texts(text1, text2)
        self.assertLess(results['jaccard_similarity'], 1.0)
        self.assertLess(results['containment_measure'], 1.0)

if __name__ == '__main__':
    unittest.main()