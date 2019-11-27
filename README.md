# python_lab2
Python 3.7.1.0 project for UNECON. RSS Reader
1. If any of the modules listed at the beginning of the code is not installed (for example, pyperclip or feedparser) - install it through cmd using pip in the scripts folder.
2. Run the file "data.py" - it is designed to create a db-file in which rss-channels will be written.
3. Run "rss.py" - a program will open consisting of a window with three buttons with inscriptions in English inside.
And now more about the insides:
1. After launch, we are horrified to find that the news window in the middle (oh, horror) is empty. Do not despair - this is due to the fact that the db file that we created is still empty. In order to fix this, we need to do the following:
2. Open the "Source Administration" tab and add some rss channel (for example, https://www.reddit.com/r/worldnews/.rss). After that we can climb on "Watch all" and watch how much news we have in the feed.
3. In addition, the program’s functionality includes searching for news by keywords ("Search at list" tab), deleting channels and copying their http-addresses.
