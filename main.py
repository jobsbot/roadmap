from flask import Flask, abort, make_response, request, jsonify
import ast
import json
import urllib

app = Flask(__name__)


# Create the URL route in our application for "/"
@app.route("/")
def home():
    return "HELLO! THIS IS CHICAGO TECH SLACK'S JOB_BOT."


@app.route("/job-bot", methods=['POST'])
def post():
    if request.get_data():
        # print("HEADERS", request.headers)
        data = request.get_data().decode('utf-8')
        return generate_convention(data)
    else:
        return "_Oops! Type /job-bot @username!_"


def generate_convention(data):
    json_data = urllib.parse.parse_qs(data)
    print(json_data)
    conv = "Hi <@" + ''.join(json_data['user_id']) + "> ! HERE IS THE CONVENTION. STICK TO IT!\n\n"

    static_msg = """
    *Job Posting Conventions with examples*
    Principal Posters:
    [Principal] [Company Name] [Website or Link to Job Posting or Job Description Text] [Contact Information or Offer to Discuss in DMs]
    
    Example: [Principal] [SpaceX] [www.spacex.com] [www.linktojobposting.com] [Email Elon or feel free to DM]
    Third Party Recruiters:
    [Third Party Recruiter] [Recruiting Company Name] [Recruiting Company Website] [Job Description Text or Link to Job Description] [Contact Information or Offer to Discuss in DMs]
    
    Example: [Third Party Recruiter] [re-factor] [re-factor.co] [Build Software for shuttle launches, etc.] [Email me at matt@re-factor.co or feel free to direct message for details]
    """
    return make_response(conv+static_msg, 201)


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

