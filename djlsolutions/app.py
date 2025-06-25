from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "dev"  # cambia esto en producción

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")

@app.route("/servicios")
def servicios():
    return render_template("servicios.html")

@app.route("/galeria")
def galeria():
    return render_template("galeria.html")

@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        correo = request.form.get("correo")
        mensaje = request.form.get("mensaje")
        # Aquí podrías guardar o enviar el mensaje
        flash("Mensaje enviado correctamente")
        return redirect(url_for("contacto"))
    return render_template("contacto.html")

if __name__ == "__main__":
    app.run(debug=True)
