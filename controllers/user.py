from flask import request
from models.user import User,Team
from extensions import db

def add_user_function():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        team_id=request.form['team_id']
        user=User(
            name=name,
            email=email,
            password=password,
            team_id=team_id
        )

        user.save()
        data= {
            'id':user.id,
            'name':user.name,
            'email':user.email,
            'password':user.password,
            'team_id':user.team_id
            }
        
        return data

def edit_user_fuction(data):
     
    if data is None:
        return "Error: User does not exist!", 404

    if request.method=='POST':
        data.name=request.form['name']
        data.email=request.form['email']
        data.password=request.form['password']

        db.session.commit()
    return data
def delete_user_function(user):
    db.session.delete(user)
    db.session.commit()

def add_team_function():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        description = request.form.get('description', '')
          # Optional field

        # Create a new team
        new_team = Team(name=name,
                        description=description
                        )
        new_team.save()

        datar={'id':new_team.id,
               'name':new_team.name,
               'description':new_team.description,
               }
        return datar
        # Redirect to the home page or team list page


def delete_team_function(team):
    db.session.delete(team)
    db.session.commit()