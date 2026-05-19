from flask import Flask, request, session, redirect, url_for, flash
from flask import render_template

app = Flask(__name__)
app.secret_key = "clave_secreta_para_sesiones"

usuarios_registrados = {
    "Luis": {"contraseña": "luis1234", "saldo": 1000},
    "María": {"contraseña": "maria1234", "saldo": 1500},
    "Carlos": {"contraseña": "carlos1234", "saldo": 2000},
    "Ana": {"contraseña": "ana1234", "saldo": 1200},    
    "Pedro": {"contraseña": "pedro1234", "saldo": 1800},
    "Laura": {"contraseña": "laura1234", "saldo": 2500},
    "Jose": {"contraseña": "jose1234", "saldo": 5000},
}

@app.route('/', methods=['GET', 'POST'])
def login():

    if request.method == "POST":

        usuario = request.form["usuario"]
        contraseña = request.form["contraseña"]

        if usuario in usuarios_registrados and usuarios_registrados[usuario]["contraseña"] == contraseña:

            session["usuario"] = usuario
            
            return redirect(url_for("dashboard"))
 
        
        else:
            flash("Usuario o contraseña incorrectos")
            return redirect(url_for("login"))
    

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "usuario" not in session:
        return redirect(url_for("login"))
    
    usuario = session["usuario"]

    return f"""
    <h1>Bienvenido, {usuario}!</h1>
    <h2>Tu saldo actual es: ${usuarios_registrados[usuario]['saldo']}.</h2>
    <a href="/retirar">Retirar Dinero</a><br>
    <a href="/logout">Cerrar Sesión</a>
    """

@app.route("/retirar", methods=["GET", "POST"])
def retirar():

    if "usuario" not in session:
        return redirect(url_for("login"))
    
    usuario = session["usuario"]

    if request.method == "POST":
        monto = float(request.form["monto"])

        if monto <= 0:
            flash("El monto a retirar debe ser mayor a cero")
            return redirect(url_for("retirar")) 
        
        if monto > usuarios_registrados[usuario]["saldo"]:
            flash("Fondos insuficientes")
            return redirect(url_for("retirar"))
        
        usuarios_registrados[usuario]["saldo"] -= monto

        return f"""
        <h1>Retiro exitoso</h1>
        <h2>Retiraste ${monto}</h2>
        <h2>Tu saldo actual es: ${usuarios_registrados[usuario]['saldo']}.</h2>
        <a href="/dashboard">Volver al menú principal</a>
        """
    return render_template("retirar.html")

@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("login"))   

app.run(debug=True)


