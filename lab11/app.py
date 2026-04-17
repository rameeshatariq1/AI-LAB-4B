from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple chatbot logic
def get_bot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hello! Welcome to the Library Assistant 📚"
    
    elif "hours" in user_input or "timing" in user_input:
        return "Library is open from 8 AM to 8 PM."

    elif "book" in user_input:
        return "You can search books using our catalog system."

    elif "due date" in user_input:
        return "Books are issued for 14 days."

    elif "fine" in user_input:
        return "Late fine is Rs. 10 per day."

    elif "bye" in user_input:
        return "Goodbye! Have a nice day 😊"

    else:
        return "Sorry, I didn't understand. Please ask about library services."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot():
    user_input = request.form["msg"]
    response = get_bot_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
