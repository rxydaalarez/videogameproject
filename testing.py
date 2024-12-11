import re

def clean_punctuation(strings):
    """
    Cleans repeated punctuation from a list of strings.
    
    Args:
    strings (list): A list of strings to clean.
    
    Returns:
    list: A new list with cleaned strings.
    """
    cleaned_strings = []
    for s in strings:
        # Replace consecutive punctuation (e.g., ".." or ",,") with a single instance
        cleaned = re.sub(r'([.,!?;:])\1+', r'\1', s)
        cleaned = re.sub(r'\*\*\*', '', cleaned)
        # Optionally, you can add space normalization around punctuation
        cleaned = re.sub(r'\s*([.,!?;:])\s*', r'\1 ', cleaned).strip()
        cleaned_strings.append(cleaned)
    return cleaned_strings

print(clean_punctuation("Hi,, My name *** is Jeb.."))