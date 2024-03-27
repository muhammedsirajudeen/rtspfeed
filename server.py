from flask import Flask, jsonify, render_template,request
from dotenv import load_dotenv
import os
import pymongo
load_dotenv()


app = Flask(__name__)
mongo_uri = os.getenv("MONGODB")
print(mongo_uri)


try:
    client=pymongo.MongoClient(mongo_uri)
    if client is not None:
        db = client.get_database('rtspfeed')  # Replace 'mydatabase' with your database name
        collection = db.get_collection('rtspurl')
        print("connected to the database")

except pymongo.errors.connectionFailure as e:
    print("Database connection failed")


# Route for rendering HTML template collect all feeds from database and return here
@app.route('/')
def index():
    cursor=collection.find()
    datalist=[data for data in cursor]
    print(datalist)
    context={
        "heading":"hey",
        "rtspdata":datalist
    }
    return render_template('index.html',**context)

# Route for getting feed and returning it
@app.route('/feed',methods=['GET','POST'])
def feed():
    if(request.method=='POST'):
        return jsonify({'message':'hello'})
    return jsonify({'message': 'Hello, world!'})

if __name__ == '__main__':
    app.run(debug=True)
