
from flask import Flask, request, jsonify
import pymysql
from flasgger import Swagger

db = pymysql.connect('localhost', 'root', '123', 'petdb')
cur = db.cursor()

app = Flask(__name__)
Swagger(app)


@app.route('/', methods = ['GET'])
def get_pet_resource():
    """
        This is the pet database API
        Call this api to get the list of all pets available.
        ---
        tags:
            - Pet Database API
        responses:
            500:
                description: Error All pets are angry!
            200:
                description: List of pets
                schema:
                    id: Pet
                    properties:
                        id:
                            type: integer
                            description: identification number of pet
                        name:
                            type: string
                            description: name of pet
                        species:
                            type: string
                            description: breed of pet
                        gender:
                            type: string
                            description: gender of pet
                        birthday:
                            type: string or datetime object
                            description: date of birth of pet
            404:
                description: Error, wrong route!
    """
    cur.execute("select * from pets")
    pets = cur.fetchall()
    return jsonify(pets)


@app.route('/', methods = ['PUT'])
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
