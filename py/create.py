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
    <h3 class="error_msg">You must have an account to create flashcards</h3>
    <p><a href="py/signup.py" class="alt">Don't have an account? Click here to create one!</a></p>
    <p><a href="py/login.py" class="alt">Already have an account? Click here to log in!</a></p>
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
    pw += query["password"].value
except:
    print(not_loggedin)

default = """
<!DOCTYPE html>
<html>
<head>
  <title>Create Flashcards</title>
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
      <li><a href="" class="active">Create</a></li>
      <li><a href='display.py?username=""" + user + "&password=" + pw + """' class="menuitem">Study</a></li>
      <li><a href='add.py?username=""" + user + "&password=" + pw + """' class="menuitem">Add</a></li>
    </ul>
  </div>
  <main>
    <h3 class="title">Create flashcards</h3>
    <form name="input" method="GET" action="create.py">
      <input type="text" name="username" value='""" + user + """' class="username" readonly>
      <input type="text" name="password" value='""" + pw + """' class="username" readonly>
      <div class="field collection_div">
        <p>Collection Name</p>
        <input type="text" name="collection" class="collection">
      </div>
      <div class="field">
        <p>Term</p>
        <input type="text" name="term1" class="term">
        <p>Definition</p>
        <input type="text" name="definition1" class="definition">
      </div>
      <div class="field">
        <p>Term</p>
        <input type="text" name="term2" class="term">
        <p>Definition</p>
        <input type="text" name="definition2" class="definition">
      </div>
      <div class="field">
        <p>Term</p>
        <input type="text" name="term3" class="term">
        <p>Definition</p>
        <input type="text" name="definition3" class="definition">
      </div>
      <div class="field">
        <p>Term</p>
        <input type="text" name="term4" class="term">
        <p>Definition</p>
        <input type="text" name="definition4" class="definition">
      </div>
      <div class="field">
        <p>Term</p>
        <input type="text" name="term5" class="term">
        <p>Definition</p>
        <input type="text" name="definition5" class="definition">
      </div>
      <div class="field">
        <p>Term</p>
        <input type="text" name="term6" class="term">
        <p>Definition</p>
        <input type="text" name="definition6" class="definition">
      </div>
      <div class="field">
        <p>Term</p>
        <input type="text" name="term7" class="term">
        <p>Definition</p>
        <input type="text" name="definition7" class="definition">
      </div>
      <div class="field">
        <p>Term</p>
        <input type="text" name="term8" class="term">
        <p>Definition</p>
        <input type="text" name="definition8" class="definition">
      </div>
      <div class="field">
        <p>Term</p>
        <input type="text" name="term9" class="term">
        <p>Definition</p>
        <input type="text" name="definition9" class="definition">
      </div>
      <div class="field">
        <p>Term</p>
        <input type="text" name="term10" class="term">
        <p>Definition</p>
        <input type="text" name="definition10" class="definition">
      </div>
      <input type="submit" value="Create Flashcards" class="submit">
    </form>
  </main>
</body>
</html>
"""

status_0 = """
<!DOCTYPE html>
<html>
<head>
  <title>Create Flashcards</title>
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
      <li><a href="" class="active">Create</a></li>
      <li><a href='display.py?username=""" + user + "&password=" + pw + """' class="menuitem">Study</a></li>
      <li><a href='add.py?username=""" + user + "&password=" + pw + """' class="menuitem">Add</a></li>
    </ul>
  </div>
  <main>
    <h3 class="success">Success</h3>
    <h3 class="success_msg">Successfully created flashcards</h3>
    <a href='display.py?username=""" + user + "&password=" + pw + """' class="alt">Click here to start studying</a>
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
      <li><a href='login.py?username=""" + user + "&password=" + pw + """' class='menuitem'>Home</a></li>
      <li><a href="" class="active">Create</a></li>
      <li><a href='display.py?username=""" + user + "&password=" + pw + """' class="menuitem">Study</a></li>
      <li><a href='add.py?username=""" + user + "&password=" + pw + """' class="menuitem">Add</a></li>
    </ul>
  </div>
  <main>
    <h3 class="error">Error</h3>
    <h3 class="error_msg">You already have a collection under the same name</h3>
  </main>
</body>
</html>
"""

status_2 = """
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
      <li><a href='login.py?username=""" + user + "&password=" + pw + """' class='menuitem'>Home</a></li>
      <li><a href="" class="active">Create</a></li>
      <li><a href='display.py?username=""" + user + "&password=" + pw + """' class="menuitem">Study</a></li>
      <li><a href='add.py?username=""" + user + "&password=" + pw + """' class="menuitem">Add</a></li>
    </ul>
  </div>
  <main>
    <h3 class="error">Error</h3>
    <h3 class="error_msg">You did not input at least 1 term and definition</h3>
  </main>
</body>
</html>
"""

status_3 = """
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
      <li><a href='login.py?username=""" + user + "&password=" + pw + """' class='menuitem'>Home</a></li>
      <li><a href="" class="active">Create</a></li>
      <li><a href='display.py?username=""" + user + "&password=" + pw + """' class="menuitem">Study</a></li>
      <li><a href='add.py?username=""" + user + "&password=" + pw + """' class="menuitem">Add</a></li>
    </ul>
  </div>
  <main>
    <h3 class="error">Error</h3>
    <h3 class="error_msg">At least one term does not have a corresponding definition</h3>
  </main>
</body>
</html>
"""

status_4 = """
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
      <li><a href='login.py?username=""" + user + "&password=" + pw + """' class='menuitem'>Home</a></li>
      <li><a href="" class="active">Create</a></li>
      <li><a href='display.py?username=""" + user + "&password=" + pw + """' class="menuitem">Study</a></li>
      <li><a href='add.py?username=""" + user + "&password=" + pw + """' class="menuitem">Add</a></li>
    </ul>
  </div>
  <main>
    <h3 class="error">Error</h3>
    <h3 class="error_msg">You cannot use commas in either your terms, definitions, or collection name</h3>
  </main>
</body>
</html>
"""
pages = [status_0, status_1, status_2, status_3, status_4]

# For local testing
# query = {"term1":"H","term2":"Cu","term3":"Zn","definition1":"hydrogen","definition2":"copper","definition3":"zinc","collection":"chem"}
# query_ls = []

def setup():
    for i in query:
        if i != "collection" and i != "username" and i != "password":
            query_ls.extend([i, query[i].value])


def crt_flashcards(category):
    to_write = ""
    idx = 1
    error = False
    while idx <= len(query_ls)/4:
        term = query_ls[query_ls.index("term" + str(idx))+1]
        #Inputted term
        definition = query_ls[query_ls.index("definition" + str(idx))+1]
        #Inputted definition
        if term.find(",") == -1 and definition.find(",") == -1:
        #Filter out terms and definitions with commas because we are using csv files to store data
            to_write += user + "," + category + "," + term + "," + definition + "\n"
            #Cards are stored in format <user>,<collection>,<term>,<definition>
        else:
            error = True
            #If any of the terms or definitions have a comma, tell parent function so they are not written
        idx += 1
    return [to_write, error]


def status():
    collection = query["collection"].value
    results = crt_flashcards(collection)
    if results[1] or collection.find(",") != -1:
        return 4
        #If any of ther terms, or definitions, or the collection have a comma, then exit the function and dont write anything
    file = open("../flashcards.csv", "r")
    lines = file.readlines()
    file.close()
    for line in lines:
        line = line.split(",")
        if len(line) >= 2:
            if line[1] == collection and line[0] == user:
                return 1
                #Collection already exists under this user
    if not query_ls:
        return 2
        #If list of values of query string is empty then return an error
    if len(query_ls)%4:
        return 3
        #If at least one term does not have a definition (or vice versa)
    file = open("../flashcards.csv", "a")
    file.write(results[0])
    file.close()
    return 0


try:
    if user and pw:
        setup()
        print(pages[status()])
except:
    print(default)
