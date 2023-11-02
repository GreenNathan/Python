from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key="dorito"

@app.route('/')
def counter():
    if "visits" not in session:
        session['visits'] = 0
    session['visits'] += 1
    return render_template('counter1.html', visits=session['visits'])

@app.route('/count_increment', methods=['post'])
def route_to_count():
    return redirect('/count')

@app.route('/count')
def count():
    session['visits'] += 1
    return render_template('counter1.html', visits=session['visits'])

@app.route('/destroy_session', methods = ["post"])
def destroy_session():
    session.pop('visits')
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)
