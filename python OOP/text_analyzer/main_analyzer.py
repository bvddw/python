"""
Program that parses a text file containing news headlines and calculates the most and least frequently occurring words.
"""

from TextAnalyzer import TextAnalyzer

analyzer = TextAnalyzer('news.txt')
analyzer.load_text()
analyzer.count_words()
top_words = analyzer.get_top_words()
bottom_words = analyzer.get_bottom_words()
print(f"The most common words: {', '.join(top_words)}.")
print(f"The fewest words: {', '.join(bottom_words)}.")
