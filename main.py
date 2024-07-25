from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import os
import json

app = Flask(__name__)

app.secret_key = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

# Page d'accueil
@app.route('/')
def home():
    return render_template('home_view.html')

# login page view
@app.route('/login_view')
def login_view():
    return render_template('login_view.html')

# REGISTER page view
@app.route('/user_regist_view')
def register_view():
    return render_template('user_regist_view.html')

# invalide credentials page view
@app.route('/invalid_credentials_view')
def invalid_credentials_view():
    return render_template('invalid_credential_view.html')

# Route pour la page d'inscription
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Charger les données existantes si le fichier existe, sinon initialiser une nouvelle liste
        if os.path.exists('users.json'):
            with open('users.json', 'r') as file:
                data = json.load(file)
        else:
            data = {'users': []}

        # Ajouter le nouvel utilisateur
        new_user = {
            'name': name,
            'email': email,
            'password': password
        }
        data['users'].append(new_user)

        # Enregistrer les données mises à jour
        with open('users.json', 'w') as file:
            json.dump(data, file, indent=4)

        return redirect(url_for('articles_list'))
    
    return render_template('user_regist_view.html')

# Route pour la page de connexion
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Charger les données existantes
        if os.path.exists('users.json'):
            with open('users.json', 'r') as file:
                data = json.load(file)
        else:
            data = {'users': []}

        # Vérifier les informations de connexion
        for user in data['users']:
            if user['email'] == email and user['password'] == password:
                session['user'] = user['name']
                return redirect(url_for('articles_list'))

        return render_template('invalid_credentials_view.html')

    return render_template('login_view.html')

# Route pour afficher la liste des articles
@app.route('/articles')
def articles_list():
    if os.path.exists('articles.json'):
        with open('articles.json', 'r') as file:
            articles_data = json.load(file)
    else:
        articles_data = {'articles': []}

    return render_template('articles_list.html', articles=articles_data['articles'])

# Route pour afficher les détails d'un article
@app.route('/article/<title>')
def article_detail(title):
    if os.path.exists('articles.json'):
        with open('articles.json', 'r') as file:
            articles_data = json.load(file)
    else:
        return "Article not found", 404

    for article in articles_data['articles']:
        if article['title'] == title:
            return render_template('article_detail.html', article=article)

    return "Article not found", 404

# Route pour gérer la déconnexion
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('role', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
