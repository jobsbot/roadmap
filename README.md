# JOB-BOT roadmap


#### Simple job-bot app.
1. I have a free local (local to me) slack workspace that I created. 
2. Added a new slack integration slash command called /job-bot. 
3. I created and deployed a local Flask app which accepts post requests. 
4. I used ngrok like Aly suggested to make my local Flask app visible to the public (this is for testing for now). ngrok generates a public IP address. 
5. Used that IP address and configured /job-bot command to send post requests to that IP address. 


##### Notes on implementation: 
1. the Flask app accepts a post request, then checks if the request has any data. 

    Example of data is a username: @johnsmith. 
2. if data is present, then the app sends a text response to the user who posted. The response alos shows CoC conventions text that Matt usually sends on the #job-board  channel. 