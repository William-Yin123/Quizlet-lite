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
  <title>Create Account</title>
  <link href="../css/login.css" rel="stylesheet" type="text/css"/>
  <link href="https://fonts.googleapis.com/css?family=Neuton&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Kaushan+Script&display=swap" rel="stylesheet">
  <link rel="shortcut icon" href="../images/icon.ico"/>
</head>
<body>
  <header>
    <h1>
      <a href="https://quizlet.com/" class="escape"><span title="Click me to avoid this trainwreck of a website!">Quizlet</span></a>
      <span class="unofficial" title="It's like real quizlet, but a lot worse!">-lite</span>
    </h1>
  </header>
  <main>
    <h3>Create Account</h3>
    <form name="input" method="GET" action="signup.py">
      <div class="input_field">
        <p class="field">Username</p>
        <input type="text" name="username">
      </div>
      <div class="input_field">
        <p class="field">Password</p>
        <input type="password" name="password">
      </div>
      <div class="input_field">
        <p class="field">Confirm Password</p>
        <input type="password" name="confirm_password">
      </div>
      <input class="submit" type="submit" value="Sign up">
    </form>
    <a href="login.py" class="alt" title="Why...">Already have an account? Log in!</a>
  </main>
</body>
</html>
"""

status_0 = """
<!DOCTYPE html>
<html>
<head>
  <title>Create Account</title>
  <link href="../css/login.css" rel="stylesheet" type="text/css"/>
  <link href="https://fonts.googleapis.com/css?family=Neuton&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Kaushan+Script&display=swap" rel="stylesheet">
  <link rel="shortcut icon" href="../images/icon.ico"/>
</head>
<body>
  <header>
    <h1>
      <a href="https://quizlet.com/" class="escape"><span title="Click me to avoid this trainwreck of a website!">Quizlet</span></a>
      <span class="unofficial" title="It's like real quizlet, but a lot worse!">-lite</span>
    </h1>
  </header>
  <main>
    <h3 class="success">Account Created</h3>
    <a href="login.py" class="alt">Click here to login and start studying!</a>
  </main>
</body>
</html>
"""

status_1 = """
<!DOCTYPE html>
<html>
<head>
  <title>Create Account</title>
  <link href="../css/login.css" rel="stylesheet" type="text/css"/>
  <link href="https://fonts.googleapis.com/css?family=Neuton&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Kaushan+Script&display=swap" rel="stylesheet">
  <link rel="shortcut icon" href="../images/icon.ico"/>
</head>
<body>
  <header>
    <h1>
      <a href="https://quizlet.com/" class="escape"><span title="Click me to avoid this trainwreck of a website!">Quizlet</span></a>
      <span class="unofficial" title="It's like real quizlet, but a lot worse!">-lite</span>
    </h1>
  </header>
  <main>
    <h3>Create Account</h3>
    <h3 class="error">Error: Passwords do not match</h3>
    <form name="input" method="GET" action="signup.py">
      <div class="input_field">
        <p class="field">Username</p>
        <input type="text" name="username">
      </div>
      <div class="input_field">
        <p class="field">Password</p>
        <input type="password" name="password">
      </div>
      <div class="input_field">
        <p class="field">Confirm Password</p>
        <input type="password" name="confirm_password">
      </div>
      <input class="submit" type="submit" value="Sign up">
    </form>
    <a href="login.py" class="alt" title="Why...">Already have an account? Log in!</a>
  </main>
</body>
</html>
"""

status_2 = """
<!DOCTYPE html>
<html>
<head>
  <title>Create Account</title>
  <link href="../css/login.css" rel="stylesheet" type="text/css"/>
  <link href="https://fonts.googleapis.com/css?family=Neuton&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Kaushan+Script&display=swap" rel="stylesheet">
  <link rel="shortcut icon" href="../images/icon.ico"/>
</head>
<body>
  <header>
    <h1>
      <a href="https://quizlet.com/" class="escape"><span title="Click me to avoid this trainwreck of a website!">Quizlet</span></a>
      <span class="unofficial" title="It's like real quizlet, but a lot worse!">-lite</span>
    </h1>
  </header>
  <main>
    <h3>Create Account</h3>
    <h3 class="error">Error: That username is already in use</h3>
    <form name="input" method="GET" action="signup.py">
      <div class="input_field">
        <p class="field">Username</p>
        <input type="text" name="username">
      </div>
      <div class="input_field">
        <p class="field">Password</p>
        <input type="password" name="password">
      </div>
      <div class="input_field">
        <p class="field">Confirm Password</p>
        <input type="password" name="confirm_password">
      </div>
      <input class="submit" type="submit" value="Sign up">
    </form>
    <a href="login.py" class="alt" title="Why...">Already have an account? Log in!</a>
  </main>
</body>
</html>
"""

status_3 = """
<!DOCTYPE html>
<html>
<head>
  <title>Create Account</title>
  <link href="../css/login.css" rel="stylesheet" type="text/css"/>
  <link href="https://fonts.googleapis.com/css?family=Neuton&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Kaushan+Script&display=swap" rel="stylesheet">
  <link rel="shortcut icon" href="../images/icon.ico"/>
</head>
<body>
  <header>
    <h1>
      <a href="https://quizlet.com/" class="escape"><span title="Click me to avoid this trainwreck of a website!">Quizlet</span></a>
      <span class="unofficial" title="It's like real quizlet, but a lot worse!">-lite</span>
    </h1>
  </header>
  <main>
    <h3>Create Account</h3>
    <h3 class="error">Error: Your username and password may not contain commas</h3>
    <form name="input" method="GET" action="signup.py">
      <div class="input_field">
        <p class="field">Username</p>
        <input type="text" name="username">
      </div>
      <div class="input_field">
        <p class="field">Password</p>
        <input type="password" name="password">
      </div>
      <div class="input_field">
        <p class="field">Confirm Password</p>
        <input type="password" name="confirm_password">
      </div>
      <input class="submit" type="submit" value="Sign up">
    </form>
    <a href="login.py" class="alt" title="Why...">Already have an account? Log in!</a>
  </main>
</body>
</html>
"""
pages = [status_0, status_1, status_2, status_3]


query = cgi.FieldStorage()


def create_acc():
    #the query[stuff] are all areas that the user needs to fill in to signup.
    username = query["username"].value
    password = query["password"].value
    password2 = query["confirm_password"].value
    if password != password2: #if the password in the first field doesn't match the second field
        return 1 #tells the user that the passwords do not match in both fields, and brings them back to the signup page
    #if all passwords match, we go on to check if the username is already used.
    if username.find(",") != -1 or password.find(",") != -1:
    #Filter our names or passwords with commas as they would interfere with how we are saving them
        return 3
    file = open("../users.csv", "r")
    users = file.readlines()
    file.close()
    for user in users: #user would be the usernames of all the everyone that has already created an account
        user = user[:-1].split(",")#takes the username only(not the password) and gets rid of the comma
        if user[0] == username: #checks to see if the inputted username(for signup) is also found in the csv file
            return 2 #if these two usernames are the same, an error message will show saying the username is already taken
    file = open("../users.csv", "a")
    file.write(username + "," + password + "\n")
    file.close()
    return 0 #if everything checks out, the account is created!


try:
    print(pages[create_acc()])
except:
    print(default)
