#from helpers import alphabet_position, rotate_character
from flask import Flask, request,redirect
from caesar import rotate_string
app= Flask(__name__)
app.config['DEBUG']= True

page_header=    """
<!DOCTYPE html>
<html>
    <head><title><p><h1>Encryption: Encrypted text</h1></p></title></head>
    <body>
"""
page_footer  = """
        
    </body>
    </html>
"""
form="""
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
    
      <!-- create your form here -->
      <form action="/rawtext" method="post">
        <label >
          Rotate by:  
            <input type="text" name="rot" value ="0" />
            <textarea  type ="text"   name = "text"  placeholder= "Type your original text "/></textarea>
        </label>
        <input type="submit" value="Submit Querry"/>
    </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form
##def encrypt(text, rot):
##    new_text="" ##  Initialisation of the encrypted text
##    for char in text:
##        new_text=new_text+rotate_character(char, rot)
##    return new_text ## encrypted text

@app.route("/", methods=['POST'])
def encrypt():
    # your main code (input and print statements)
    #def encrypt(text, rot):
    ##    text= input("Type a message: ")
    ##    rot= int(input("Rotate by: "))
    
    text=   request.form['text']           ##get text from the form
    rot=     request.form['rot']  ## get the rotation from the form
    new_text="" ##  Initialisation of the encrypted text
    for char in text:
        #new_text=new_text+rotate_character(char, rot)
        new_text=new_text+rotate_string(char, rot)
    #print(new_text)## encrypted text
    content=page_header+"<h1>"+new_text+"</h1>"+page-footer
    return content

#if __name__ == "__main__":
   # main()
app.run()
