import mariadb
import dbconnect
import traceback



def add_new_post():
    conn = dbconnect.db_connection()
    cursor = dbconnect.db_cursor(conn)
    if(conn == None or cursor == None):
        print("error in database connection")
        dbconnect.close_db_cursor(cursor)
        dbconnect.close_db_connection(conn)
        return
    try:
        # this is my code for entering a new post into db %s means value we enter will be a string.
        add_post = input('post: ')
        cursor.execute('INSERT INTO blog_post (username, content) VALUES(%s, %s)',(username, add_post))
        conn.commit()
    except:
        print("Something went wrong inserting adding new post")
        traceback.print_exc()    
        dbconnect.close_db_cursor(cursor)
        dbconnect.close_db_connection(conn)

def see_all_posts():
    conn = dbconnect.db_connection()
    cursor = dbconnect.db_cursor(conn)
    if(conn == None or cursor == None):
        print("error in database connection")
        dbconnect.close_db_cursor(cursor)
        dbconnect.close_db_connection(conn)
        return
    try:
        # this try executes the sql to grab all from blog posts names and content
        cursor.execute("SELECT * FROM blog_post")
        my_result = cursor.fetchall()
        for x in my_result:
            print(x[1])
            print(x[2])
    except:
        print("Something went wrong trying to view all blogs")
        traceback.print_exc()    
        dbconnect.close_db_cursor(cursor)
        dbconnect.close_db_connection(conn)

# this is the selection process of choosing what selection the user wants to make between choosing between both functions
username = input('enter username: ')
selection = input('selection: ')
# had to transfer strings to ints this took me a very long time to figure out kept having problems because i accidentally had my loop set in strings and not int print(x[1])
selection = int(float(selection))
# the if and elif statements are what call the functions after user choses
if(selection == 1):
    add_new_post()
elif(selection == 2):
    see_all_posts()



