import os
from mysql.connector import connect
  
    
def querystart():
    conn = connect(user=os.environ['username'], password=os.environ['password'], host=os.environ['host'], database=os.environ['database'])
    data = []
    with conn.cursor() as cursor:
        cursor.execute("SELECT DISTINCT product FROM products")
        result = cursor.fetchall()
        key = ('product',)
            
        for row in result:
            data.append(dict(zip(key, row)))
            
    conn.close()
    return data
        

def querysize(product):
    conn = connect(user=os.environ['username'], password=os.environ['password'], host=os.environ['host'], database=os.environ['database'])
    data = []
    with conn.cursor() as cursor:
        query = f"SELECT DISTINCT size FROM products WHERE product='{product}'"
        cursor.execute(query)
        result = cursor.fetchall()
        key = ('size',)
            
        for row in result:
            data.append(dict(zip(key, row)))
            
    conn.close()
    return data
        

def queryresult(product, size, type):
    conn = connect(user=os.environ['username'], password=os.environ['password'], host=os.environ['host'], database=os.environ['database'])
    data = []
    with conn.cursor() as cursor:
        cursor.execute("SELECT id FROM products WHERE product = %s AND size = %s AND type = %s", (product, size, type,))
        result = cursor.fetchall()
        key = ('id',)
            
        for row in result:
            data.append(dict(zip(key, row)))
            
    conn.close()
    return data


def querytype(product, size):
    conn = connect(user=os.environ['username'], password=os.environ['password'], host=os.environ['host'], database=os.environ['database'])
    data = []
    with conn.cursor() as cursor:
        query = f"SELECT DISTINCT type FROM products WHERE product='{product}' AND size='{size}'"
        cursor.execute(query)
        result = cursor.fetchall()
        key = ('type',)
            
        for row in result:
            data.append(dict(zip(key, row)))
            
    conn.close()
    return data


def queryall(product, size):
    conn = connect(user=os.environ['username'], password=os.environ['password'], host=os.environ['host'], database=os.environ['database'])
    data = []
    with conn.cursor() as cursor:
        cursor.execute("SELECT id FROM products WHERE product = %s AND size = %s", (product, size,))
        result = cursor.fetchall()
        key = ('id',)
            
        for row in result:
            data.append(dict(zip(key, row)))
            
    conn.close()
    return data


def addproduct(product, size, type):
    conn = connect(user=os.environ['username'], password=os.environ['password'], host=os.environ['host'], database=os.environ['database'])
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO products (product, size, type) VALUES (%s, %s, %s)", (product, size, type,))
        conn.commit()
    conn.close()
    return
    
    
def select_options(parameter):
    conn = connect(user=os.environ['username'], password=os.environ['password'], host=os.environ['host'], database=os.environ['database'])
    data = []
    with conn.cursor() as cursor:
        query = f"SELECT DISTINCT {parameter} FROM products"
        cursor.execute(query)
        result = cursor.fetchall()
        key = (parameter,)
            
        for row in result:
            data.append(dict(zip(key, row)))
            
    conn.close()
    return data


def deleteproduct(id):
    conn = connect(user=os.environ['username'], password=os.environ['password'], host=os.environ['host'], database=os.environ['database'])
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM products WHERE id = %s", (id,))
        conn.commit()
    conn.close()
    return

