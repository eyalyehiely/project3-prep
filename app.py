from flask import Flask,render_template,redirect,jsonify,json,request
import datetime
app = Flask(__name__)

@app.route('/api/services',methods = ['GET'])
def get_services():
    data = ['service1','service2']
    return json.dumps({
        "services":data,
        "length":len(data),
        "last_updated":datetime.datetime.now()
        })


@app.route('/api/services', methods = ['POST'])
def add_services():
    data = json.loads(request.json)['services']
    return json.dumps({
        "status":'ok',
        "length":len(data)
        })




if __name__ == '__main__':
    app.run(debug=True)