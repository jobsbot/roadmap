from flask import Flask, abort, make_response, request, jsonify
import ast

app = Flask(__name__)


# Create the URL route in our application for "/"
@app.route("/")
def home():
    return "HELLO! THIS IS CHICAGO TECH SLACK'S JOB_BOT."


@app.route("/job-bot", methods=['POST'])
def post():
    # print("HEADERS", request.headers)
    data = request.get_data().decode('utf-8')
    ss = request.json
    print(ss)

    return "OK!"
    # if request.data:
    #     data = request.get_json() #ast.literal_eval(request.data.decode("utf-8"))
    #     print('te', data)
    #     return generate_convention(data)
    # else:
    #     return abort(400, "This is a Bad request!")


def generate_convention(data):
    conv = "Hi " + data['text'] + "! HERE IS THE CONVENTION. STICK TO IT!\n"
    return make_response(conv, 201)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)



"""
SAMPLE PAYLOAD 
token=gIkuvaNzQIHg97ATvDxqgjtO
&team_id=T0001
&team_domain=example
&enterprise_id=E0001
&enterprise_name=Globular%20Construct%20Inc
&channel_id=C2147483705
&channel_name=test
&user_id=U2147483697
&user_name=Steve
&command=/weather
&text=94070
&response_url=https://hooks.slack.com/commands/1234/5678
&trigger_id=13345224609.738474920.8088930838d88f008e0
"""