from flask import Flask, redirect, render_template, request, session
import database

# Configure application
app = Flask(__name__)
app.secret_key = 'Roopkd8958@'


@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store'
    return response

@app.route("/")
def index():
    data = database.querystart()
    return render_template("index.html", data=data)

@app.route("/size")
def size():
    product_choosed = request.args.get("product")
    size_data = database.querysize(product_choosed)
    session['product'] = product_choosed
    return render_template("size.html", size_data=size_data)

@app.route("/type")
def type():
    si = request.args.get("size")
    prod = session.get('product')
    type_data = database.querytype(prod, si)
    session['size'] = si
    return render_template("type.html", type_data=type_data)

@app.route("/product")
def product():
    produ = session.get('product')
    siz = session.get('size')
    typ = request.args.get("type")
    
    if typ == "all":
        available = database.queryall(produ, siz)
    else:
        available = database.queryresult(produ, siz, typ)
        
    session['type'] = typ
    return render_template("available.html", available=available)

@app.route("/delete")
def delete():
    id_delete = request.args.get("delete")
    database.deleteproduct(id_delete)
    produ = session.get('product')
    siz = session.get('size')
    typ = session.get('type')
    
    if typ == "all":
        available = database.queryall(produ, siz)
    else:
        available = database.queryresult(produ, siz, typ)
    
    return render_template("available.html", available=available)

@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        product_to_save = request.form.get("textproduct")
        size_to_save = request.form.get("textsize")
        type_to_save = request.form.get("texttype")
        
        if not product_to_save or not size_to_save or not type_to_save:
            return redirect("/add")
        
        database.addproduct(product_to_save, size_to_save, type_to_save)
        return redirect("/")
        
    elif request.method == "GET":
        start = database.select_options("product")
        size = database.select_options("size")
        type = database.select_options("type")
        return render_template("add.html", starts=start, sizes=size, types=type)



if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
