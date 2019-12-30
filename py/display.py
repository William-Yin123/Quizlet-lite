#!/usr/bin/python3
print("Content-Type: text/html\n")
print('')

import cgi
import cgitb
cgitb.enable()


not_loggedin = """
<!DOCTYPE html>
<html>
<head>
  <title>Error</title>
  <link href="../css/login.css" rel="stylesheet" type="text/css"/>
  <link href="https://fonts.googleapis.com/css?family=Neuton&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Kaushan+Script&display=swap" rel="stylesheet">
  <link rel="shortcut icon" href="../images/icon.ico"/>
</head>
<body>
  <header>
    <h1>
      <a href="https://quizlet.com/" class="escape" title="Click me to avoid this trainwreck of a website!">Quizlet</a>
      <span class="unofficial" title="It's like real quizlet, but a lot worse!">-lite</span>
    </h1>
  </header>
  <main>
    <h1 class="error">Error</h1>
    <h3 class="error_msg">You must have an account to view flashcards</h3>
    <a href="py/signup.py" class="alt">Don't have an account? Click here to create one!</a>
    <a href="py/login.py" class="alt">Already have an account? Click here to log in!</a>
  </main>
</body>
</html>
"""

query = cgi.FieldStorage()
query_ls = []
user = ""
pw = ""
try:
    user += query["username"].value
    pw = query["password"].value
except:
    print(not_loggedin)


#Used to find and display user collections
def find_collections():
    file = open("../flashcards.csv", "r")
    cards = file.readlines()
    file.close()
    #Read all the cards so we can find all the collections that belong to the current user
    options = ""
    collections = []
    for card in cards:
        card = card[:-1].split(",")
        if card[0] == user and not card[1] in collections:
        #If card is ownedd by user and the collections the card belongs to has not been displayed yet, then display
            options += "<div class='container'><div class='option'><input type='radio' name='collection' value=" + card[1] + ">" + card[1] + "</div></div>"
            collections.append(card[1])
            #Add to list that keeps track of all the user's collections we have encountered so far
    return options


default = """
<!DOCTYPE html>
<html>
<head>
  <title>Study</title>
  <link href="../css/menu.css" rel="stylesheet" type="text/css"/>
  <link href="https://fonts.googleapis.com/css?family=Neuton&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Kaushan+Script&display=swap" rel="stylesheet">
  <link rel="shortcut icon" href="../images/icon.ico"/>
</head>
<body>
  <header>
    <h3>
      <a href="https://quizlet.com/" class="escape">Quizlet</a>
      <span class="unofficial" title="It's like real quizlet, but a lot worse!">-lite</span>
    </h3>
  </header>
  <div class="navbar">
    <ul class="menu">
      <li><a href='login.py?username=""" + user + "&password=" + pw + """' class='menuitem'>Home</a></li>
      <li><a href='create.py?username=""" + user + "&password=" + pw + """' class="menuitem">Create</a></li>
      <li><a href="" class="active">Study</a></li>
      <li><a href='add.py?username=""" + user + "&password=" + pw + """' class="menuitem">Add</a></li>
    </ul>
  </div>
  <main>
    <h3 class="title">Choose a collection of flashcards to study from</h3>
    <form name="input" method="GET" action="display.py">
      <input type="text" name="username" value='""" + user + """' class="username" readonly>
      <input type="text" name="password" value='""" + pw + """' class="username" readonly>
      <p>""" + user + """'s Collections</p>
      <div class="select_menu">
        """ + find_collections() + """
      </div>
      <input type="submit" value="Start Studying" class="submit">
    </form>
  </main>
</body>
</html>
"""


to_display = ""
status = -1
collection = ""
def display(html_str, viewing):
    viewing += query["collection"].value
    file = open("../flashcards.csv", "r")
    cards = file.readlines()
    file.close()
    counter = 1
    for card in cards:
        card = card[:-1].split(",")
        if len(card) == 4:
            if card[0] == user and card[1] == viewing:
            #If the card's user field matches the current user and the collection field matches the collection we are viewing then display it
                html_str += "<div class='container'><div class='flashcard'><p class='definition'>Definition: " + card[3] + "</p><input type='text' name='definition" + str(counter) + "' value=" + card[3] + " class='username' readonly><input type='text' name='term" + str(counter)+ "' class='term'></div></div>"
                #Display each card's definition with an input field for them to type the term
                #Create an input for the definition with the value set to the definition of the card and make it readonly(not changeable by user) so that we can get what definition each answer corresponds to
                counter += 1
    if html_str == "":
    #No cards were found
        return [html_str, 1, viewing]
    return [html_str, 0, viewing]


try:
    results = display("", "")
    to_display = results[0]
    status = results[1]
    collection = results[2]
except:
    print(default)

status_0 = """
<!DOCTYPE html>
<html>
<head>
  <title>Studying From """ + collection + """</title>
  <link href="../css/display.css" rel="stylesheet" type="text/css"/>
  <link href="https://fonts.googleapis.com/css?family=Neuton&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Kaushan+Script&display=swap" rel="stylesheet">
  <link rel="shortcut icon" href="../images/icon.ico"/>
</head>
<body>
  <header>
    <h3>
      <a href="https://quizlet.com/" class="escape">Quizlet</a>
      <span class="unofficial" title="It's like real quizlet, but a lot worse!">-lite</span>
    </h3>
  </header>
  <div class="navbar">
    <ul class="menu">
      <li><a href='login.py?username=""" + user + "&password=" + pw + """' class='menuitem'>Home</a></li>
      <li><a href='create.py?username=""" + user + "&password=" + pw + """' class="menuitem">Create</a></li>
      <li><a href="" class="active">Study</a></li>
      <li><a href='add.py?username=""" + user + "&password=" + pw + """' class="menuitem">Add</a></li>
    </ul>
  </div>
  <main>
    <h3 class="title">Viewing flashcards from """ + collection + """</h3>
    <form name="input" method="GET" action="check.py">
      <input type="text" name="username" value='""" + user + """' class="username" readonly>
      <input type="text" name="password" value='""" + pw + """' class="username" readonly>
      <input type="text" name="collection" value='""" + collection + """' class="username" readonly>
      """ + to_display + """
      <input type="submit" value="Check" class="submit">
  </main>
</body>
</html>
"""

status_1 = """
<!DOCTYPE html>
<html>
<head>
  <title>Error</title>
  <link href="../css/menu.css" rel="stylesheet" type="text/css"/>
  <link href="https://fonts.googleapis.com/css?family=Neuton&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Kaushan+Script&display=swap" rel="stylesheet">
  <link rel="shortcut icon" href="../images/icon.ico"/>
</head>
<body>
  <header>
    <h3>
      <a href="https://quizlet.com/" class="escape" title="Click me to avoid this trainwreck of a website!">Quizlet</a>
      <span class="unofficial" title="It's like real quizlet, but a lot worse!">-lite</span>
    </h3>
  </header>
  <div class="navbar">
    <ul class="menu">
      <li><a href="" class='menuitem'>Home</a></li>
      <li><a href='create.py?username=""" + user + "&password=" + pw + """' class="menuitem">Create</a></li>
      <li><a href='display.py?username=""" + user + "&password=" + pw + """' class="active">Study</a></li>
      <li><a href='add.py?username=""" + user + "&password=" + pw + """' class="menuitem">Add</a></li>
    </ul>
  </div>
  <main>
    <h3 class="error">Error</h3>
    <h3 class="error_msg">Collection does not exist</h3>
  </main>
</body>
</html>
"""
pages = [status_0, status_1]

if user and pw and status != -1:
    print(pages[status])
