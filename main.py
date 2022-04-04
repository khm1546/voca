from flask import Flask
from datetime import datetime
from flask import render_template, request, redirect, url_for, session, jsonify, session
import pymysql
import random
import json


app = Flask(__name__)
app.secret_key = 'asdfasdfsdf'
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
    if level == "10":
        q_num = 10
    elif level == "5":
        q_num = 10

    d = {}
    for i in range(1, q_num+1):
        d['q{}'.format(i)] = request.form["q{}".format(i)]
    print(d)

    for i in range(1, q_num+1):
        if session['a{}'.format(i)] == 0:
            session['a{}'.format(i)] = "A"
        elif session['a{}'.format(i)] == 1:
            session['a{}'.format(i)] = "B"
        elif session['a{}'.format(i)] == 2:
            session['a{}'.format(i)] = "C"
        print(session['a{}'.format(i)])


    for i in range(1, q_num+1):
        print(d['q{}'.format(i)])
        if d['q{}'.format(i)] is None or d['q{}'.format(i)] == "":
            print(session['q{}'.format(i)], ": ", "?")
        elif d['q{}'.format(i)] == session['a{}'.format(i)]:
            print(session['q{}'.format(i)], ": ", "O")
        else:
            print(session['q{}'.format(i)], ": ", "X")


    return render_template("/voca-result.html", level=level, time=time)

@app.route("/AAA")
def aaa():


    return render_template("/test/voca-question-jh.html")

@app.route("/voca/ajax/q_load", methods=['POST'])
def q_load():

    level = request.form["level"]
    unit = request.form["unit"]
    if level == "10":
        q_num = 10
    elif level == "5":
        q_num = 10

    conn = pymysql.connect(host='localhost', user='root', password='root', db='voca')
    curs = conn.cursor(pymysql.cursors.DictCursor)
    curs.execute("SELECT idx, question, meaning FROM question WHERE level = %s AND unit = %s ORDER BY RAND() LIMIT %s", (level,unit, q_num))
    questions = curs.fetchall()

    curs.execute("SELECT idx, meaning FROM question WHERE level=%s AND unit=%s ORDER BY RAND()", (level, unit))
    distractors = curs.fetchall()

    for q in questions:
        idx = q['idx']
        count = 0
        choices = []
        while count < 2:
            d = random.choice(distractors)
            if d['idx'] != idx and d['idx'] not in choices:
                q['EXAMPLE_{}'.format(count+1)] = d['meaning']
                choices.append(d['idx'])
                count += 1

    session.clear()
    data = []
    for num, q in enumerate(questions, 1):
        row = {}
        idx = q['idx']
        session['q{}'.format(num)] = idx
        dists = [q['meaning'], q['EXAMPLE_1'], q['EXAMPLE_2']]
        indices = [0, 1, 2]
        random.shuffle(indices)
        answer_idx = indices.index(0)
        session['a{}'.format(num)] = answer_idx
        dists = [dists[i] for i in indices]
        row['meaning'] = dists[0]
        row['EXAMPLE_1'] = dists[1]
        row['EXAMPLE_2'] = dists[2]
        row['question'] = q['question']
        data.append(row)

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
    app.run(host='0.0.0.0', port=14591, debug=True)

