# Plagiarism Detection Tool

A modular Python-based plagiarism detection tool that implements various text similarity metrics.

## Features

- Text preprocessing and cleaning
- N-gram based comparison
- Multiple similarity metrics:
  - Jaccard Similarity
  - Containment Measure
- Modular and extensible design

## Project Structure

```
src/
├── text_preprocessor.py    # Text cleaning and tokenization
├── ngram_generator.py      # N-gram generation utilities
├── similarity_metrics.py   # Similarity calculation methods
├── plagiarism_detector.py  # Main detector class
└── main.py                # Example usage

tests/
└── test_plagiarism_detector.py  # Unit tests
```

## Usage

```python
from plagiarism_detector import PlagiarismDetector

# Initialize detector
detector = PlagiarismDetector(ngram_size=3)

# Compare texts
results = detector.compare_texts(text1, text2)

# Access results
jaccard_score = results['jaccard_similarity']
containment_score = results['containment_measure']
```

## Running Tests

```bash
python -m unittest tests/test_plagiarism_detector.py
```

## How it Works

1. **Text Preprocessing**:
   - Converts text to lowercase
   - Removes special characters
   - Tokenizes into words

2. **N-gram Generation**:
   - Creates n-grams from tokens
   - Helps capture phrase-level similarities

3. **Similarity Metrics**:
   - Jaccard Similarity: Measures overlap between texts
   - Containment Measure: Handles different-sized texts

## Extending the Tool

To add new similarity metrics:
1. Add new metric functions in `similarity_metrics.py`
2. Update the `compare_texts` method in `PlagiarismDetector`