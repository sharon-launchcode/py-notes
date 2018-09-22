from flask import Flask, request
#added request object which will allow us to access the data in request user
app = Flask(__name__)
#below does not work in Pythonanywhere
#app.config['DEBUG'] = True
#above does not work in Pythonanywhere

#set up global element in form
form = """
<!doctype html>
    <html>
        <form action="/hello" method="post">
            <label for="first-name">First Name</label>
            <input id="first-name" type="text" name="first_name" />
            <input type="submit" />
        </form>
    </html>

"""

@app.route('/')
def index():
    #return 'Hello from my tutor Flask!'
    #instead of returning a string return the value of whats in the global form variable
    return form
    #so now rendered by the application the http request is coming FROM the browser to the application
    #handled by index function
    #need to check on screen reader function
@app.route('/hello', methods=['POST'])
def hello():
    #For a GET method only first_name = request.args.get('first_name') note that it uses PARENS not BRACKETS
    first_name = request.form['first_name'] #for post method accessing a dictionary like method so brackets
    return '<h3>Hello  ' + first_name + '</h3>'
