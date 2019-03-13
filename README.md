# JOB-BOT roadmap


#### Simple job-bot app.
1. This app uses a local slack workspace https://chijobtest.slack.com/
2. The slash command, also known as slack integration slash command, is called /job-bot. 
3. I created and deployed a local Flask app which accepts post requests. 
4. I used ngrok like Aly suggested to make my local Flask app visible to the public (this is for testing for now). ngrok generates a public IP address. 
5. I used that IP address and configured /job-bot command to send post requests to that IP address. 


##### Notes on implementation: 
Example usage: /job-bot @username. /job-bot @janesmith. 
1. So far, I've only tested it with my user. Would be nice to have someone else join the slack workspace and test it. 
2. the Flask app accepts a post request, then checks if the request has a username. 
    
    Example usage: 
    
    a. _/job-bot @username_. Username is present, then the app sends a text response to the user who posted. The response shows CoC conventions text that Matt Hoffman usually sends on the #job-board channel. 
    
    b. otherwise, return the _Usage_ message: "_Oops! Type /job-bot @username!_"


_here is the slash command settings page in the chijobtest slack workspace:_

https://chijobtest.slack.com/apps/A0F82E8CA-slash-commands?next_id=0

Anyone who has access to the workspace can edit the slash command settings, particularly the URL to send the request to. That way, anyone on this project can test the functionality and make changes. 

also, everything is customizable i.e, command name, response message etc. 
