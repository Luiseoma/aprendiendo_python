from flask import Flask, request, session, redirect, url_for, flash

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
            
            return f"""
            <h1>Bienvenido {usuario} 😄</h1>
            
            <h2>Tu saldo actual es: ${usuarios_registrados[usuario]['saldo']}.</h2>
            
            <a href="/retirar">Retirar dinero</a>
            """
 
        
        else:
            flash("Usuario o contraseña incorrectos")
            return redirect(url_for("login"))
    

    return """
    <h1>Login Cajero</h1>

    <form method="POST">

        <input type="text" name="usuario" placeholder="Usuario">

        <br><br>

        <input type="password" name="contraseña" placeholder="Contraseña">

        <br><br>

        <button type="submit">Ingresar</button>

    </form>
    """

@app.route("/retirar", methods=["GET", "POST"])
def retirar():

    if "usuario" not in session:
        return "<h1>Debes iniciar sesión para acceder a esta página</h1>"
    
    usuario = session["usuario"]

    if request.method == "POST":
        monto = float(request.form["monto"])

        if monto <= 0:
            return redirect(url_for("retirar"))
        
        if monto > usuarios_registrados[usuario]["saldo"]:
            return redirect(url_for("retirar"))
        
        usuarios_registrados[usuario]["saldo"] -= monto

        return f"""
        <h1>Retiro exitoso</h1>
        <h2>Retiraste ${monto}</h2>
        <h2>Tu saldo actual es: ${usuarios_registrados[usuario]['saldo']}.</h2>
        <a href="/">Volver al menú principal</a>
        """
    
    return """
    <h1>Retirar Dinero</h1>

    <form method="POST">
        <input type="number" name="monto" placeholder="Monto a retirar">

        <br><br>

        <button type="submit">Retirar</button>
    </form>
    """

app.run(debug=True)


