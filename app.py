from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

e = create_engine('sqlite:///kicks.db')

app = Flask(__name__)
api = Api(app)

#Set initial response to allow CORS
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
  return response

class Kicks(Resource):
  def get(self):
    conn = e.connect()
    query = conn.execute("select * from kicks")
    result = {'kicks': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
    return result
    #return {'kicks': [query.cursor.fetchall()]}

  def post(self):
    #param1 = request.form['param1']
    #param2 = request.form['param2']
    kName = request.form['kName']
    model = request.form['model']
    brand = request.form['brand']
    conn = e.connect()
    conn.execute('insert into kicks')
    # if (db insertion ok)
    return 'added'
    # else
    # return 'failed'

    #Need to sanitize data before executing SQL instructions

#Specify end point
api.add_resource(Kicks, '/kicks')
#api.add_resource(Kicks, '/<string:kick_id>')

if __name__ == '__main__':
     app.run(host='0.0.0.0', debug=queryTrue)