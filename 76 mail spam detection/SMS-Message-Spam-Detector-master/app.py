from flask import Flask, render_template, url_for, request, session
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
import pymysql
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib

connection = pymysql.connect(host="localhost", user="root", password="", database="spammail")
cursor = connection.cursor()

app = Flask(__name__)
app.secret_key = 'random string'


@app.route('/')
def home():
    return render_template('index1.html')
@app.route('/sendmail1')
def sendmail1():
    return render_template('sendmail.html',username=session['user'])



@app.route('/sendmail')
def sendmail():
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        username = request.form.get("username")

        password = request.form.get("password")

        # print("insert into userdetails(fname, lname, password) values('"+fname+"','"+lname+",'"+password+")")

        # cursor.execute("insert into userdetails(fname, lname, password) values(:fname, :lname, :password)",{"fname":fname,"lname":fname,"password":password})
        cursor.execute(
            "insert into userdetails(name, phone, username ,password) values('" + name + "','" + phone + "','" + username + "','" + password + "')")

        connection.commit()

        return render_template("login.html")
    else:
        return render_template("about.html")

    return render_template('sendmail.html')


@app.route('/logout')
def logout():
    return render_template('index1.html')
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/register1', methods=["POST", "GET"])
def register1():
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        username = request.form.get("username")

        password = request.form.get("password")
        msg = 'Successfully Register plz login now'
        # print("insert into userdetails(fname, lname, password) values('"+fname+"','"+lname+",'"+password+")")

        # cursor.execute("insert into userdetails(fname, lname, password) values(:fname, :lname, :password)",{"fname":fname,"lname":fname,"password":password})
        cursor.execute(
            "insert into userdetails(name, phone, username ,password) values('" + name + "','" + phone + "','" + username + "','" + password + "')")

        connection.commit()

        return render_template("index1.html",msg=msg)


@app.route('/foo')
def foo():
    username = session['user']
    cursor.execute('SELECT * FROM sendmail WHERE sendermail = %s ', (username))

    print(cursor.execute)
    data = cursor.fetchall()  # data from database
    msg = 'Incorrect username/password!'
    return render_template("alldata.html", value=data)
@app.route('/recieved')
def recieved():
    username = session['user']
    cursor.execute('SELECT * FROM sendmail WHERE recievermail = %s ', (username))

    print(cursor.execute)
    data = cursor.fetchall()  # data from database
    msg = 'Incorrect username/password!'
    return render_template("alldata.html", value=data)
@app.route('/predict', methods=['POST'])
def predict():
    df = pd.read_csv("spam.csv", encoding="latin-1")
    df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
    # Features and Labels
    df['label'] = df['class'].map({'ham': 0, 'spam': 1})
    X = df['message']
    y = df['label']

    # Extract Feature With CountVectorizer
    cv = CountVectorizer()
    X = cv.fit_transform(X)  # Fit the Data
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    # Naive Bayes Classifier
    from sklearn.naive_bayes import MultinomialNB

    clf = MultinomialNB()
    clf.fit(X_train, y_train)
    clf.score(X_test, y_test)
    # Alternative Usage of Saved Model
    # joblib.dump(clf, 'NB_spam_model.pkl')
    # NB_spam_model = open('NB_spam_model.pkl','rb')
    # clf = joblib.load(NB_spam_model)

    if request.method == 'POST':
        sendermail = request.form.get("sendermail")

        recievermail = request.form.get("recievermail")

        message = request.form.get("message")
        data = [message]
        vect = cv.transform(data).toarray()
        myprediction = clf.predict(vect)
        if myprediction == [1]:
            checkstatus="spam"
        elif myprediction == [0]:
            checkstatus="not spam"
        cursor = connection.cursor()
        cursor.execute(
            "insert into sendmail(sendermail, recievermail, message,myprediction) values('" + sendermail + "','" + recievermail + "','" + message + "','" + checkstatus + "')")
        connection.commit()
        print(cursor.execute)

        return render_template("sendmail.html")


@app.route('/login1', methods=["POST", "GET"])
def login1():
    if request.method == "POST":

        username = request.form.get("username")

        password = request.form.get("password")

        cursor.execute('SELECT * FROM userdetails WHERE username = %s AND password = %s', (username, password))
        # Fetch one record and return result
        account = cursor.fetchone()
        print(account)

        # If account exists in accounts table in out database
        if account:

            session['user'] = account[2]
            msg = 'Logged in successfully'

            return render_template('sendmail.html', username=session['user'])
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
        # Show the login form with message (if any)6
    return render_template('index1.html', msg=msg)


if __name__ == '__main__':
    app.run(debug=True)
