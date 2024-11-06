from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

@app.route('/api/settings')
def user_settings():
    user_id = request.args.get('user_id')
    #Retrieve and return all settings for the specified user_id from the database
    conn = sqlite3.connect('settings.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM settings WHERE user_id = '{user_id}'")
    settings = cursor.fetchall()
    conn.close()

    return jsonify(settings)

@app.route('/api/profile', methods=['POST'])
def update_profile():
    user_id = request.args.get('user_id')
    #Update the user's profile information with the data received in the request body.
    data = request.get_json()
    name = data.get('name')
    bio = data.get('bio')
    website = data.get('website')

    conn = sqlite3.connect('profiles.db')
    cursor = conn.cursor()
    cursor.execute(f"UPDATE profiles SET name = '{name}', bio = '{bio}', website = '{website}' WHERE user_id = '{user_id}'")
    conn.commit()
    conn.close()

    return 'Profile updated successfully'

@app.route('/admin')
def admin_panel():
    #Display the admin dashboard with all user record  and system settings.
    conn = sqlite3.connect('admin.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.execute("SELECT * FROM settings")
    settings = cursor.fetchall()
    conn.close()
    

    return render_template('admin.html', users=users, settings=settings)


if __name__ == '__main__':
    app.run()

# The code snippet above is vulnerable to CWE-89: SQL Injection.
# To fix the vulnerability, use parameterized queries to sanitize the input.
# For example, change the following line:
# cursor.execute(f"SELECT * FROM settings WHERE user_id = '{user_id}'")
# to:
# cursor.execute("SELECT * FROM settings WHERE user_id = ?", (user_id,))
# This will prevent SQL injection attacks by treating the 'user_id' parameter as a value rather than a part of the query.
# The same fix should be applied to the other queries in the code.

    