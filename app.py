from flask import Flask, request, redirect, render_template
import sqlite3
import string, random

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('url_shortener.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS urls
                 (id INTEGER PRIMARY KEY, original_url TEXT, short_url TEXT)''')
    conn.commit()
    conn.close()

# Generate a random short URL
def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    return short_url

# Store URL mapping
def store_url_mapping(original_url, short_url):
    conn = sqlite3.connect('url_shortener.db')
    c = conn.cursor()
    c.execute("INSERT INTO urls (original_url, short_url) VALUES (?, ?)", (original_url, short_url))
    conn.commit()
    conn.close()

# Get original URL
def get_original_url(short_url):
    conn = sqlite3.connect('url_shortener.db')
    c = conn.cursor()
    c.execute("SELECT original_url FROM urls WHERE short_url = ?", (short_url,))
    result = c.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['url']
        short_url = generate_short_url()
        store_url_mapping(original_url, short_url)
        return render_template('index.html', short_url=short_url)
    return render_template('index.html')

@app.route('/<short_url>')
def redirect_to_url(short_url):
    original_url = get_original_url(short_url)
    if original_url:
        return redirect(original_url)
    else:
        return 'URL not found', 404

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
