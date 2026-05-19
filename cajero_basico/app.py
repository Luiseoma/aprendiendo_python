from flask import Flask, request, session, redirect, url_for, flash, render_template
import json
import os

app = Flask(__name__)
app.secret_key = "clave_secreta_para_sesiones"

# ----------------------------
# JSON HELPERS
# ----------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USUARIOS_PATH = os.path.join(BASE_DIR, "usuarios.json")

def cargar_usuarios():
    if not os.path.exists(USUARIOS_PATH):
        return {}
    with open(USUARIOS_PATH, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}

def guardar_usuarios(usuarios):
    with open(USUARIOS_PATH, "w") as file:
        json.dump(usuarios, file, indent=4)


# ----------------------------
# LOGIN
# ----------------------------
@app.route('/', methods=['GET', 'POST'])
def login():

    if request.method == "POST":

        print("Leyendo desde:", USUARIOS_PATH)
        print("Archivo existe:", os.path.exists(USUARIOS_PATH))
        print("Usuarios cargados:", list(cargar_usuarios().keys()))

        usuario = request.form["usuario"].strip()
        password = request.form["password"].strip()

        usuarios_registrados = cargar_usuarios()

        if usuario not in usuarios_registrados:
            flash("Usuario no registrado")
            return redirect(url_for("login"))

        user = usuarios_registrados[usuario]

        # 🔧 Asegurar estructura ANTES de usar el usuario
        user.setdefault("password", "")
        user.setdefault("saldo", 0)
        user.setdefault("intentos", 0)
        user.setdefault("bloqueado", False)

        print("USUARIO:", usuario)
        print("INPUT PASSWORD:", password)
        print("PASSWORD JSON:", user.get("password"))
        print("MATCH:", user.get("password") == password)

        if user["bloqueado"]:
            flash("Usuario bloqueado")
            return redirect(url_for("login"))

        if user["password"].strip() == password:
            user["intentos"] = 0
            session["usuario"] = usuario
            guardar_usuarios(usuarios_registrados)
            return redirect(url_for("dashboard"))

        # Contraseña incorrecta
        user["intentos"] += 1
        if user["intentos"] >= 3:
            user["bloqueado"] = True
            flash("Usuario bloqueado por intentos fallidos")
        else:
            flash(f"Contraseña incorrecta ({3 - user['intentos']} intentos restantes)")

        guardar_usuarios(usuarios_registrados)
        return redirect(url_for("login"))

    return render_template("login.html")


# ----------------------------
# DASHBOARD
# ----------------------------
@app.route("/dashboard")
def dashboard():

    if "usuario" not in session:
        return redirect(url_for("login"))

    usuarios_registrados = cargar_usuarios()
    usuario = session["usuario"]

    return f"""
    <h1>Bienvenido, {usuario}!</h1>
    <h2>Tu saldo actual es: ${usuarios_registrados[usuario]['saldo']}.</h2>
    <a href="/retirar">Retirar Dinero</a><br>
    <a href="/logout">Cerrar Sesión</a>
    """


# ----------------------------
# RETIRO
# ----------------------------
@app.route("/retirar", methods=["GET", "POST"])
def retirar():

    if "usuario" not in session:
        return redirect(url_for("login"))

    usuarios_registrados = cargar_usuarios()
    usuario = session["usuario"]

    if request.method == "POST":

        monto = float(request.form["monto"])

        if monto <= 0:
            flash("El monto debe ser mayor a cero")
            return redirect(url_for("retirar"))

        if monto > usuarios_registrados[usuario]["saldo"]:
            flash("Fondos insuficientes")
            return redirect(url_for("retirar"))

        usuarios_registrados[usuario]["saldo"] -= monto
        guardar_usuarios(usuarios_registrados)

        return f"""
        <h1>Retiro exitoso</h1>
        <h2>Retiraste ${monto}</h2>
        <h2>Tu saldo actual es: ${usuarios_registrados[usuario]['saldo']}.</h2>
        <a href="/dashboard">Volver al menú principal</a>
        """

    return render_template("retirar.html")


# ----------------------------
# LOGOUT
# ----------------------------
@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("login"))


app.run(debug=True)
