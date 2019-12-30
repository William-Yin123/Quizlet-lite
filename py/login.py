#!/usr/bin/python3
print("Content-Type: text/html\n")
print('')


import cgi
import cgitb
cgitb.enable()

default = """
<!DOCTYPE html>
<html>
<head>
  <title>Log in</title>
  <link href="../css/login.css" rel="stylesheet" type="text/css"/>
  <link href="https://fonts.googleapis.com/css?family=Neuton&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Kaushan+Script&display=swap" rel="stylesheet">
  <link rel="shortcut icon" href="../images/icon.ico"/>
</head>
<body>
  <header>
    <h1>
      <a href="https://quizlet.com/" title="Click me to avoid this trainwreck of a website!">Quizlet</a>
      <span class="unofficial" title="It's like real quizlet, but a lot worse!">-lite</span>
    </h1>
  </header>
  <main>
    <h3>Login</h3>
    <form name="input" method="GET" action="login.py">
      <div class="input_field">
        <p class="field">Username</p>
        <input type="text" name="username">
      </div>
      <div class="input_field">
        <p class="field">Password</p>
        <input type="password" name="password">
      </div>
      <input class="submit" type="submit" value="Log in">
    </form>
    <a href="signup.py" class="alt" title="The worst decision you ever made...">Don't have an account? Sign up!</a>
  </main>
</body>
</html>
"""

query = cgi.FieldStorage()
user = ""
pw = ""


def verification():
    file = open("../users.csv", "r")
    users = file.readlines()
    file.close()
    username = query["username"].value
    password = query["password"].value
    for user in users:
        user = user[:-1].split(",") # takes the username from the csv file(named users.csv) and the password and separates them into different items in the list
        if username == user[0]: #checks to see if the username inputted matches one in the csv file
            if password == user[1]:#if the username exists, it checks to see if the passwords match
                return [0, username, password] #returns the first status, which means you have successfully logged in
            else:
                return [1, username, password] #if the usrname is correct, but not the password, it will show an error message saying the password is incorrect
    return [2, username, password] #this happens if the username they inputted doesn't exist in the csv file

status = -1
try:
    results = verification()
    status = results[0] #outputs the html for the specified conditions(status)
    user += results[1] #index 1 of the return list is the username
    pw += results[2] #index 2 of the return list is the password
except:
    print(default)


status_0 = """
<!DOCTYPE html>
<html>
<head>
  <title>""" + user + """'s Homepage</title>
  <link href="../css/homepage.css" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Neuton&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Kaushan+Script&display=swap" rel="stylesheet">
  <link rel="shortcut icon" href="../images/icon.ico"/>
</head>
<body>
  <header>
    <h3><a href="https://quizlet.com/">Quizlet</a><span class="unofficial">-lite</span></h3>
  </header>
  <div class="navbar">
    <ul class="menu">
      <li><a href="" class='active'>Home</a></li>
      <li><a href='create.py?username=""" + user + "&password=" + pw + """' class="menuitem">Create</a></li>
      <li><a href='display.py?username=""" + user + "&password=" + pw + """' class="menuitem">Study</a></li>
      <li><a href='add.py?username=""" + user + "&password=" + pw + """' class="menuitem">Add</a></li>
    </ul>
  </div>
  <main>
    <h3 class="title">Homepage</h3>
    <p>Welcome to Quizlet-lite """ + user + """, the online study service where you can create, store, and view digital flashcards created by you.</p>
    <p>Get started by choosing an option on the menu to the left.</p>
    <p>If at any time you find yourself in need of an actually decent website, you can always click on the Quizlet logo on the upper left hand corner to go to the real Quizlet. I highly recommend it as it is free, easy to use, and has several options that will help you study for that tough test coming up.</p>
  </main>
</body>
</html>
"""

status_1 = """
<!DOCTYPE html>
<html>
<head>
  <title>Log in</title>
  <link href="../css/login.css" rel="stylesheet" type="text/css"/>
  <link href="https://fonts.googleapis.com/css?family=Neuton&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Kaushan+Script&display=swap" rel="stylesheet">
  <link rel="shortcut icon" href="../images/icon.ico"/>
</head>
<body>
  <header>
    <h1>
      <a href="https://quizlet.com/" title="Click me to avoid this trainwreck of a website!">Quizlet</a>
      <span class="unofficial" title="It's like real quizlet, but a lot worse!">-lite</span>
    </h1>
  </header>
  <main>
    <h3>Login</h3>
    <h3 class="error">Error: Incorrect password</h3>
    <form name="input" method="GET" action="login.py">
      <div class="input_field">
        <p class="field">Username</p>
        <input type="text" name="username">
      </div>
      <div class="input_field">
        <p class="field">Password</p>
        <input type="password" name="password">
      </div>
      <input class="submit" type="submit" value="Log in">
    </form>
    <a href="signup.py" class="alt" title="The worst decision you ever made...">Don't have an account? Sign up!</a>
  </main>
</body>
</html>
"""

status_2 = """
<!DOCTYPE html>
<html>
<head>
  <title>Log in</title>
  <link href="../css/login.css" rel="stylesheet" type="text/css"/>
  <link href="https://fonts.googleapis.com/css?family=Neuton&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Kaushan+Script&display=swap" rel="stylesheet">
  <link rel="shortcut icon" href="../images/icon.ico"/>
</head>
<body>
  <header>
    <h1>
      <a href="https://quizlet.com/" title="Click me to avoid this trainwreck of a website!">Quizlet</a>
      <span class="unofficial" title="It's like real quizlet, but a lot worse!">-lite</span>
    </h1>
  </header>
  <main>
    <h3>Login</h3>
    <h3 class="error">Error: User does not exist</h3>
    <form name="input" method="GET" action="login.py">
      <div class="input_field">
        <p class="field">Username</p>
        <input type="text" name="username">
      </div>
      <div class="input_field">
        <p class="field">Password</p>
        <input type="password" name="password">
      </div>
      <input class="submit" type="submit" value="Log in">
    </form>
    <a href="signup.py" class="alt" title="The worst decision you ever made...">Don't have an account? Sign up!</a>
  </main>
</body>
</html>
"""
pages = [status_0, status_1, status_2]

if status != -1: #checks to see if one of the conditions is met.
    print(pages[status])
