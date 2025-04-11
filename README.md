# Lab: Building a Front-to-Back Event Catalog

## Learning Goals

- Serve a homepage using Flask
- Create API routes that return and accept JSON
- Handle GET and POST requests on the back end
- Connect a Flask back end to a static front end
- Pass all provided back end tests

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repo-url>
cd course-8-module-6-connect-client-server-lab
```

### 2. Create Your Environment

**Using Pipenv:**
```bash
pipenv install
pipenv shell
```

---

## Running the App

```bash
python server.py
```

Then open `client/index.html` in your browser to view the frontend.

---

## Running the Tests

To check your work, run:

```bash
pytest
```

All tests must pass to complete the lab.

---

## Your Tasks

- [ ] Implement the `/` route to return a welcome message in JSON
- [ ] Implement a `GET /events` route that returns all event data
- [ ] Implement a `POST /events` route that accepts a new event and returns it with status 201
- [ ] Return a `400 Bad Request` if required data is missing in a POST

---

## File Structure

```
.
├── client/
│   ├── index.html
│   ├── styles.css
│   └── script.js
├── server.py
├── tests/
│   └── test_app.py
├── Pipfile
├── Pipfile.lock
├── README.md
```

---

Good luck! 🚀
