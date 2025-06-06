from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)

# 数据文件路径
DATA_FILE = "data.json"

# 初始化数据文件
def init_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump({"users": []}, f)

# 读取数据
def read_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# 保存数据
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_info():
    if request.method == 'POST':
        data = request.form.to_dict()
        db = read_data()
        db["users"].append(data)
        save_data(db)
        return redirect(url_for('list_info'))
    return render_template('add_info.html')

@app.route('/list')
def list_info():
    db = read_data()
    return render_template('list.html', users=db["users"])

# API接口 - 获取所有用户信息
@app.route('/api/users', methods=['GET'])
def get_users():
    db = read_data()
    return jsonify(db["users"])

# API接口 - 添加用户
@app.route('/api/users', methods=['POST'])
def add_user_api():
    new_user = request.get_json()
    db = read_data()
    db["users"].append(new_user)
    save_data(db)
    return jsonify({"status": "success", "id": len(db["users"])}), 201

if __name__ == '__main__':
    init_data()
    app.run(debug=True)