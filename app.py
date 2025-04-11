from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv

load_dotenv()  # Memuat variabel dari .env jika diperlukan

app = Flask(__name__)
app.secret_key = 'supersecret'  # Untuk menggunakan flash messages

# ====================
# ROUTING HALAMAN HTML
# ====================

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/policy")
def policy():
    return render_template("policy.html")

@app.route("/articles")
def articles():
    return render_template("articles.html")

@app.route("/writings")
def writings():
    return render_template("writings.html")

@app.route("/biodiesel")
def biodiesel():
    return render_template("biodiesel.html")

@app.route("/training")
def training():
    return render_template("training.html")

@app.route("/consulting")
def consulting():
    return render_template("consulting.html")

# ================
# FORM KONTAK
# ================

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        nama = request.form.get('nama')
        email = request.form.get('email')
        telepon = request.form.get('telepon')
        layanan = request.form.get('layanan')
        pesan = request.form.get('pesan')

        print("Pesan masuk dari:", nama, email, layanan)
        print("Isi pesan:", pesan)

        flash("Terima kasih, pesan Anda telah dikirim!", "success")
        return redirect(url_for('contact'))

    return render_template("contact.html")

# ====================
# JALANKAN APLIKASI
# ====================
if __name__ == "__main__":
    app.run(debug=False)
