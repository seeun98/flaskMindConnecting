from flask import Flask, render_template, request
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.mindConnecting

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        id = reqeust.form['id']
        pw = request.form['password']

        memberInformation = {
            'id' : id,
            'password' : pw
        }

        #db의 아이디,비밀번호와 입력된 정보가 맞는지 확인


        return jsonify({'result':'success', 'msg' : 'login seccuess'})

@app.route("/joinus", methods=['GET', 'POST'])
def joinus():
    if request.method == 'GET':
        return render_template('joinus.html')
    else:
        id = request.form['id']
        pw = request.form['password']
        email = request.form['email']
        is_student = request.form['is_student']
        department = request.form['department']

        information = {
            'id' : id,
            'password' : pw,
            'email' : email,
            'is_student' : is_student,
            'department' : department
        }
        print(information)
        db.member.insert_one({'id' : id, 'password': pw, 'is_student': is_student, 'email': email, 'department': department})
        return render_template('login.html')

if __name__ == '__main__':
    app.run("0.0.0.0", port=5000, debug=True)