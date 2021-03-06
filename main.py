from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form = """ 
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
      <form action="/" method="post">
        <div>
            <label for="rot">Rotate by:</label>
            <input type="number" name="rot" value="0">
        </div>
        <textarea type="text" name="text" >{0}</textarea>
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

    # return   "<h1>" + encrypted_text + "</h1>"
    return   form.format(encrypted_text)

    
@app.route("/")
def index():
    return form.format("")

app.run()