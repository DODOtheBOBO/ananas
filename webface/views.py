#!/usr/bin/env python3
# Soubor: views.py
# Úloha:  Flask --- pohledy
############################################################################
from flask import (render_template, Markup, request,
                   redirect, session)
from webface import app
############################################################################


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/super/')
def super():
    text = "Dnes je máme programování, což mi udělalo velikou radost :-)"
    return render_template('super.html', text=text)


@app.route('/number/<i>')
def number(i):
    return render_template('number.html', number=i)


@app.errorhandler(404)
def page_not_found(error):
    print(error.code)
    print(error.name)
    print(error.description)
    return render_template('404.html', e=error), 404

@app.route('/login/', methods=['POST'])
def login_post():
    jmeno = request.form.get('jmeno')
    heslo = request.form.get('heslo')
    next = request.args.get('next')        
    if  check_password_hash(str(pwhash.get(jmeno)),heslo):
        session['jmeno'] = jmeno
        flash('Úspěšně jsi se přihlásil.', 'zelena')
        return redirect(next or url_for('login'))
    else:
        flash('chybné jméno nebo heslo', 'cervena')
        if next:
            return redirect(url_for('login', next=next))
        else:
            return redirect(url_for('login'))

@app.route('/login/', methods=['GET'])
def login_get():
    return render_template('login.html')

@app.route('/logout/', methods=['GET'])
def logout():
    session.pop('jmeno', None)
    return redirect(url_for('login'))
