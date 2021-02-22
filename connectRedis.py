import os
import json
import redis
from flask import Flask,request,jsonify

app = Flask(__name__)
db=redis.StrictRedis(
        host="10.100.2.134",
        #host='node9157-advweb-19.app.ruk-com.cloud',
        port=6379,
        #port=11163,
        password='ONVpsx16132',
        decode_responses=True) 

@app.route('/',methods=['GET']) 
def Show_Customers():
    name=db.keys() 
    name.sort()
    req = []
    for i in name :
        req.append(db.hgetall(i))
    return jsonify(req)

# Get Just Only 1 Guys
@app.route('/<Key>',methods=['GET'])
def Show_Once(Key):
    customers = db.hgetall(Key)
    print (customers)
    return jsonify(customers)

#ใส่ข้อมูลเพิ่มในตาราง
@app.route('/insert',methods=['POST'])
def Add_user():
    Address = request.json['Address']
    Career = request.json['Career']
    Fax = request.json['Fax']
    Tel = request.json['Tel']
    Key = request.json['Key']
    #print (Address)
    #print (Career)
    #print (Fax)
    #print (Tel)
    user = {"Address":Address,"Career":Career,"Fax":Fax ,"Tel":Tel}
    db.hmset(Key,user)
    return 'Data Already Inserted!!'

#ลบข้อมูล
@app.route('/<Key>',methods=['DELETE'])
def delet_data(Key):
    db.delete(Key)
    return 'Data Already Deleted'

@app.route('/setname/<name>')
def setname(name):
    db.set('name',name)
    return 'Name updated.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
