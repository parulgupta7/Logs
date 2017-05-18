import psycopg2

# Fuction to return psycopg2 connection
def connection(database_name="news"):
    try:
        name = 'news'
        db = psycopg2.connect('dbname={}'.format(name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("Error: cannot connect")

# Function to find the most popular article authors of all time
def top_authors():
    session, cursor = connection()
    q = """SELECT authors.name,
        (SELECT SUM(views) FROM author_view2 WHERE
        author_view2.id = authors.id) FROM authors;"""
    cursor.execute(q);
    result = cursor.fetchall()
    session.close()
    cursor.close()
    for i in range(0, len(result), 1):
        print result[i][0] + ": " + str(result[i][1]) + ' views'

# Funtion to find error requests
def Error():
    session, cursor = connection()
    q = """SELECT * FROM error_view3
           WHERE error_percent >= 1.0"""
    cursor.execute(q)
    result = cursor.fetchall()
    session.close()
    for i in range(0, len(result), 1):
        print str(result[i][0]) + " " + str(result[i][1]) + "%"

# Function to find top 3 articles
def top3_articles():
    session, cursor = connection()
    q = """SELECT title, count(title) AS count FROM log, articles
        WHERE path = CONCAT('/article/', articles.slug)
        GROUP BY title ORDER BY count DESC;"""
    cursor.execute(q)
    result = cursor.fetchall()
    session.close()
    cursor.close()
    print "Top 3 popular articles are:\n"
    for i in range(0, 3, 1):
        print result[i][0]+"->"+ str(result[i][1])




print"\n"
top3_articles()
print"\n"
top_authors()
print"\n"
Error()
print"\n"


