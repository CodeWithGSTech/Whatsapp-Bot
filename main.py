from flask import Flask
from googlesearch import search
import requests
from twilio.twiml.messaging_response import MessagingResponse
 
 
app = Flask(__name__)
 
@app.route("/", methods=["POST"])
 
# chatbot logic
def bot():
 
    # user input
    user_msg = request.values.get('Body', '').lower()
 
    # creating object of MessagingResponse
    response = MessagingResponse()
 
    # User Query
    q = user_msg + "geeksforgeeks.org"
 
    # list to store urls
    result = []
 
    # searching and storing urls
    for i in search(q, num_results=3):
        result.append(i)
 
    # displaying result
    msg = response.message(f"--- Results for '{user_msg}' ---")
    for result in search_results:
        msg = response.message(result)
 
    return str(response)
 
 
if __name__ == "__main__":
    app.run()