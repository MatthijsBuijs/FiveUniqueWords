"""Finds lists of five words with unique letters
    """
import time
import numpy as np

five_words = np.array([])
tic = time.perf_counter()
with open('words_alpha.txt', 'r', encoding='utf-8') as file:
    pass
toc = time.perf_counter()

print(f"Found {len(five_words)} sets of five words within {toc-tic:0.4f} seconds")