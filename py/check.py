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
collection = query["collection"].value
try:
    user += query["username"].value
    pw += query["password"].value
except:
    print(not_loggedin)


def setup():
    counter = 0
    for i in query:
        if i != "collection" and i != "username" and i != "password":
            if "definition" in i:
                counter += 1
                #Count the number of terms the user was asked for
            query_ls.extend([i, query[i].value])
    return counter


html = ""
def check_answers():
    file = open("../flashcards.csv", "r")
    lines = file.readlines()
    file.close()
    html_str = ""
    cards = []
    idx = 1
    for line in lines:
        line = line[:-1].split(",")
        if line[0] == user and line[1] == collection:
        #If creator and collection of card math the current user and collection, then add a list containing the term and definition of the card to the list of cards
            cards.append([line[2], line[3]])
    #Cards in the file are stored in order of creation
    #This is the same order that they are displayed in
    #This means that the first card will correspond to the first answer that the user inputs, the second to the second answer, and so on
    while idx <= flashcards:
        guess = ""
        card = cards[idx-1]
        try:
            guess = query_ls[query_ls.index("term" + str(idx))+1]
            #if user does not answer the question, this would give an error, so we enclosed it in a try block
        except:
            guess = ""
        if guess.lower() == card[0].lower() and query_ls[query_ls.index("definition" + str(idx))+1] == card[1]:
            html_str += "<div class='container'><div class='flashcard correct'><h4>Correct</h4><p class='definition'>Definition: " + card[1] + "</p><input type='text' class='term' value='" + guess + "' readonly></div></div>"
        else:
            html_str += "<div class='container'><div class='flashcard incorrect'><h4>Incorrect</h4><p class='definition'>Definition: " + card[1] + "</p><input type='text' class='term' value='" + guess + "' readonly></div></div>"
        idx += 1
    return html_str


flashcards = setup()
results = check_answers()
page = """
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
    """ + results + """
  </main>
</body>
</html>
"""
print(page)
