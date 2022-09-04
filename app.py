from flask import Flask,request,jsonify
app=Flask(__name__)

contacts=[
    {
        "id":1,
        "name":"Raju",
        "Contact":"1234567890",
        "done":False
    },
     {
        "id":2,
        "name":"Rahul",
        "Contact":"0987654321",
        "done":False
    }
]
@app.route("/add-data",methods=["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide data"
        },400)
    contact={
         "id":contacts[-1]["id"]+1,
        "name":request.json["name"],
        "Contact":request.json.get("Contact",""),
        "done":False
    }
    contacts.append(contact)
    return jsonify({
            "status":"success",
            "message":"contact added successfully"
        },200)
        
@app.route("/get-data")
def getcontact():
    return jsonify({
        "data":contacts
    })
if(__name__=="__main__"):
    app.run(debug=True)
