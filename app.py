## IMPORTAR PAQUETES ##

import psycopg2

from flask import Flask, render_template, abort, request,session
import os, json, requests

app = Flask(__name__)


## Rutas

@app.route('/',methods=["GET"])
def inicio():
	return render_template("index.html")

@app.route('/consulta',methods=["POST"])
def consulta():
	ip= request.form.get("ip")
	bbdd= request.form.get("bbdd")
	user= request.form.get("user")
	passw= request.form.get("passw")
	conexion= psycopg2.connect(host=ip,user=user,database=bbdd,password=passw)
	cur= conexion.cursor()

	## Extraer datos ##

	cur.execute('Select * from empleados;')
	lista= cur.fetchall()
	listado=[]
	cur.close()
	for i in lista:
		diccionario={}
		diccionario["dni"]=i[0]
		diccionario["nombre"]=i[1]
		diccionario["apellidos"]=i[2]
		diccionario["salario"]=i[3]
		diccionario["id_dept"]=i[4]
		listado.append(diccionario)

	return render_template("consulta.html",listado=listado)

app.run('0.0.0.0',debug=True)