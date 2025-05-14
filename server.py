from flask import Flask, jsonify, request

app = Flask(__name__)

# Create a list called 'events' with a couple of sample event dictionaries
# Each dictionary should have an 'id' and a 'title'
events = [
    {"id": 1, "title": "Tech Conference 2025"},
    {"id": 2, "title": "Python Meetup"},
    {"id": 3, "title": "Web Development Workshop"}
]

# TASK: Create a route for "/"
# This route should return a JSON welcome message
@app.route("/", methods=["GET"])
def home():
    """
    Homepage route that returns a welcome message in JSON format.
    
    Returns:
        JSON: A welcome message
    """
    return jsonify({
        "message": "Welcome to the Events API!",
        "endpoints": {
            "get_events": "/events (GET)",
            "create_event": "/events (POST)"
        }
    })

# TASK: Create a GET route for "/events"
# This route should return the full list of events as JSON
@app.route("/events", methods=["GET"])
def get_events():
    """
    Get all events.
    
    Returns:
        JSON: A list of all events
    """
    return jsonify(events)

# TASK: Create a POST route for "/events"
# This route should:
# 1. Get the JSON data from the request
# 2. Validate that "title" is provided
# 3. Create a new event with a unique ID and the provided title
# 4. Add the new event to the events list
# 5. Return the new event with status code 201
@app.route("/events", methods=["POST"])
def create_event():
    """
    Create a new event.
    
    Expects:
        JSON: A request body with a 'title' field
        
    Returns:
        JSON: The newly created event with status code 201
        or error message with status code 400 if validation fails
    """
    # Get JSON data from request
    data = request.get_json()
    
    # Validate that title is provided
    if not data or 'title' not in data:
        return jsonify({
            "error": "Missing required field: title"
        }), 400
    
    # Create a new event with a unique ID
    new_id = max(event["id"] for event in events) + 1 if events else 1
    new_event = {
        "id": new_id,
        "title": data["title"]
    }
    
    # Add the new event to the events list
    events.append(new_event)
    
    # Return the new event with status code 201 (Created)
    return jsonify(new_event), 201

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST'
    return response

if __name__ == "__main__":    
    app.run(debug=True)