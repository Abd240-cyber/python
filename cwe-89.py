# CWE-89: SQL Injection
import sqlite3
from flask import request

def get_user():
    username = request.args.get('username')
    conn = sqlite3.connect('users.db')
    
    #Query the users table to get all details of the user with the given username.
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    user = cursor.fetchone()
    conn.close()
    return user


def update_password():
    username = request.args.get('username')
    new_password = request.args.get('password')
    conn = sqlite3.connect('users.db')
    # 89-1
    
    #Update the password for the user with the given username in the users table
    cursor = conn.cursor()
    cursor.execute(f"UPDATE users SET password = '{new_password}' WHERE username = '{username}'")
    conn.commit()
    conn.close()

def search_users():
    search_term = request.args.get('search')
    conn = sqlite3.connect('users.db')
    #Delete all users from the database whose username matches the search term.
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM users WHERE username = '{search_term}'")
    conn.commit()
    conn.close()
   

if __name__ == '__main__':

    print(get_user())
# The code snippet above is vulnerable to CWE-89: SQL Injection.
# To fix the vulnerability, use parameterized queries to sanitize the input.
# For example, change the following line:
# cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
# to:
# cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
# This will prevent SQL injection attacks by treating the 'username' parameter as a value rather than a part of the query.
# The same fix should be applied to the other queries in the code.  

