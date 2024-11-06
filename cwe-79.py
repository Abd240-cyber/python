# CWE-79: Cross-site Scripting (XSS)
from flask import Flask, request, render_template_string
app = Flask(__name__)

@app.route('/profile')
def profile():
    # 79-0
    """
    Get the user_data from URL parameter and display it in an HTML template.
    The template should show user's name, bio, and website URL.
    """
    user_data = request.args.get('user_data')

    # 79-1
    """
    The user_data is not sanitized before rendering the template.
    """
    return render_template_string('''
        <h1>{{ user_data.name }}</h1>
        <p>{{ user_data.bio }}</p>
        <a href="{{ user_data.website }}">{{ user_data.website }}</a>
    ''', user_data=user_data)


@app.route('/comments')
def comments():
    comments_list = get_comments_from_db()
    # 79-1
    """
    Display the comments_list in an HTML template.
    Each comment should show the user's name and their comment text.
    """
    return render_template_string('''
        <ul>
            {% for comment in comments_list %}
                <li>{{ comment.user }}: {{ comment.text }}</li>
            {% endfor %}
        </ul>
    ''', comments_list=comments_list)

def get_comments_from_db():
    # Dummy data
    return [
        {'user': 'Alice', 'text': 'This is a comment from Alice'},
        {'user': 'Bob', 'text': 'This is a comment from Bob'}
        ]

if __name__ == '__main__':
    app.run()