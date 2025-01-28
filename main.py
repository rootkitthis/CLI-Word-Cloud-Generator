#imports libraries
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import re

#Important file paths stored as variables
#note: change file paths to location of file paths locally on your machine
file_path = 'words.txt'
excluded_file_path = 'excluded.txt'

#function that reads a text file and returns a list of words and stores it in the variable words
def ReadSourceWords(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()

    words = re.findall(r'\b\w+\b', text)
    return words

#funtion that reads excluded.txt and returns the list of words and stores it in the variable ExcludedWords
def ReadExcludedWords(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()
    ExcludedWords = re.findall(r'\b\w+\b', text)
    return ExcludedWords

# Function to filter out words to be excluded and stores it in the variable filtered_words
def FilterWords(word_list, exclude_words):
    filtered_words = []
    for word in word_list:
        if word not in exclude_words:
            filtered_words.append(word)
    return filtered_words


#Main Logic
def main():
    WordList = ReadSourceWords(file_path)
    ExcludeList = ReadExcludedWords(excluded_file_path)
    FilteredWords = FilterWords(WordList, ExcludeList)

    # Creates word cloud using using frequency of word counted
    WordCounts = Counter(FilteredWords)
    wordcloud = WordCloud(
        width=1000,
        height=500,
        background_color='white',
        max_font_size=100,
        #colormap= 'winter',
    ).generate_from_frequencies(WordCounts)

    # generates the word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    main()