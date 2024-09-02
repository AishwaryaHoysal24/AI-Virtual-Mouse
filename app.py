from flask import Flask, render_template, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['GET'])
def start_script():
    try:
        # Run your Python script here
        subprocess.Popen(["python", "AiVirtualMouseProject.py"])
        return jsonify({"message": "AI Virtual Mouse started!"})
    except Exception as e:
        return jsonify({"message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)