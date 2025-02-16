import re
import random
from syllapy import count

def estimate_syllables(word):
    """
    Estimates syllables in a word as a backup when syllapy is incorrect.
    - Uses vowel groupings to estimate.
    """
    word = word.lower()
    word = re.sub(r"[^a-z]", "", word)  # Remove punctuation
    vowels = "aeiouy"
    syllable_count = sum(1 for i in range(len(word)) if word[i] in vowels and (i == 0 or word[i-1] not in vowels))

    return max(syllable_count, 1)  # Ensure at least 1 syllable per word

def count_syllables(sentence):
    """Counts syllables in a sentence more accurately by using both syllapy and heuristics."""
    
    #  Remove punctuation
    sentence = re.sub(r"[^\w\s]", "", sentence)

    # Split into words
    words = sentence.split()

    # Limit to first 6 words (avoids overcounting in long headlines)
    words = words[:6]

    # Filter out very long words (which may inflate syllables)
    words = [word for word in words if len(word) < 10]

    #  Use both syllapy and heuristic backup
    total_syllables = sum(count(word) if count(word) > 0 else estimate_syllables(word) for word in words)

    # Debugging Output
    print(f"DEBUG: '{sentence}' (Limited to: {' '.join(words)}) counted {total_syllables} syllables.")

    return total_syllables

def construct_haiku(headlines):
    """Creates a haiku from news headlines with flexible syllable matching."""
    
    five_syllable_lines = []
    seven_syllable_lines = []

    for line in headlines:
        syllable_count = count_syllables(line)

        if 4 <= syllable_count <= 6:  # Accept 4-6 syllables for 5-syllable lines
            five_syllable_lines.append(line)
        elif 6 <= syllable_count <= 8:  # Accept 6-8 syllables for 7-syllable lines
            seven_syllable_lines.append(line)

    if len(five_syllable_lines) < 2 or len(seven_syllable_lines) < 1:
        return "❌ Not enough headlines to form a haiku today."

    line1 = random.choice(five_syllable_lines)
    line2 = random.choice(seven_syllable_lines)
    line3 = random.choice(five_syllable_lines)
    
    return f"{line1}\n{line2}\n{line3}"


