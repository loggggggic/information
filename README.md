# My Flask API

这是一个简单的 Flask 应用程序，用于管理用户信息。该应用程序允许用户添加、查看和通过 API 访问用户数据。

## 目录结构
my_flask_api/
├── static/
│ └── styles.css
├── templates/
│ ├── add_info.html
│ ├── index.html
│ └── list.html
├── app.py
├── data.json
└── README.md


## 功能

- **添加用户信息**：用户可以通过表单添加姓名、邮箱、电话和地址。
- **查看用户列表**：用户可以查看已添加的所有用户信息。
- **API 接口**：
  - `GET /api/users`：获取所有用户信息。
  - `POST /api/users`：添加用户信息。

## 安装

1. **克隆仓库**：
   ```bash
   git clone https://github.com/loggggggic/information.git
   cd information

2. **创建虚拟环境**:
   python -m venv myenv
   source myenv/bin/activate  # 在 Windows 上使用 myenv\Scripts\activate

3. **安装依赖**:
   pip install Flask

# 使用
1. **运行应用**：
    python app.py

2. **访问应用**：
    打开浏览器，访问 http://127.0.0.1:5000

3. **使用 API**：
    - **获取用户信息**：curl http://127.0.0.1:5000/api/users
    - **添加用户信息**：curl -X POST http://127.0.0.1:5000/api/users -H "Content-Type: application/json" -d '{"name": "张三", "email": "zhangsan@example.com", "phone": "123456789", "address": "中国"}'



