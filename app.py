from flask import Flask,json,request
import datetime
import db
app = Flask(__name__)

@app.route('/api/services',methods = ['GET'])
def get_services():
    data = db.query("SELECT * FROM services")
    return json.dumps({
        "services":json.dumps(data),
        "length":len(data),
        "last_updated":datetime.datetime.now()
        })


@app.route('/api/services', methods = ['POST'])
def add_services():
    data = request.json['services']
    db.query(f"INSERT INTO services (name) VALUES({tuple(data)})")
    return json.dumps({
        "status":'ok',
        "length":len(data)
        })




if __name__ == '__main__':
    app.run(debug=True)