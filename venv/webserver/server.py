from flask import Flask, render_template, request
from forms import inputForm
#Handles the running of the webserver
app = Flask(__name__)
app.config['SECRET_KEY'] = 'testKey'
#Default page if no other page is specified in the path
@app.route('/')
def home():
    return 'hello World'
#Input Page:Handles the input from the user. Uses the GET and POST method as it is getting the user's input and posting it to eh server
@app.route('/input',methods=['GET','POST'])
def i_forms():#Handles the form functionailty
    #Creates a new form object
    form = inputForm()
    #Checks if the form is submitted and displays the input from the user on the result page
    if form.is_submitted():
        result = request.form
        print(result)
        print(result.get('username'))
        username = result.get('username')#Retrieves the input from the form
        return render_template('userDisplay.html', username=username)#Renders the results page passing the input as a parameter
    return render_template('input.html',form=form)
    

if __name__ == '__main__':
    app.run()
