
from flask import Flask,request,jsonify
import json
import sqlite3
app = Flask(__name__)

def create_connection():
    try:
        conn = sqlite3.connect("user.db")
        return conn
    except Error as e:
        print(e)

    return None

def setData(row):
    try:
      x = {
          "id": row[0],
          "firstname": row[1],
          "lastname":row[2],
          "email": row[3],
          "gender": row[4],
          "age": row[5]
        }

      return x
    except Exception as e:
      print(e)

@app.route('/users')
def index():
    con = create_connection()
    cursor = con.cursor()
    data = request.json
    data = []
    myresult = cursor.execute("SELECT * FROM 'users' LIMIT {} ").format(limit)
    for row in myresult:
        x = {
          "id": row[0],
          "firstname": row[1],
          "lastname":row[2],
          "email": row[3],
          "gender": row[4],
          "age": row[5]
        }
        data.append(x)

    return json.dumps(data)


@app.route('/api/<name>')
def get(name):
        return 'hello {}'.format(name)

@app.route('/api', methods=['GET'])
def hello(name):
        return 'hello '


@app.route('/users/id/<id>', methods=['GET'])
def getDataById(id):
    con = create_connection()
    cursor = con.cursor()
    sql = "SELECT * FROM 'users' where id = '{}'".format(id)
    result = cursor.execute(sql)
    data = []
    for row in result:
        x = setData(row)
        data.append(x)

    return json.dumps(data)

@app.route('/users/firstname/<firstname>', methods=['GET'])
def getDataByFirstname(firstname):
    con = create_connection()
    cursor = con.cursor()
    sql = "SELECT * FROM 'users' where first_name = '{}'".format(firstname)
    result = cursor.execute(sql)
    data = []
    for row in result:
        x = setData(row)
        data.append(x)

    return json.dumps(data)


@app.route('/users/lastname/<lastname>', methods=['GET'])
def getDataByLastname(lastname):
    con = create_connection()
    cursor = con.cursor()
    sql = "SELECT * FROM 'users' where last_name = '{}'".format(lastname)
    result = cursor.execute(sql)
    data = []
    for row in result:
        x = setData(row)
        data.append(x)

    return json.dumps(data)

@app.route('/users/email/<email>', methods=['GET'])
def getDataByEmail(email):
    con = create_connection()
    cursor = con.cursor()
    sql = "SELECT * FROM 'users' where email = '{}'".format(email)
    result = cursor.execute(sql)
    data = []
    for row in result:
        x = setData(row)
        data.append(x)

    return json.dumps(data)

@app.route('/users/gender/<gender>', methods=['GET'])
def getDataByGender(gender):
    con = create_connection()
    cursor = con.cursor()
    sql = "SELECT * FROM 'users' where gender = '{}'".format(gender)
    result = cursor.execute(sql)
    data = []
    for row in result:
        x = setData(row)
        data.append(x)

    return json.dumps(data)

@app.route('/users/age/<age>', methods=['GET'])
def getDataByAge(age):
    con = create_connection()
    cursor = con.cursor()
    sql = "SELECT * FROM 'users' where age = {}".format(age)
    result = cursor.execute(sql)
    data = []
    for row in result:
        x = setData(row)
        data.append(x)

    return jsonify(data)


@app.route('/users/new', methods=['POST'])
def addUser():
    data = request.json
    con = create_connection()
    cursor = con.cursor()
    sql = "SELECT MAX(id) FROM 'users'"
    cursor.execute(sql)
    result = cursor.fetchall()
    for x in result:
         last_index = x[0] +1


    sql = "INSERT INTO users (id,first_name,last_name,email,gender,age) VALUES (?,?,?,?,?,?)"
    val = (last_index,data['firstname'],data['lastname'],data['email'],data['gender'],data['age'])
    cursor.execute(sql,val)

    con.commit()
    return "เพิ่มข้อมูลเรียบร้อยแล้ว"

@app.route('/users/<id>', methods=['DELETE'])
def deleteUser(id):
    con = create_connection()
    cursor = con.cursor()
    sql = "DELETE FROM 'users' where id = {}".format(id)
    cursor.execute(sql)
    con.commit()
    return "ลบข้อมูลเรียบร้อยแล้ว"

@app.route('/users/', methods=['PUT'])
def editUser():
    data = request.json
    id = data['id']
    con = create_connection()
    cursor = con.cursor()
    sql = "UPDATE users set first_name = ?,last_name = ?,email = ?,gender = ?,age = ? where id = {}".format(id)
    val = (data['firstname'],data['lastname'],data['email'],data['gender'],data['age'])
    cursor.execute(sql,val)
    con.commit()
    return "แก้ไขข้อมูลเรียบร้อยแล้ว"


if __name__ == '__main__':
   app.run()