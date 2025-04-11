from flask import Flask, jsonify, request

app = Flask(__name__)

# Create a list called 'events' with a couple of sample event dictionaries
# Each dictionary should have an 'id' and a 'title'

# TASK: Create a route for "/"
# This route should return a JSON welcome message

# TASK: Create a GET route for "/events"
# This route should return the full list of events as JSON

# TASK: Create a POST route for "/events"
# This route should:
# 1. Get the JSON data from the request
# 2. Validate that "title" is provided
# 3. Create a new event with a unique ID and the provided title
# 4. Add the new event to the events list
# 5. Return the new event with status code 201

if __name__ == "__main__":
    app.run(debug=True)
