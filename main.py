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

    return render_template("/voca-question-ps.html", level=level)

@app.route("/result", methods=['POST'])
def voca_result():
    level = request.form["level"]

    return render_template("/voca-result.html", level=level)

@app.route("/AAA")
def aaa():


    return render_template("/test/voca-question-jh.html")

@app.route("/voca/ajax/q_load", methods=['POST'])
def q_load():

    q_list = [{
            "level":10,
            "question":{
                "q_num":1,
                "q":"영화",
                "a1":"movie",
                "a2":"mavie",
                "a3":"mobie"
            }
        },
        {
            "level": 10,
            "question": {
                "q_num": 2,
                "q": "2번 문항",
                "a1": "movie",
                "a2": "mavie",
                "a3": "mobie"
            }
        },
        {
            "level": 10,
            "question": {
                "q_num": 3,
                "q": "3번 문항",
                "a1": "movie",
                "a2": "mavie",
                "a3": "mobie"
            }
        },
        {
            "level": 5,
            "question": {
                "q_num": 1,
                "q": "STARTER 1번 문항",
                "a1": "movie",
                "a2": "mavie",
                "a3": "mobie"
            }
        },
        {
            "level": 5,
            "question": {
                "q_num": 2,
                "q": "STARTER 2번 문항",
                "a1": "movie",
                "a2": "mavie",
                "a3": "mobie"
            }
        },
        {
            "level": 5,
            "question": {
                "q_num": 3,
                "q": "STARTER 3번 문항",
                "a1": "movie",
                "a2": "mavie",
                "a3": "mobie"
            }
        },

        {
            "level": 4,
            "question": {
                "q_num": 1,
                "q": "BASIC 1번 문항",
                "a1": "movie",
                "a2": "mavie",
                "a3": "mobie",
                "a4": "mobie",
                "a5": "mobie"
            }
        },
        {
            "level": 4,
            "question": {
                "q_num": 2,
                "q": "BASIC 2번 문항",
                "a1": "movie",
                "a2": "mavie",
                "a3": "mobie",
                "a4": "mobie",
                "a5": "mobie"
            }
        },
        {
            "level": 4,
            "question": {
                "q_num": 3,
                "q": "BASIC 3번 문항",
                "a1": "movie",
                "a2": "mavie",
                "a3": "mobie",
                "a4": "mobie",
                "a5": "mobie"
            }
        },
        {
            "level": 3,
            "question": {
                "q_num": 1,
                "q": "JUNIOR 1번 문항",
                "a1": "movie",
                "a2": "mavie",
                "a3": "mobie",
                "a4": "mobie",
                "a5": "mobie",
                "a6": "mobie"
            }
        },
        {
            "level":3,
            "question": {
                "q_num": 2,
                "q": "JUNIOR 2번 문항",
                "a1": "movie",
                "a2": "mavie",
                "a3": "mobie",
                "a4": "mobie",
                "a5": "mobie",
                "a6": "mobie"
            }
        },
        {
            "level": 3,
            "question": {
                "q_num": 3,
                "q": "JUNIOR 3번 문항",
                "a1": "movie",
                "a2": "mavie",
                "a3": "mobie",
                "a4": "mobie",
                "a5": "mobie",
                "a6": "mobie"
            }
        },

        {
            "level": 6,
            "question": {
                "q_num": 1,
                "q": "HJ 1번 문항",
                "a1": "movie",
                "a2": "mavie",
                "a3": "mobie",
                "a4": "mobie",
                "a5": "mobie",
                "a6": "mobie"
            }
        },
        {
            "level": 6,
            "question": {
                "q_num": 2,
                "q": "HJ 2번 문항",
                "a1": "movie",
                "a2": "mavie",
                "a3": "mobie",
                "a4": "mobie",
                "a5": "mobie",
                "a6": "mobie"
            }
        },
        {
            "level": 6,
            "question": {
                "q_num": 3,
                "q": "HJ 3번 문항",
                "a1": "movie",
                "a2": "mavie",
                "a3": "mobie",
                "a4": "mobie",
                "a5": "mobie",
                "a6": "mobie"
            }
        },
    ]

    return jsonify(q_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

