import numpy as np
from flask import Flask,render_template,request
import pickle
model=pickle.load(open('ckd.pkl','rb'))
app=Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('main.html')
@app.route('/login',methods=['POST'])
def func2():
    age=request.form['age']
    bp=request.form['bp']
    sg=request.form['sg']
    al=request.form['al']
    su=request.form['su']
    rbc=request.form['rbc']
    pc=request.form['pc']
    pcc=request.form['pcc']
    ba=request.form['ba']
    bgr=request.form['bgr']
    bu=request.form['bu']
    sc=request.form['sc']
    sod=request.form['sod']
    pot=request.form['pot']
    hemo=request.form['hemo']
    pcv=request.form['pcv']
    wc=request.form['wc']
    rc=request.form['rc']
    htn=request.form['htn']
    dm=request.form['dm']
    cad=request.form['cad']
    appet=request.form['appet']
    pe=request.form['pe']
    ane=request.form['ane']
    data=[[float(age),float(bp),float(sg),float(al),float(su),float(rbc),float(pc),float(pcc),float(ba),float(bgr),float(bu),float(sc),float(sod),float(pot),float(hemo),float(pcv),float(wc),float(rc),float(htn),float(dm),float(cad),float(appet),float(pe),float(ane)]]
    pred=model.predict(data)
    print(pred[0])
    if(pred<0.5):
        ans = 'Person with CKD'
    else:
       ans = 'Person with no CKD'
    
    
    return render_template('main.html',y= ans)
if __name__=='__main__':
    app.run(debug=True)