from flask import Flask, render_template, request, redirect, session

# Importing this library tp 
from datetime import datetime


app = Flask(__name__)

app.secret_key = "I love the Dominican Republic 🇩🇴"

@app.route('/')
def fruit_store():
    return render_template("fruit_store.html")

#  this route helps place orders and redirects to the orders page
@app.route('/place_order', methods=['POST'])
def place_order():

    session['strawberry'] = int(request.form['strawberry'])
    session['raspberry'] = int(request.form['raspberry'])
    session['apple'] = int(request.form['apple'])
    session['name'] = request.form['name']
    session['id'] = request.form['id']
    
    # Assigning the sum of each fruit to session['total] to render using Jinja syntax in our html page
    session['total'] = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    
    #  Printing out this message on the terminal 
    print (f"Charging {session['name']} for {session['total']} fruits")
    return redirect('/order')

@app.route('/order')
def order ():
    now = datetime.now()
    #  Utilizing this format to print the date info
    date_time = now.strftime("%b %d %Y, %H:%M:%S %p")
    return render_template('order.html', date_time = date_time)

if __name__=="__main__":
    app.run(debug=True)
