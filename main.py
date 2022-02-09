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
            "a1":"home",
            "a2":"hoem",
            "a3":"herm"
        },
        {"q_num":3,
            "q":"배우",
            "a1":"actro",
            "a2":"actor",
            "a3":"actar"
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

