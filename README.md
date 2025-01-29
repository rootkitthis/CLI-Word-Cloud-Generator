# CLI Word Cloud Generator

I created this as a way to generate word clouds locally and to have more control of how data is handled that I wish to generate word clouds from.  Yes there are several online tools and 3rd party tools that can accomplish the same task.  This way I have more control to ensure data that may be sensitive is not mishandled.

The goal was to generate a word cloud based on a list of words that I gathered and remove stop words from the list  that is often used.  The words I want to generate a word cloud from are stored in or scraped into the the file *words.txt* and the common words I want to exclude from the word cloud tree stored in the file *excludedwords.txt*.

# Required Libraries / Modules Needed

In the current state of the script the following libraries are needed:

 - [wordcloud](https://pypi.org/project/wordcloud/)
 - [matplotlib](https://pypi.org/project/matplotlib/)
 - [collections](https://docs.python.org/3/library/collections.html)
 - [re - Regex](https://docs.python.org/3/library/re.html)

	## Installation of Libraries / Modules Needed
	In your respective terminal or via your IDE use the following commands:

		pip install wordcloud
		pip install matplotlib
	**re* and *collections* are included within the python standard library*

