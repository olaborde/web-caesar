from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form = """ 
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
      <form action="/" method="post">
        <div>
            <label for="rot">Rotate by:</label>
            <input type="text" name="rot" value="0">
        </div>
        <textarea type="text" name="text" placeholder="{0}  "></textarea>
        <br>
        <input type="submit" value="submit">
    </form>
    </body>
</html>

"""
@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']  
    the_rot = int(rot)   
    
    text = request.form['text']

    encrypted_text = rotate_string (text, the_rot)

    return   "<li>" + encrypted_text + "</li>"

    
@app.route("/")
def index():
    return form

app.run()