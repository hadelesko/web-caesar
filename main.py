#from helpers import alphabet_position, rotate_character
from flask import Flask, request,redirect
from caesar import rotate_string
app= Flask(__name__)
app.config['DEBUG']= True
page_header="""
<!DOCTYPE html>
<html>
    <body>
"""
page_footer="""
      </body>
</html>   
"""

form   =   """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
    
      <!-- create your form here -->
      <form  method="post">
                <div>
                        <label  >Rotate by:</label> 
                        <input type="text" name="rot" value="0">
                </div>
                <textarea  type ="text"   name = "text" />{0}</textarea><br>        
                <input type="submit" />
     </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return   form.format('text') #default return value of form.format("text") /  form.format("rot")
@app.route("/",  methods  =  ['POST'])
def encrypt():
    
    text   =   request.form['text']          ## get text from the form
    rot     =   int(request.form['rot'] )   ## get the rotation from the form
                                                          ##  and parse it into integer
    new_text   =   ""                             ##  Initialisation of the encrypted text to empty string

    # Building the new text
    
    for char in text:
        new_text=new_text+rotate_string(char, rot)
        
    ## encrypted text
     
    content=form.format(new_text)
    #content= 'Rotating  "' + text+ '    gives  ' +'  "' +form.format(new_text)+'"
    return content

app.run()
