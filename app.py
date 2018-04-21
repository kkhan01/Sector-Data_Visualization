from __future__ import print_function
from flask import Flask, render_template, request, flash, redirect, url_for, session
import json
import sys

app = Flask(__name__)
app.secret_key = 'keysmithsmakekeys'

#PRINTS STUFF!!!!
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    return

@app.route('/')
def root():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

dsn = ""
dss = ""
dsf = ""
cn = ""
@app.route('/quiz/<value>', methods=['POST','GET'])
def quiz(value):
    eprint(value)
    global dsn
    global dss
    global dsf
    global cn
    # when value is:
    #1 = countries, 2 = cars, 3 = songs
    if(value == '1'):
        dsn = "the world's top 15 most populous countries"
    elif(value == '2'):
        dsn = "the Europe's top 15 most popular car models"
    elif(value == '3'):
        dsn = "the world's top 15 most popular songs"
    eprint(dsn)
    dss = 15
    dsf = 'WorldPopulation.csv'
    cn = "Percentage of Population of the 15 Most Populous Countries"
    return render_template('quiz.html', dataset_name=dsn, dataset_size=dss, data_file=dsf, chart_name=cn, time=60)

@app.route('/visualization')
def visualization():
    return render_template('visualization.html', dataset_name="World Population", data_file='WorldPopulation.csv')

query = "hi"
array = ['hi', 'bye']
@app.route('/search/<res>', methods=['POST','GET'])
def search(res):
    global query
    st = query
    global array
    result = array
    #eprint("Testing:")
    #eprint(array)
    return render_template('search.html', s_text = st, results = result)

@app.route('/searchjs', methods=['POST','GET'])
def searchjs():
    q = request.form['q']
    #eprint(q)
    d = request.form['d']
    dd = json.loads(d)
    #eprint(dd)
    
    #session["q"] = q
    #session["d"] = dd[0]

    global query
    query = q

    global array
    array = dd
    return "Hi"

@app.route('/s', methods=['POST','GET'])
def s():
    return "hi"

if __name__ == "__main__":
    app.debug = True
    app.run()
