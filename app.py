from flask import Flask, request, make_response
from pymongo import MongoClient
import  json



app = Flask(__name__)

client = MongoClient('mongodb+srv://API_Project:Etladmin!2021@cluster0.m1jxb.mongodb.net/API_Project?retryWrites=true&w=majority')

db = client.get_database('API_Project')

records = db.Answers

@app.route('/')
def home():
    return "Hello World"

pay_slip_url = records.update_many(
    {"name":"Payslip"},{"$set":{
                        "d_url":"https://ai.pulsehrm.com/ords/f?p=120:353:3149919257526::::"}}
)

expense_url = records.update_many(
    {"name":"Expense"},{"$set":{
                        "d_url":"https://ai.pulsehrm.com/ords/f?p=120:352:3149919257526:::::"}}
)

leave_url = records.update_many(
    {"name":"Leave"},{"$set":{
                        "d_url":"https://ai.pulsehrm.com/ords/f?p=120:324:3149919257526:::::"}}
)

regularize_attendance_url = records.update_many(
    {"name":"Regularize_Attendance"},{"$set":{
                        "d_url":"https://ai.pulsehrm.com/ords/f?p=120:30:3149919257526:::30::"}}
)

@app.route('/clientUrl', methods =["GET", "POST"])
def client_url():
    pay_slip_url_client = records.find({"name":"Payslip"},
                                        {"d_url":2,"_id":0})
    for pay_slip_client in pay_slip_url_client:
        return str(pay_slip_client['d_url'])

@app.route('/webhook', methods=['POST'])
def webhook():

    if request.method == "POST":
        req = request.get_json(silent=True, force=True)
        res = processRequest(req)

        res = json.dumps(res, indent=4)
        r = make_response(res)
        r.headers['Content-Type'] = 'application/json'
        return r


def processRequest(req):

    # Get all the Query Parameter
    query_response = req["queryResult"]
    print(query_response)
    text = query_response.get('queryText', None)
    parameters = query_response.get('parameters', None)
    intent = query_response.get("intent").get('displayName')
    if (intent == 'Payslip'):
        def get_data():
            pay_slip_url_client = records.find({"name": "Payslip"},
                                               {"d_url": 2, "_id": 0})
            for pay_slip_client in pay_slip_url_client:
                final_url = str(pay_slip_client['d_url'])

            return {
                "fulfillmentText": final_url,
            }
    elif (intent == 'Expense'):
        def get_data():
            pay_slip_url_client = records.find({"name": "Expense"},
                                               {"d_url": 2, "_id": 0})
            for pay_slip_client in pay_slip_url_client:
                final_url = str(pay_slip_client['d_url'])

            return {
                "fulfillmentText": final_url,
            }

    elif (intent == 'Leave'):
        def get_data():
            pay_slip_url_client = records.find({"name": "Leave"},
                                               {"d_url": 2, "_id": 0})
            for pay_slip_client in pay_slip_url_client:
                final_url = str(pay_slip_client['d_url'])

            return {
                "fulfillmentText": final_url,
            }

    elif (intent == 'Regularize_Attendance'):
        def get_data():
            pay_slip_url_client = records.find({"name": "Regularize_Attendance"},
                                               {"d_url": 2, "_id": 0})
            for pay_slip_client in pay_slip_url_client:
                final_url = str(pay_slip_client['d_url'])

            return {
                "fulfillmentText": final_url,
            }

    res = get_data()

    return res

if __name__ == '__main__':
    app.run(debug=True)