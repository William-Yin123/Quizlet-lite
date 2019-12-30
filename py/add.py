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
#tries to add the username inputted and sets it as the string user, adds the password inputted and sets it to the string pw.
    user += query["username"].value
    pw += query["password"].value
except:
#if the query string doesn't have a username and password(or in this case nothing in the query string)
    print(not_loggedin)
    #prints error message(not_loggedin) to tell the user that they must log in first

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
      <li><a href='create.py?username=""" + user + "&password=" + pw + """' class="menuitem">Create</a></li>
      <li><a href='display.py?username=""" + user + "&password=" + pw + """' class="menuitem">Study</a></li>
      <li><a href="" class="active">Add</a></li>
    </ul>
  </div>
  <main>
    <h3 class="title">Add to an existing collection</h3>
    <form name="input" method="GET" action="add.py">
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
      <li><a href='create.py?username=""" + user + "&password=" + pw + """' class="menuitem">Create</a></li>
      <li><a href='display.py?username=""" + user + "&password=" + pw + """' class="menuitem">Study</a></li>
      <li><a href="" class="active">Add</a></li>
    </ul>
  </div>
  <main>
    <h3 class="success">Success</h3>
    <h3 class="success_msg">Successfully added flashcards</h3>
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
      <li><a href='create.py?username=""" + user + "&password=" + pw + """' class="menuitem">Create</a></li>
      <li><a href='display.py?username=""" + user + "&password=" + pw + """' class="menuitem">Study</a></li>
      <li><a href="" class="active">Add</a></li>
    </ul>
  </div>
  <main>
    <h3 class="error">Error</h3>
    <h3 class="error_msg">You do not have a collection with that name</h3>
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
      <li><a href='create.py?username=""" + user + "&password=" + pw + """' class="menuitem">Create</a></li>
      <li><a href='display.py?username=""" + user + "&password=" + pw + """' class="menuitem">Study</a></li>
      <li><a href="" class="active">Add</a></li>
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
      <li><a href='create.py?username=""" + user + "&password=" + pw + """' class="menuitem">Create</a></li>
      <li><a href='display.py?username=""" + user + "&password=" + pw + """' class="menuitem">Study</a></li>
      <li><a href="" class="active">Add</a></li>
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
      <li><a href='create.py?username=""" + user + "&password=" + pw + """' class="menuitem">Create</a></li>
      <li><a href='display.py?username=""" + user + "&password=" + pw + """' class="menuitem">Study</a></li>
      <li><a href="" class="active">Add</a></li>
    </ul>
  </div>
  <main>
    <h3 class="error">Error</h3>
    <h3 class="error_msg">You may not use commas in your terms and definitions</h3>
  </main>
</body>
</html>
"""
pages = [status_0, status_1, status_2, status_3, status_4]
#sets pages to the three possible website pages that will occur when a user is signed in.

def setup():
    for i in query: #looks through the cgi.Fieldstorage
        if i != "collection" and i != "username" and i != "password": #if the item in cgi.FieldStorage is not the username, password or collection name
            query_ls.extend([i, query[i].value]) #add it to the end of query_ls(list) so that all the terms and definitions can be assessed later
            #in the format (<term1>, <term1_name>, <defition1>, <defintion1_name> ...) so that order of the flashcards created can be kept


#function that will input the terms and definitions into a csv file in the specific format.
def crt_flashcards(category):
    to_write = ""
    idx = 1
    error = False
    while idx <= len(query_ls)/4: #divide by 4 because each term and defintion pair is composed of 4 item(mentioned above)
        try:
            term = query_ls[query_ls.index("term" + str(idx))+1]
            definition = query_ls[query_ls.index("definition" + str(idx))+1]
            if term.find(",") == -1 and definition.find(",") == -1:
            #Filters out terms and definitions with commas because they interfere with how we are storing the flashcards
                to_write += user + "," + category + "," + term + "," + definition + "\n"
                #Creates format: <username>,<collection>,<term>,<defintion>
                #adds 1 to idx so that you get the term's name, not the number of the term(also for defintion).
            else:
                error = True
            idx += 1
        except:
            idx += 1
    return [to_write, error]


#determines which page to output if the user has been signed in
def status():
    collection = query["collection"].value
    results = crt_flashcards(collection)
    if results[1]:
    #If there was a comma in a term or definition then exit the function and return the error page to the user
        return 4
    file = open("../flashcards.csv", "r")
    lines = file.readlines()
    file.close()
    for line in lines:
        line = line.split(",") #splits the list by the commas
        if len(line) >= 2: #if there are more than or equal to 2 terms and defintion pairs created
            if line[1] == collection and line[0] == user: #checks to see if the first term is the username and the second is the collection name
                file = open("../flashcards.csv", "a") #allows us to add to flashcards.csv
                file.write(results[0]) #takes which collection the user wants to add to
                #and creates new lines in the csv file
                file.close()
                return 0 #returns status_0 which says that you have successfully added last cards
    if not query_ls: #if there is no query_ls present. This means that no term or definition already exists in the collection.
        return 2 #outputs the error that a term or definition has not been inputted
    if len(query_ls)%4: #in query_ls, each term and definition comes in 4's, thus if everything is inputted correctly, the list should be divisible by 4
        return 3 #means that either a term or definition isnt matched properly
    return 1 #if none of this works, that means that there is no collection that has been created under the specified name


try:
    if user and pw: #this makes sure that the user is signed in
        setup()
        print(pages[status()])
except:
    print(default)
