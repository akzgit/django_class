#activate the virtual environment
from flask import Flask,request,redirect,url_for,render_template #flask - package, Flask -module/class
from flask_mysqldb import MySQL #pip install flask_mysqldb ->flsk and mysqldb are classes imported from a package
app =Flask(__name__)    #app is the object , __name__ variable/argument

#configuration of databse
app.config['MYSQL_HOST']='localhost'
# app.config['MYSQLPORT']=3307 #for diffeent port
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='root'
app.config['MYSQL_DB']='flaskDBX' #after creating the database

mysql=MySQL(app) #connectivity between flask and mysql

@app.route('/') #default page
def Homepage():
    return render_template('Home.html') #render_template is used to render from the template folder

@app.route('/about')
def about():
    return render_template('Aboutus.html')

@app.route('/comments')
def display_comments():
    return render_template('contact.html')

@app.route('/comments', methods=['GET', 'POST'])
def add_comments():
    if request.method == 'POST':
        ufeedback = request.form['feedback']
        cur = mysql.connection.cursor()
        cur.execute('''insert into feedbackdetails(feedback) values(%s)''', (ufeedback,))
        mysql.connection.commit()
        cur.close()
        comments_html = get_comments()  # Get updated comments HTML
        return render_template('contact.html', comments=comments_html)  # Return to contact.html with comments

    return redirect(url_for('display_comments'))

@app.route('/get_comments', methods=['GET'])
def get_comments():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT feedback FROM feedbackdetails''')
    comments = [row[0] for row in cur.fetchall()]
    cur.close()

    comments_html = '<ul>'
    for comment in comments:
        comments_html += '<li>' + comment + '</li>'
    comments_html += '</ul>'

    return comments_html




if __name__ =='__main__':
    app.run(debug = True)