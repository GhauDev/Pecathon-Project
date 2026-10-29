from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the homepage
@app.route("/")
def home():
    # Pass data dynamically to the HTML template
    return render_template("index.html", message="Hello, World!")

# Run the application
if __name__ == "__main__":
    app.run(debug=True)