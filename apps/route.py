# Set up your imports here!
# import ...


from flask import Flask
app = Flask(__name__)

@app.route('/') # Fill this in!
def index():
    return '<h1>Hello Puppy!</h1>'

@app.route('/puppy/<name>') # Fill this in!
def puppylatin(name):
    if name.endswith('y'):
        lname =name[:-1]+'ful'
    else:
        lname=name+'y'
    return '<h1>This is a page for {}<h1>'.format(lname)
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!

    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"
 

if __name__ == '__main__':
    app.run(host="0.0.0.0")