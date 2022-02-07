from flask import Flask, render_template, request, redirect, session

app = Flask( __name__ )
app.secret_key = "estoessecreto"

listaUsuarios = []

#1 ruta lista falta en el html
@app.route( '/', methods=['GET'] )
def despliegaDojoSurvey():
    return render_template( "index.html" )

#2 ruta lista falta results.html
@app.route( '/results', methods=["GET"] )
def despliegaDashboard():
    if 'nombre' in session:
        return render_template( "results.html", usuarios=listaUsuarios )
    else:
        return redirect( '/' )

#1A listo falta en la seccion index html
@app.route( '/encuesta', methods=["POST"] )
def encuesta():
    nuevoUsuario = {
        "nombre" : request.form["nombre"],
        "locacion" : request.form["locacion"],
        "language" : request.form["language"],
        "comentario" : request.form["comentario"]
    }
    session["nombre"] = request.form["nombre"]
    session["language"] = request.form["language"]
    listaUsuarios.append( nuevoUsuario )
    return redirect( '/results' )

#2A ruta lista falta results.html
@app.route( '/logout', methods=["GET"] )
def logoutUsuario():
    session.clear()
    listaUsuarios.clear()
    return redirect( '/' )

if __name__ == "__main__":
    app.run( debug = True )