from flask import Blueprint,render_template,redirect,url_for
from controllers.user import add_user_function,edit_user_fuction,delete_user_function,add_team_function,delete_team_function
import sys
from models.user import User,Team


main=Blueprint('main',__name__)

@main.route('/',methods=['GET'])

def home():
    data= User.get_all()
    return render_template('index.html',data=data)

@main.route('/adduser',methods=['GET','POST'])

def add_user():
    data=add_user_function()
    
    return render_template('adduser.html',data=data)

@main.route('/edituser/<int:id>',methods=['GET','POST'])
def edit_user(id):
    user=User.get_by_id(id)
    print("user object",user)
    if user is None:
        return "error not found",404
    data=edit_user_fuction(user)
    return render_template('edituser.html',user=user,data=data)

@main.route('/deleteuser/<int:id>',methods=['POST'])
def delete_user(id):
    user=User.get_by_id(id)
    print(user,file=sys.stderr)
    delete_user_function(user)
    return redirect(url_for('main.home'))

@main.route('/teams', methods=['GET'])
def list_teams():
    teams = Team.get_all_with_users()
    return render_template('teams.html', teams=teams)

@main.route('/team/<int:team_id>/users', methods=['GET'])
def list_team_users(team_id):
    users = User.get_by_team(team_id)
    return render_template('team_users.html', users=users)

@main.route('/addteam', methods=['GET', 'POST'])
def add_team():
    datar=add_team_function()
    # If it's a GET request, render the form
    return render_template('addteam.html',data=datar)
@main.route('/deleteteam/<int:id>', methods=['POST'])
def delete_team(id):
    team = Team.get_by_id(id)  # Fetch the team by ID
    if team is None:
        return "Team not found", 404  # Return an error if the team doesn't exist
    delete_team_function(team)
    return redirect(url_for('main.home'))
   
   

