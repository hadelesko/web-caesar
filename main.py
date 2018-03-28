from flask import Flask, request
app= Flask(__name__)
app.config['DEBUG']= True

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
        <label>
          Rotate by:  
            <input type="text" name="Rotate by"/>
            <textarea placeholder= "Type your original text "></textarea>
        </label>
        <input type="submit" value="Add It"/>
    </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    new_text="" ##  Initialisation of the encrypted text
    for char in text:
        new_text=new_text+rotate_character(char, rot)
    return new_text ## encrypted text

def main():
    # your main code (input and print statements)
    #def encrypt(text, rot):
    text= input("Type a message: ")
    rot= int(input("Rotate by: "))
    new_text="" ##  Initialisation of the encrypted text
    for char in text:
        new_text=new_text+rotate_character(char, rot)
    print(new_text)## encrypted text

#if __name__ == "__main__":
   # main()
app.run()
