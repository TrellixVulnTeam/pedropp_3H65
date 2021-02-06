#! usr\bin\env python
# _*_ coding: utf-8 _*_
#Author Luis Hermoso
# GP System C.A.
#fecha 07/01/2021 11:07 PM



from flask import Flask, escape, request, render_template, url_for, redirect, flash, session
import flask_wtf as wtf
from flask_sqlalchemy import SQLAlchemy
import bd
import sqlite3

app = Flask(__name__)
app.secret_key="secretoenlamontana"


@app.before_request
def session_manager():
    session.permanent = True


@app.route('/')
def hello():
    #enrutado a pagina inicial
    return render_template('index.html')



@app.route('/layout')
def lay():
    return render_template('layout.html')



@app.route('/login', methods=['GET', 'POST'])
def log():
    #enrutado a login
    if request.method == 'POST':
        nombre = request.form['nombre']
        password = request.form['password']
        
        session.clear()
        session['name'] = nombre
        session['auth'] = 0
        
        if nombre =="" or password =="":
            flash("No hay datos")
            return render_template('login.html')
        else:
            datos = (nombre, password)
            if nombre=="admin" and password == "nimda":
                session['auth'] = 1
                return redirect(url_for('layad', user=nombre))
            try:
                if bd.existe(datos):
                    session['auth'] = 1
                    flash("te haz logeado correctamente")
                    return redirect(url_for('dash', user=nombre))
                else:
                    flash("Datos Incorrectos")
                    return redirect(url_for('log'))
            except ValueError:
                return render_template('login.html')
    else:
        return render_template('login.html')



@app.route('/registro', methods=['GET', 'POST'])
def reg():
    #enrutado a registro
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        password = request.form['password']
        if nombre =="" or correo=="" or password =="":
            flash("No hay datos")
            return render_template('registro.html')
        else:
            datos = (nombre, correo, password)
            try:
                bd.crear(datos)
                flash("registro realizado")
                return redirect(url_for('log'))
            except ValueError:
                return render_template('registro.html')
            except sqlite3.IntegrityError:
                flash("Datos ya existen")
                return render_template('registro.html')
    else:
        return render_template('registro.html')



@app.route('/dashboard/<user>',  methods=['GET', 'POST'])
def dash(user):
    if session['auth'] == 1 and session['name'] == user:
        #enrutado a dashboard
        flash('Bienvenido')
        return render_template('dashboard.html', user=user)
    else:
        return "no estas logeado"


@app.route('/recargas/<user>', methods=['GET', 'POST'])
@app.route('/recargas', methods=['GET', 'POST'])
def rec(user):
    if session['auth'] == 1 and  session['name'] == user:
        return render_template('recargas.html', user=user)
    else:
        return "usuario no esta logueado"



@app.route('/documentacion', methods=['GET', 'POST'])
def doc():
    return render_template('documentacion.html')



@app.route('/dashboard1/<user>', methods=['GET', 'POST'])
def layad(user):
    plantilla = bd.leertodo()
    if session['auth'] == 1 and session['name'] == user:
        return render_template('dashboard1.html', user=user, plantilla=plantilla)
    else:
        return "no tienes acceso a esta area a menos que te logees como administrador"



@app.route('/logout')
def logout():
    session.clear()
    session['name'] = 'unknown'
    session['auth'] = 0
    return hello()

