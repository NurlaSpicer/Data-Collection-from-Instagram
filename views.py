from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """
    Main page of the web application.
    """
    try:
        # Here you can integrate data and visualizations
        return render_template('index.html')
    except Exception as e:
        print(f"Error processing request: {e}")
        return "An error occurred while loading the page."

if __name__ == "__main__":
    app.run(debug=True)
