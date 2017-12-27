from flask import Flask, request, redirect, render_template
import cgi
import os



app = Flask(__name__)

app.config['DEBUG'] = True      

@app.route("/")
def index():
    return render_template('homepage.html')

@app.route("/confirmation",methods=['POST'])
def confirmation(Username):
    username= request.form['Username']
    return render_template('confirmation.html',name=username)


@app.route('/', methods=['POST'])
def validate_login():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    error_name=""
    password_error=""
    verify_error=""
    error_pass_same=""
    email_error=""
    password1=""

    
    if password == "":
       password_error = "'{0}'please specify the password".format(password)
       password=""
    else:
        if len(password) > 20:
           password_error = "password lenght is more than 20 Characters"
           password1=password
           password = ""
        else:
            if len(password) < 3:
              password_error = "password is less than 3 characters"
              password1=password
              password=""
            else:
              password = password
    if verify == "":
       error_pass_same = "'{0}'password re-enter is empty".format(verify)
       verify=""
       password=""
    else:
        if verify != password:
           if password1 == verify : 
              verify =""
              password=""
           else:
              error_pass_same = "Password did not match "
              verify =""
              password=""
        else:
            if verify == password : 
               if password1 != "" :
                   password = ""
                   verify = ""
    if password == "":
        verify = ""
    else:
        verify = verify
    if email != '':
        if " " in email:
            email_error = "Not a valid email address - please re-enter"
            
        elif "@" not in email: 
            email_error = "Not a valid email address - please re-enter"
            
        elif "." not in email:
            email_error = "Not a valid email address - please re-enter"
            
        elif len(email) < 3 or len(email) > 20:
            email_error = "Email must be 3-20 characters long"        
            
    else:
        email = ""   


   
    
    if username == "":
       error_name = "'{0}'please specify the username".format(username)
       username=""
       
    else:
        if len(username) > 20:
           error_name = "username should not be more than 20 characters"
           username=""
           
        else:
            if len(username) < 3 :
               error_name = "username should be min 3 letters"
               username=""
               
            else:
                username = username
    
    if not error_name and not password_error and not error_pass_same and not email_error :
        return render_template('confirmation.html',username=username)
    else:    
        return render_template('homepage.html', username=username, password=password,
            verify=verify,
            email=email,
            error_name=error_name,
            password_error=password_error,
            error_pass_same=error_pass_same,
            email_error=email_error)
app.run()