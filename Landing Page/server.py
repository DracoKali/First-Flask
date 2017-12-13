from flask import Flask, render_template, redirect, request
app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/ninjas')
   

@app.route('/ninjas', methods=['GET', 'POST'])
def ninja():
    return render_template('ninjas.html')
    
    

@app.route('/ninjaNew', methods=['POST'])
def ninjaNew():
    first = request.form['first']
    print first
    last = request.form['last']
    email = request.form['email']
    area = request.form['area']
    return redirect('/')
    # return render_template('ninjaNew.html', first=first, last=last, area=area, email=email)


@app.route('/ninjaNew', methods=['GET'])
def show():
    return render_template('ninjaNew.html')


if __name__ == '__main__':
    app.run(debug=True)
