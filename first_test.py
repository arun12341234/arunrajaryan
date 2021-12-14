from flask import Flask
from flask import Flask, redirect, url_for, render_template, request, flash
app = Flask(__name__)


# //required
app.secret_key = "any-string-you-want-just-keep-it-secret"
from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField,FileField
from wtforms.validators import DataRequired, Email
import email_validator

#for bootstarp
from flask_bootstrap import Bootstrap
Bootstrap(app)


#for dtabase 
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/portfolio'
db = SQLAlchemy(app)
#simple html page 
@app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
def hello_world1():
    error = 'Invalid username/password'
    return render_template('arunrajaryan.html', error=error)
    # return render_template('portfolio.html', error=error)












#simple html page with static data

@app.route("/mypage")
# def hello_world():
#     return "<p>Hello, World!</p>"
def hello_world2():
    error = 'Invalid username/password'
    user_data={'first_name':'Arun','middle_name':'','last_name':'','Langulages':'Python, Django, Flask, Angular 8+','exp_year':'2+','designation':'Software Engineer','exp_in':'Software Applications Development','image':'',}
    project_data = [
        {'project_name':'Breathalyzer Alcohol Content Check',
        'project_desc':'An application feature Which is Integrated with an IoT Device and passing the values to the application. The BAC status will be displayed in message board in the application.Generate Report: A reporting tool which is integrated in the application to generate the reports according to the data.',
        'project_tech':'Python, Django, Pandas, Angular 8+',
        'project_url':'http://49.206.19.247:8779/',
        
        'url_type':'Website'},
        {'project_name':'Breathalyzer Alcohol Content Check','project_desc':'An application feature Which is Integrated with an IoT Device and passing the values to the application. The BAC status will be displayed in message board in the application.Generate Report: A reporting tool which is integrated in the application to generate the reports according to the data.','project_tech':'Python, Django, Pandas, Angular 8+','project_url':'http://49.206.19.247:8779/','url_type':'Website'},
        {'project_name':'Breathalyzer Alcohol Content Check','project_desc':'An application feature Which is Integrated with an IoT Device and passing the values to the application. The BAC status will be displayed in message board in the application.Generate Report: A reporting tool which is integrated in the application to generate the reports according to the data.','project_tech':'Python, Django, Pandas, Angular 8+','project_url':'http://49.206.19.247:8779/','url_type':'Website'},
        {'project_name':'Breathalyzer Alcohol Content Check','project_desc':'An application feature Which is Integrated with an IoT Device and passing the values to the application. The BAC status will be displayed in message board in the application.Generate Report: A reporting tool which is integrated in the application to generate the reports according to the data.','project_tech':'Python, Django, Pandas, Angular 8+','project_url':'http://49.206.19.247:8779/','url_type':'Website'},
    
        ]
    user_contact = {'email':'ak080495@gmail.com1',
    'phone1':'+919934110211',
    'phone2':'+919663720230',
    'address':'House no. 3072/1B, Block 7, Ranjeet Nagar, New Delhi, Delhi 110008.',
    'whatsapp':'9934110211',
    'github':'arun12341234',
    'linkdin':'arun-kumar-1bb0b4b5',
    'gmail':'ak080495@gmail.com',}

    return render_template('portfolio.html', error=error,user_contact=user_contact, data= project_data,user_data=user_data)


  
class contactForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[
      DataRequired(), Email(granular_message=True)])
    message= StringField(label='Message')
    submit = SubmitField(label="Log In")


    @app.route("/post_data", methods=['GET', 'POST'])
    def post_data():
        cform = contactForm()

        if cform.validate_on_submit():
            print(cform.name.data)
            print(f"Name:{cform.name.data}, E-mail:{cform.email.data}, message:{cform.message.data}")
        else:
            print("Invalid Credentials")
                    
        return render_template("contact.html", form=cform)



# pip install Flask-Bootstrap

class user_data_Form(FlaskForm):

    first_name = StringField(label='First Name', validators=[DataRequired()])
    middle_name = StringField(label='Middle Name', validators=[DataRequired()])
    last_name = StringField(label='Last Name', validators=[DataRequired()])

    Langulages = StringField(label='Langulages', validators=[DataRequired()])
    exp_year = StringField(label='Years Experiance', validators=[DataRequired()])
    designation = StringField(label='Designation', validators=[DataRequired()])
    exp_in = StringField(label='Experience In', validators=[DataRequired()])
    image = FileField(label='Upload your Image', validators=[DataRequired()])
    submit = SubmitField(label="Submit")


class user_contact_Form(FlaskForm):

    email = StringField(label='Email id', validators=[DataRequired(), Email(granular_message=True)])
    phone1 = StringField(label='Mobile no.', validators=[DataRequired()])
    phone2 = StringField(label='Alternate mobile no.', validators=[DataRequired()])

    address = StringField(label='Address', validators=[DataRequired()])
    whatsapp = StringField(label='Whatsapp No.', validators=[DataRequired()])
    github = StringField(label='Github Link', validators=[DataRequired()])
    linkdin = StringField(label='Linkdin Link', validators=[DataRequired()])
    gmail = StringField(label='Gmail Id', validators=[DataRequired()])
    submit = SubmitField(label="Submit")



class project_data_Form(FlaskForm):

    project_name = StringField(label='What is your project name?', validators=[DataRequired()])
    project_desc = StringField(label='Write description of your project?', validators=[DataRequired()])
    project_tech = StringField(label='Technologies used in your project?', validators=[DataRequired()])

    project_url = StringField(label='What is your project url?', validators=[DataRequired()])
    url_type = StringField(label='Which kind of project url?', validators=[DataRequired()])
    submit = SubmitField(label="Submit")



@app.route("/user_data", methods=['GET', 'POST'])
def user_data():
    # user_data={'first_name':'Arun','middle_name':'','last_name':'','Langulages':'Python, Django, Flask, Angular 8+','exp_year':'2+','designation':'Software Engineer','exp_in':'Software Applications Development','image':'',}
    cform = user_data_Form()


    return render_template("user_data.html", form=cform)

    
    




@app.route("/project_data", methods=['GET', 'POST'])
def project_data():
    cform = project_data_Form()


    return render_template("project_data.html", form=cform)





@app.route("/user_contact", methods=['GET', 'POST'])
def user_contact():
    cform = user_contact_Form()


    return render_template("user_contact.html", form=cform)





if __name__ == '__main__':
    # app.debug = True
    app.run()