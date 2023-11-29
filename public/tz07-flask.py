## file is called tz07-flask.py

from flask inport Flask, request, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
return redirect(url_for('myFlask'))

@app.route('/myFlask', methods = ['POST', 'GET'])
def myFlask():
    # Print the full URL to the command line
    print(f"Use this URL: {request.url}")
    try:
      if request.method == 'GET':
        result = subprocess.run(['python3', 'tz07-web.py', "Enter Data"], capture_output=true, text=True)
        
    return result.stdout
except Exception as e:
    return f'<h1 style="color:red;">Error: {str(e)}</h1>'
if_name_ == '_main_':
  app.run(debug=True)

# -------------------------------------------------------------------------------------------------------

## this file is called tz07-web.py
import sys

myHTML = '''
<form method="POST">
  Enter your input: <input type="text" name="user_input">
  <input type="submit" value="Submit">
</form>
'''

def myRunPy(input_value):
    # Process the input and return the result
    # return f"Processed: {input_ value}"
    return myHTML + input_value

if _name_ == "_main_":
  input_value = sys.argv[1]  # Get input from command line argument
  result = myRunPy(input_value)
  print(result)
