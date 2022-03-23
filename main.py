from flask import Flask
from datetime import datetime
from flask import render_template, request, redirect, url_for, session, jsonify
import pymysql
import json


app = Flask(__name__)

@app.route("/")
def index():

    return render_template("/voca-main.html")

@app.route("/level-select")
def level_select():

    page = "voca-chapter"

    return render_template("/voca-level.html", page=page)

@app.route("/voca-chapter", methods=['POST'])
def voca_pre():

    level = request.form["level"]
    page = "voca-question"


    return render_template("/chapter_pre.html", level=level, page=page)


@app.route("/voca-question", methods=['POST'])
def voca_question():

    level = request.form["level"]
    unit = request.form["unit"]

    print(unit);

    return render_template("/voca-question-ps.html", level=level, unit=unit)

@app.route("/result", methods=['POST'])
def voca_result():
    level = request.form["level"]
    time = request.form["time"]

    return render_template("/voca-result.html", level=level, time=time)

@app.route("/AAA")
def aaa():


    return render_template("/test/voca-question-jh.html")

@app.route("/voca/ajax/q_load", methods=['POST'])
def q_load():

    level = request.form["level"]
    unit = request.form["unit"]
    if level == "10":
        q_num = 20
    elif level == "5":
        q_num = 25

    conn = pymysql.connect(host='localhost', user='root', password='root', db='voca')
    curs = conn.cursor(pymysql.cursors.DictCursor)
    curs.execute("SELECT DISTINCT(question),meaning, (select meaning from question WHERE meaning = meaning order by RAND() LIMIT 1 ) AS EXAMPLE_1 , (select meaning from question WHERE meaning = meaning  order by RAND() LIMIT 1 ) AS EXAMPLE_2 FROM question q WHERE q.level = %s AND Unit = %s ORDER BY RAND() LIMIT %s", (level,unit, q_num))
    data = curs.fetchall()

    return jsonify(data)

@app.route("/voca_chapter_ajax", methods=['POST'])
def chapter_load():

    level = request.form["level"]
    chapter = request.form["chapter"]

    conn = pymysql.connect(host='localhost', user='root', password='root', db='voca')
    curs = conn.cursor(pymysql.cursors.DictCursor)
    curs.execute("SELECT * FROM UNIT WHERE CHAPTER = %s AND LEVEL = %s", (chapter,level))
    data = curs.fetchall()

    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

