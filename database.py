from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['connection_string']

def querystart():
    engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })
    data = []
    with engine.connect() as cursor:
        result = cursor.execute(text("SELECT DISTINCT product FROM products")).all()
        key = ('product',)
            
        for row in result:
            data.append(dict(zip(key, row)))
            
    engine.dispose()
    return data
        

def querysize(product):
    engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })
    data = []
    with engine.connect() as cursor:
        query = text(f"SELECT DISTINCT size FROM products WHERE product='{product}'")
        
        result = cursor.execute(query).all()
        key = ('size',)
            
        for row in result:
            data.append(dict(zip(key, row)))
            
    engine.dispose()
    return data
        

def queryresult(product, size, type):
    engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })
    data = []
    with engine.connect() as cursor:
        query = text("SELECT id FROM products WHERE product=:product AND size=:size AND type=:type")
        result = cursor.execute(query, {'product': product, 'size': size, 'type': type}).all()
        key = ('id',)
            
        for row in result:
            data.append(dict(zip(key, row)))
            
    engine.dispose()
    return data


def querytype(product, size):
    engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })
    data = []
    with engine.connect() as cursor:
        query = text(f"SELECT DISTINCT type FROM products WHERE product='{product}' AND size='{size}'")
        
        result = cursor.execute(query).all()
        key = ('type',)
            
        for row in result:
            data.append(dict(zip(key, row)))
            
    engine.dispose()
    return data


def queryall(product, size):
    engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })
    data = []
    with engine.connect() as cursor:
        query = text("SELECT id FROM products WHERE product = :product AND size = :size")
        result = cursor.execute(query, {'product': product, 'size': size}).all()
        key = ('id',)
            
        for row in result:
            data.append(dict(zip(key, row)))
            
    engine.dispose()
    return data


def addproduct(product, size, type):
    engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })
    with engine.connect() as cursor:
    query = text("INSERT INTO products (product, size, type) VALUES (:product, :size, :type)")
        cursor.execute(query, {'product': product, 'size': size, 'type': type})
    engine.dispose()
    return
    
    
def select_options(parameter):
    engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })
    data = []
    with engine.connect() as cursor:
        query = text(f"SELECT DISTINCT {parameter} FROM products")
        
        result = cursor.execute(query).all()
        key = (parameter,)
            
        for row in result:
            data.append(dict(zip(key, row)))
            
    engine.dispose()
    return data


def deleteproduct(id):
    engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })
    with engine.connect() as cursor:
        query = text("DELETE FROM products WHERE id = :id")
        cursor.execute(query, { 'id': id})
    engine.dispose()
    return


