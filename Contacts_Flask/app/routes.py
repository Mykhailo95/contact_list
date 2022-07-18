from flask import current_app as app
from flask import request
from .models import db, Email, Phone, Contact

@app.route('/users', methods=['POST'])
def creat_cont():
    username = request.json['username']
    email = request.json['email_id']
    phone = request.json['phone_id']
    age = request.json['age']

    contact = Contact.query.filter((Contact.username==username) | (Contact.email_id==email)).first()
    
    new_user = Contact(username=username, email=email, phone=phone, age=age)
    db.session.add(new_user)
    db.session.commit()
    
    return f'User {username} has been create'

@app.route('/user/<id>', methods=['GET'])
def get_contact():
    pass
