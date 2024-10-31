from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory storage
students = []
current_id = 1

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = next((s for s in students if s['ID'] == id), None)
    return jsonify(student) if student else abort(404)

@app.route('/students', methods=['POST'])
def create_student():
    global current_id
    data = request.get_json()
    student = {'ID': current_id, 'Name': data['Name'], 'Grade': data['Grade'], 'Email': data['Email']}
    students.append(student)
    current_id += 1
    return jsonify(student), 201

@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = next((s for s in students if s['ID'] == id), None)
    if not student:
        abort(404)
    data = request.get_json()
    student.update({k: data[k] for k in data if k in student})
    return jsonify(student)

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    global students
    students = [s for s in students if s['ID'] != id]
    return jsonify({"message": "Deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
