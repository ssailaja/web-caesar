from flask import Flask, request
from caesar import rotate_string
app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

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
    <form action="/encrypt" method="post">

        <label for="Rotateby">Rotate by:</label>
        
            <input type="text" id="Rotateby" name="rot" value="0"/>
            <textarea name="text">{0}</textarea>      
        
        <input type="submit" value="Submit Query"/ >
    </form>

    </body>
</html>
"""

@app.route("/encrypt", methods=['POST'])
def encrypt():
    rot_value = int(request.form['rot'])
    text_value = request.form['text']
    encrypted_text_value = rotate_string(text_value, rot_value)

    return form.format(encrypted_text_value)

   
""".format(encrypted_text) """

@app.route("/")
def index():
    return form.format('')

app.run()