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

@app.route("/result", methods=['GET','POST'])
def voca_result():

    level = request.args.get("level")
    unit = request.args.get("unit")

    return render_template("/voca-result.html", level=level, unit=unit)


@app.route("/marking", methods=['GET','POST'])
def marking():
    level = request.form["level"]
    unit = request.form["unit"]

    if level == "10":
        q_num = 10
    elif level == "5":
        q_num = 10

    d = {}
    for i in range(1, q_num+1):
        d['q{}'.format(i)] = request.form["q{}".format(i)]

    for i in range(1, q_num+1):
        if session['a{}'.format(i)] == 0:
            session['a{}'.format(i)] = "A"
        elif session['a{}'.format(i)] == 1:
            session['a{}'.format(i)] = "B"
        elif session['a{}'.format(i)] == 2:
            session['a{}'.format(i)] = "C"
        print(session['a{}'.format(i)])



    conn = pymysql.connect(host='localhost', user='root', password='root', db='voca')
    curs = conn.cursor(pymysql.cursors.DictCursor)

    for i in range(1, q_num+1):
        print(d['q{}'.format(i)])
        if d['q{}'.format(i)] is None or d['q{}'.format(i)] == "":
            curs.execute("INSERT INTO VOCA_RESULT (q_idx,unit,user_idx,a_check,level) values (%s,%s,'1','?',%s)", (session['q{}'.format(i)],unit,level))
            conn.commit()
        elif d['q{}'.format(i)] == session['a{}'.format(i)]:
            curs.execute("INSERT INTO VOCA_RESULT (q_idx,unit,user_idx,a_check,level) values (%s,%s,'1','O',%s)", (session['q{}'.format(i)],unit,level))
            conn.commit()
        else:
            curs.execute("INSERT INTO VOCA_RESULT (q_idx,unit,user_idx,a_check,level) values (%s,%s,'1','X',%s)", (session['q{}'.format(i)],unit,level))
            conn.commit()
    return redirect(url_for('voca_result', level=level,unit=unit))

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

@app.route("/exam_result_ajax", methods=['POST'])
def exam_result_ajax():

    level = request.form["level"]
    unit = request.form["unit"]
    user_idx = request.form["user_idx"]

    conn = pymysql.connect(host='localhost', user='root', password='root', db='voca')
    curs = conn.cursor(pymysql.cursors.DictCursor)
    curs.execute("SELECT sum(if(a_check='O', 1,0)) as correct, sum(if(a_check='X', 1,0)) as wrong_answer, sum(if(a_check='?', 1,0)) as answer_pass FROM voca_result WHERE unit = %s AND LEVEL = %s AND user_idx = %s", (unit,level,user_idx))
    data = curs.fetchone()




    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=14591, debug=True)

