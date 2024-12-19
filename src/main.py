"""
Example usage of the plagiarism detector.
"""
from src.plagiarism_detector import PlagiarismDetector

def main():
    # Example texts
    original_text = """
    The quick brown fox jumps over the lazy dog.
    This is a simple example of text comparison.
    """
    
    suspicious_text = """
    The quick brown fox jumps over the lazy dog.
    This is an example showing text similarity.
    """

    # Initialize detector
    detector = PlagiarismDetector(ngram_size=3)
    
    # Compare texts
    results = detector.compare_texts(original_text, suspicious_text)
    
    # Print results
    print("\nPlagiarism Detection Results:")
    print("-" * 30)
    print(f"Jaccard Similarity: {results['jaccard_similarity']:.2%}")
    print(f"Containment Measure: {results['containment_measure']:.2%}")

if __name__ == "__main__":
    main()