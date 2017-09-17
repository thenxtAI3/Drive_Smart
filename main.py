from flask import Flask, render_template, request, redirect, url_for # imports libraries for flask web development
import os # library for system functions
import smtplib # library for email rendering

app = Flask(__name__) # initializes app

class User_info(): # globally saved variables
    email = ""
    website = []
    note = []
    address = []
    contact = []
    final = []
    message = ""

x = User_info() # sets the info class to the variable x

#Homepage#######################################
@app.route('/') # homepage route
def home():
    return render_template("home.html") # renders homepage
@app.route('/', methods=['POST'])
def home_process(): # function that processes POST method
    x.email = request.form['user_email'] # grabs inputted user email and saves it to class variable "email"
    return redirect(url_for('feature', user_email=x.email)) # passes email into following "feature" template

#Feature########################################
@app.route('/feature') # feature route
def feature(): # renders feature
    values = {'user_email': x.email} # creates a dictionary of variables
    return render_template("feature.html", values=values) # renders feature template with values passed

#Driving########################################
@app.route('/driving') # driving route
def driving(): # renders interface HTML
    return render_template("interface.html")

@app.route('/driving', methods=["POST"])
def saving(): # process POST method
    if 'website' in request.form: # if the request.form has name variable 'website'
        website = request.form['website'] # request website
        x.website.append(website) # append to website list
    elif 'note' in request.form: # similar format following
        note = request.form['note']
        x.note.append(note)
    elif 'address' in request.form:
        address = request.form['address']
        x.address.append(address)
    elif 'contact' in request.form:
        contact = request.form['contact']
        x.contact.append(contact)
    return render_template("interface.html")

#Thank You######################################
@app.route('/thank_you') # thank you route
def thank_you(): # sets up thank you page
    website = "\n".join(x.website)
    note = "\n".join(x.note)
    address = "\n".join(x.address)
    contact = "\n".join(x.contact)
    saved = "****WEBSITE**** \n" + website + "\n" + "****NOTES**** \n" + note + "\n" +  "****ADDRESS**** \n" + address  + "\n" + "****CONTACT**** \n" + contact
    endmessage = "\nThank you for using Drive Smart!"
    final_message = saved + endmessage
    # email portion
    server = smtplib.SMTP('smtp.gmail.com', 587) # sets enail server
    server.starttls() # starts server access
    server.login("youremail", "yourpassword") # inputs team created email
    msg = final_message # sets string message to a variable
    server.sendmail("youremail", x.email, msg) # sends to specified user email
    server.quit() # ends server access
    return render_template("thank_you.html", user_email=x.email) # renders thank you template

#Checking if run from user######################
if __name__ == '__main__':
    app.run(
        port=int(os.getenv('PORT', 8080)),
        host=os.getenv("IP", "0.0.0.0"),
        debug=True
        )
