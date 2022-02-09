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



    return render_template("/voca-level.html")

@app.route("/voca-pre")
def voca_pre():



    return render_template("/chapter_pre.html")


@app.route("/voca-q-pre")
def voca_q_pre():

    return render_template("/voca-question-ps.html")

@app.route("/result", methods=['POST'])
def voca_result():



    return render_template("/voca-result.html")

@app.route("/voca/ajax/q_load", methods=['POST'])
def q_load():

    q_list = [{"q_num":1,
            "q":"영화",
            "a1":"movie",
            "a2":"mavie",
            "a3":"mobie"
        },
        {"q_num":2,
            "q":"집",
            "a1":"movie",
            "a2":"mavie",
            "a3":"mobie"
        },
        {"q_num":3,
            "q":"배우",
            "a1":"movie",
            "a2":"mavie",
            "a3":"mobie"
        },
        {"q_num":4,
            "q":"군대",
            "a1":"movie",
            "a2":"mavie",
            "a3":"mobie"
        },
        {"q_num":5,
            "q":"영웅",
            "a1":"movie",
            "a2":"mavie",
            "a3":"mobie"
        }
    ]

    return jsonify(q_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

