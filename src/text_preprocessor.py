"""
Text preprocessing utilities for plagiarism detection.
"""
import re
from typing import List

def clean_text(text: str) -> str:
    """Remove special characters and convert to lowercase."""
    # Convert to lowercase and remove special characters
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

def tokenize(text: str) -> List[str]:
    """Split text into words."""
    return text.split()