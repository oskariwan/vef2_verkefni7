import os
from flask import Flask, render_template, session, url_for, request, redirect, escape
app = Flask(__name__)

app.secret_key = os.urandom(8)   
print(os.urandom(8))

# database
vorur = [   [0,"Peysa","peysa.jpg",2500],
            [1,"Skór","skor.jpg",3500],
            [2,"Buxur","buxur.jpg",4500],
            [3,"Trefill","trefill.jpg",1500],
            [4,"Jakki","jakki.jpg",13500],
            [5,"Húfa","hufa.jpg",3550]
        ]

# Rót
@app.route("/")
def index():
    karfa = []
    fjoldi=0
    if 'karfa' in session:
        karfa = session['karfa']
        fjoldi = len(karfa)
    return render_template("index.tpl", v=vorur, fjoldi=fjoldi)

# Bætum vöru í körfu.  Session hluturinn 'karfa' geymir lista af lista.
@app.route("/add/<int:id>")
def frett(id): 
    karfa = []
    fjoldi=0    
    if 'karfa' in session:
        karfa = session['karfa']
        karfa.append(vorur[id])
        session['karfa'] = karfa
        fjoldi = len(karfa)
    # ef breytan karfa er 0
    else:
        karfa.append(vorur[id])
        session['karfa'] = karfa
        fjoldi = len(karfa)

    return render_template("index.tpl", v=vorur, fjoldi=fjoldi)

# Skoðum körfuna
@app.route("/karfa")
def karfa():
    karfa = []
    summa = 0
    # Karfan er ekki tóm
    if 'karfa' in session:
        karfa = session['karfa']
        fjoldi = len(karfa) # fjöldi vara í körfu
        for i in karfa: # reiknum út heildarverð körfu, sendum niður í template
            summa += int(i[3])
        return render_template("karfa.tpl", k = karfa, tom = False, fjoldi=fjoldi, samtals=summa)
    # Karfan er tóm
    else:
        return render_template("karfa.tpl", k = karfa, tom = True)

# Eyðum einni vöru úr körfunni, okkur svo hent yfir í /körfuna (refresh)
@app.route("/eydavoru/<int:id>")
def eydavoru(id):
    karfa = []
    karfa = session['karfa']
    vara = 0
    # Finnum hvar í session listanum valin vara er í körfunni og eyðum henni
    for i in range(len(karfa)): 
        if karfa[i][0]  == id:
            vara = i
    karfa.remove(karfa[vara])
    session['karfa'] = karfa
    return render_template("eydavoru.tpl")

# Eyðum allir körfunni, okkur er svo hent yfir á rót (refresh) frá eyda.tpl
@app.route("/eyda")
def eyda():
    session.pop('karfa', None)
    return render_template("eyda.tpl")

# Upplýsingar sem sendar eru úr formi á karfa.tpl
@app.route('/result', methods = ['POST']) 
def result():
    if request.method == 'POST':
        kwargs={
            'name': request.form['nafn'],
            'email': request.form['email'],
            'phone': request.form['simi'],
            'price': request.form['samtals'],
        }
        return render_template('result.tpl',**kwargs)

# útskráning ath. redirect
@app.route('/logout')
def logout():
    session.pop('karfa', None)
#    return render_template('index.tpl')
    return redirect(url_for('index'))

@app.errorhandler(404)
def pagenotfound(error):
    return render_template('pagenotfound.html'), 404

@app.errorhandler(405)
def method_not_alloved(error):
    return render_template('method_not_alloved.tpl'), 405

if __name__ == '__main__':
    app.run()   