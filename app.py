from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/attendance', methods=['POST'])
def attendance():
    # Process the attendance data here
    data = request.get_json()
    # You can access your data processing or face recognition functions here
    response = {"status": "success", "data": data}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
