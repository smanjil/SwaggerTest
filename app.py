
from flask import Flask, request, jsonify
import pymysql
from flasgger import Swagger
from flasgger.utils import swag_from

db = pymysql.connect('localhost', 'root', '123', 'petdb')
cur = db.cursor()

app = Flask(__name__)
Swagger(app)


@app.route('/', methods = ['GET'])
@swag_from('yml/get.yml')
def get_pet_resource():
    cur.execute("select * from pets")
    pets = cur.fetchall()
    return jsonify(pets)


@app.route('/', methods = ['PUT'])
@swag_from('yml/put.yml')
def update_pet_resource():
    val = request.json
    for column in request.json.keys():
        if column != 'id':
            sql = "update pets set {0} = '{1}' where id = {2};" .format(column, val[column], val['id'])
            cur.execute(sql)
            db.commit()
    return jsonify({'Success': True})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
