from flask import Flask, render_template, request, redirect #We need to import flask in order to use it!
app = Flask(__name__) #Create an instance of flask - activating it, getting it ready for usage
app.secret_key="supersecret"

def charge_card(name, product):
    print(f"Charging {name} $20.00 for {product}")
    print(f"Shipping {product} to {name}...")



@app.route('/') #The user will go to localhost:5000/ to activate this route
def index():    #This is the function that runs when the route is activated
    return "<h1>Hello Flask!</h1>" #This is what we send to the user

@app.route('/big_hello/<name>') #route parameters<>{}
def big_hello(name):
    print(name)
    return f"<h1 style='font-size:100pt'> HELLO {name}</h1>"

@app.route('/small_hello')
def small_hello():
    return "hello"

@app.route('/calc/<int:x>/<int:y>')
def calc(x,y):
    return f"{x+y}"

@app.route('/accept_form', methods=["post"])
def accept_form():
    print("data Received")
    print(request.form)
    print(f"{request.form['uname']} bought {request.form['product']}")
    return "thanks for the data"
    return redirect("/thanks")

    charge_card(request.form['uname'], request.from['product'])

@app.route("/thanks")
def(thanks):
    return "thanks for your purchase!"

    session['user'] = request.form['uname']
    session['product'] =  request.form['product']

@app.rout('/clear')
def clear():
    session.clear()
    return redirect('/thanks')

@app.route('/neat')
def neat():

    my_number = 6

    my_list = [
        "potatoes"
        "apples"
        "rice"
        "tar"
        "uranium"
        "cookies"
        "lamb"
        "soup"
        "rats"
    ]
    return render_template("neat.html", number=my_number, list=my_list)

if __name__ == "__main__":# Only run if directly run by the user!
    app.run(debug=True) #This will start the server!