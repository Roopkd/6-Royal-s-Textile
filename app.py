import sqlite3
from flask import Flask, flash, redirect, render_template, request, session, g

# Configure application
app = Flask(__name__)
app.secret_key = 'Roopkd8958@'

# Configure CS50 Library to use SQLite database
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('products.db')
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(error):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store'
    return response

@app.route("/")
def index():
    db = get_db()
    start_display = db.execute("SELECT DISTINCT start FROM products").fetchall()
    db.commit()
    return render_template("index.html", s_display=start_display)

@app.route("/size")
def size():
    product_choosed = request.args.get("product")
    db = get_db()
    size_display = db.execute("SELECT DISTINCT size FROM products WHERE start=?", (product_choosed,)).fetchall()
    session['product'] = product_choosed
    return render_template("size.html", size_display=size_display)

@app.route("/type")
def type():
    si = request.args.get("size")
    prod = session.get('product')
    db = get_db()
    type_display = db.execute("SELECT DISTINCT type FROM products WHERE start=? AND size=?", (prod, si)).fetchall()
    session['size'] = si
    return render_template("type.html", type_display=type_display)

@app.route("/product")
def product():
    produ = session.get('product')
    siz = session.get('size')
    typ = request.args.get("type")
    db = get_db()
    available = db.execute("SELECT id FROM products WHERE start=? AND size=? AND type=?", (produ, siz, typ)).fetchall()
    session['type'] = typ
    return render_template("available.html", available=available)

@app.route("/delete")
def delete():
    id_delete = request.args.get("delete")
    db = get_db()
    db.execute("DELETE FROM products WHERE id=?", (id_delete,))
    db.commit()
    produ = session.get('product')
    siz = session.get('size')
    typ = session.get('type')
    available = db.execute("SELECT id FROM products WHERE start=? AND size=? AND type=?", (produ, siz, typ)).fetchall()
    return render_template("available.html", available=available)

@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        product_to_save = request.form.get("textproduct")
        size_to_save = request.form.get("textsize")
        type_to_save = request.form.get("texttype")
        
        if not product_to_save or not size_to_save or not type_to_save:
            return redirect("/add")
        
        db = get_db()
        db.execute("INSERT INTO products (start, size, type) VALUES (?,?,?)", (product_to_save, size_to_save, type_to_save))
        db.commit()
        return redirect("/")
        
    elif request.method == "GET": 
        db = get_db()
        start = db.execute("SELECT DISTINCT start FROM products").fetchall()
        size = db.execute("SELECT DISTINCT size FROM products").fetchall()
        type = db.execute("SELECT DISTINCT type FROM products").fetchall()
        return render_template("add.html", starts=start, sizes=size, types=type)



if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
