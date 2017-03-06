#
# Database access functions for the web forum.
# 

import time
import psycopg2
import bleach

## Database connection
# DB = []

## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    DB = psycopg2.connect("dbname=forum")
    c = DB.cursor()

    c.execute("UPDATE posts SET content = 'cheese' WHERE content LIKE '%spam%';")
    c.execute("DELETE FROM posts WHERE content LIKE 'cheese';")
    c.execute("SELECT time, content FROM posts ORDER BY time DESC")

    posts = [{'content': str(bleach.clean(row[1])), 'time': str(row[0])} for row in c.fetchall()]
    # posts.sort(key=lambda row: row['time'], reverse=True)
    DB.commit()
    DB.close()
    return posts

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    DB = psycopg2.connect("dbname=forum")
    c = DB.cursor()
    cleaned = bleach.clean(content)
    c.execute("INSERT INTO posts (content) VALUES (%s)", (cleaned,))

    DB.commit()
    DB.close()

    #t = time.strftime('%c', time.localtime())
    #DB.append((t, content))
