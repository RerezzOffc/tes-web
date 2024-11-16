from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def handle_data():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    return jsonify({"message": f"Hello, {name}! Your email {email} is received."})

if __name__ == '__main__':
    app.run(debug=True)
