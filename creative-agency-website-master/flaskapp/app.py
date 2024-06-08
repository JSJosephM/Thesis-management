from flask import Flask, request, render_template
import os
from datetime import datetime
import mysql.connector

app = Flask(__name__)

# MySQL configuration (replace with your actual credentials)
app.config['MYSQL_HOST'] = 'localhost:3306'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'users'

mysql_conn = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        # Insert file metadata into MySQL (e.g., filename, timestamp)
        cursor = mysql_conn.cursor()
        query = "INSERT INTO files (filename, upload_timestamp) VALUES (%s, %s)"
        cursor.execute(query, (file.filename, datetime.now()))
        mysql_conn.commit()
        cursor.close()

        return "File uploaded successfully"

if __name__ == '__main__':
    app.run(debug=True)
