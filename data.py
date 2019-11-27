import sqlite3
links = sqlite3.connect("links.db")
cursor = links.cursor()
cursor.execute("""CREATE TABLE links
                  (adress text
                  )
               """)
