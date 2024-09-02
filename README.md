# URL Shortener

## Description
The URL Shortener is a simple Python-based web application that allows users to convert long URLs into shorter, more manageable links. Users input a long URL, and the application generates a unique shortened URL. When the shortened URL is accessed, the user is redirected to the original long URL.

This project is built using the Flask web framework and SQLite for database storage. The application provides a minimal user interface where users can input URLs and see the shortened link.

## Features
- **Shorten URLs:** Converts long URLs into short, unique links.
- **URL Redirection:** Redirects the user to the original URL when they access the shortened link.
- **Database Storage:** Stores URL mappings in a SQLite database.
- **Simple UI:** Provides a basic web interface for URL input and display of shortened URLs.

## Project Structure
The project is organized as follows:
```
url-shortener/ 
├── url-shortener-env/  
├── app.py 
├── templates/ 
│ └── index.html  
├── static/ 
│ └── css/ 
│   └── styles.css  
└── url_shortener.db 
```

## Requirements
- Python 3.x
- Flask
- SQLite (built-in with Python)

## Setup Instructions
### 1. Clone the Repository
```bash
git clone <repository-url>
cd url-shortener
```
### 2. Create a Virtual Environment
```bash
python3 -m venv url-shortener-env
```
### 3. Activate the Virtual Environment
- **On macOS/Linux:**
```bash
source url-shortener-env/bin/activate
```
- **On Windows:**
```bash
url-shortener-env\Scripts\activate
```
### 4. Install Dependencies
```bash
pip install Flask
```
### 5. Run the Application
```bash
python app.py
```
The application will be accessible at http://127.0.0.1:5000/.

## How It Works
- **User Input:** The user inputs a long URL into the form on the homepage.
- **Short URL Generation:** The application generates a random 6-character string as the shortened URL.
- **Database Storage:** The original URL and its corresponding shortened URL are stored in an SQLite database.
- **Redirection:** When the shortened URL is visited, the application retrieves the original URL from the database and redirects the user.

## Example
- **User enters:** https://example.com/some/very/long/url
- **Application generates:** http://127.0.0.1:5000/abc123
- When the user visits http://127.0.0.1:5000/abc123, they are redirected to https://example.com/some/very/long/url.