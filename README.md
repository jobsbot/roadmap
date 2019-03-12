# JOB-BOT roadmap


#### Simple job-bot app.
1. I have a free local (local to me) slack workspace that I created. 
2. Added a new slack integration slash command called /job-bot. 
3. I created and deployed a local Flask app which accepts post requests. 
4. I used ngrok like Aly suggested to make my local Flask app visible to the public (this is for testing for now). ngrok generates a public IP address. 
5. Used that IP address and configured /job-bot command to send post requests to that IP address. 


##### Notes on implementation: 
Example usage: /job-bot @username. /job-bot @janesmith. 
1. So far, I've only tested it with my user. Would be nice to have someone else join the slack workspace and test it. 
2. the Flask app accepts a post request, then checks if the request has any data. 
3. if data is present, then the app sends a text response to the user who posted. The response shows CoC conventions text that Matt Hoffman usually sends on the #job-board channel. 

....