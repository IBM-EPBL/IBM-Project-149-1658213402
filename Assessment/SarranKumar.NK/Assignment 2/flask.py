


from flask import Flask,render_template,request

app=Flask(__name__)
@app.route('/')
@app.route('/register')
def homepage():
    return render_template('register.html')


@app.route("/confim",methods=['POST','GET'])
def register():
    if request.method == 'POST':
        n = request.form.get('name')
        a = request.form.get('age')
        c = request.form.get('city')
        return render_template('conform.html',name=n,age=a,city=c)


if __name__=="__main__":
    app.run(debug=True)