import flask

app=flask.Flask(__name__)
"""
@app.route("/hello")
def hello():
    return "hello flask"
"""
"""
@app.route("/getgrades")
def get_grades():
    grades=[]
    with open("input.txt") as fin:
        for lin in fin:
            if len(lin)>0:
                lin=lin.strip()
                fields=lin.strip().split('\t')
                grades.append(fields)
    import json
    json_str=json.dumps(grades)
    return json_str

"""
@app.route("/gradebyid/<id>")
def gradebyid(id):
    grades=[]
    with open("input.txt") as fin:
        for lin in fin:
            if len(lin)>0:
                lin=lin.strip()
                fields=lin.strip().split('\t')
                if fields[0]==id:
                    grades.append(fields)
    import json
    json_str=json.dumps(grades)
    return json_str
app.run()