import os
import psycopg2
from flask import Flask, render_template, jsonify
import credentialfile

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user=credentialfile.DB_USERNAME,
        password=credentialfile.DB_PASSWORD)
    return conn

@app.route('/get_tree_data/', methods=['GET'])
def get_tree_data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT master_station_code, member_code FROM master_station_code_tbl;')
    codes = cur.fetchall()

    data = {}

    for row in codes:
        master_station_code = row[0]
        member_code = row[1]

        if master_station_code not in data:
            data[master_station_code] = {'name':master_station_code, 'children': []}

        data[master_station_code]['children'].append(member_code)

    print(data)

    cur.close()
    conn.close()

    json_data = jsonify(data)

    return json_data

@app.route('/', methods=['GET'])
def tree_view():
    return render_template('tree_view.html')

if __name__ == '__main__':
    app.run(debug=True)