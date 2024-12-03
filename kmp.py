import matplotlib.pyplot as plt
import numpy as np

def compute_lps(pattern):
    """
    Preprocess the pattern to compute the Longest Prefix Suffix (LPS) array.
    
    :param pattern: The pattern to search for.
    :return: LPS array.
    """
    m = len(pattern)
    lps = [0] * m  # LPS array initialization
    length = 0  # length of previous longest prefix suffix
    i = 1

    # Build the LPS array
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    """
    Perform KMP search to find the pattern in the given text.
    
    :param text: The text to search within.
    :param pattern: The pattern to search for.
    :return: List of start indices where the pattern is found in the text.
    """
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)  # Preprocess the pattern
    matches = []
    i = 0  # Index for text
    j = 0  # Index for pattern
    comparisons = []  # Store comparison counts for each step
    
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            comparisons.append((i, j))  # Track the progress of comparisons

        if j == m:
            # Found a match
            matches.append(i - j)
            j = lps[j - 1]

        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
        comparisons.append((i, j))  # Track the progress of comparisons
    
    return matches, comparisons

def plot_comparisons(comparisons):
    """
    Plot the comparison steps for KMP algorithm.
    
    :param comparisons: List of comparison progress during KMP search.
    """
    steps = np.arange(len(comparisons))
    text_comparisons = [c[0] for c in comparisons]
    pattern_comparisons = [c[1] for c in comparisons]

    plt.figure(figsize=(10, 6))
    plt.plot(steps, text_comparisons, label="Text Pointer", marker='o', color='blue')
    plt.plot(steps, pattern_comparisons, label="Pattern Pointer", marker='x', color='red')

    plt.title("Comparison Steps in KMP Algorithm")
    plt.xlabel("Step Number")
    plt.ylabel("Position in Text/Pattern")
    plt.legend()
    plt.grid(True)
    plt.show()

# Main function to demonstrate the algorithm
if __name__ == "__main__":
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    
    print(f"Text: {text}")
    print(f"Pattern: {pattern}")
    
    matches, comparisons = kmp_search(text, pattern)
    
    # Display matches
    if matches:
        print(f"Pattern found at positions: {matches}")
    else:
        print("Pattern not found in the text.")
    
    # Display comparison steps in terminal
    print(f"\nComparison Steps (Text, Pattern):")
    for step in comparisons:
        print(f"Text Index: {step[0]}, Pattern Index: {step[1]}")
    
    # Plot the comparisons
    plot_comparisons(comparisons)
