from flask import Flask
from flask import Flask, redirect, url_for, render_template, request, flash
app = Flask(__name__)

@app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
def hello_world1():
    error = 'Invalid username/password'
    return render_template('arunrajaryan.html', error=error)
    # return render_template('portfolio.html', error=error)


@app.route("/mypage")
# def hello_world():
#     return "<p>Hello, World!</p>"
def hello_world():
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
    user_contact = {'email':'ak080495@gmail.com1','phone1':'+919934110211','phone2':'+919663720230','address':'House no. 3072/1B, Block 7, Ranjeet Nagar, New Delhi, Delhi 110008.','whatsapp':'9934110211','github':'arun12341234','linkdin':'arun-kumar-1bb0b4b5','gmail':'ak080495@gmail.com',}

    return render_template('portfolio.html', error=error,user_contact=user_contact, data= project_data,user_data=user_data)

if __name__ == '__main__':
    # app.debug = True
    app.run()