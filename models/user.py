from extensions import db

class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(200))
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())
    # Relationship to users (members)
    users = db.relationship('User', backref='team', cascade='all, delete-orphan')

    @property
    def data(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'users': [user.data for user in self.users]  # Include users in the team
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        teams = cls.query.all()
        return [team.data for team in teams]

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter(cls.id == id).first()

    # New method: Get all teams with their users
    @classmethod
    def get_all_with_users(cls):
        teams = cls.query.all()
        return [team.data for team in teams]
   
    



class User(db.Model):
     __tablename__='users'
     id = db.Column(db.Integer,primary_key=True)
     name=db.Column(db.String(80),nullable=False,unique=True)
     email=db.Column(db.String(200),nullable=False,unique=True)
     password=db.Column(db.String(200))
     created_at=db.Column(db.DateTime(),nullable=False,server_default=db.func.now())
     updated_at=db.Column(db.DateTime(),nullable=False,server_default=db.func.now(),onupdate=db.func.now())
     team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=True)

     @property
     def data(self):
          return {
               'id':self.id,
                'username':self.name,
                'email':self.email,
                'password':self.password,
                'team_id': self.team_id

          }
    
     def save(self):
          db.session.add(self)
          db.session.commit()



     @classmethod
     def get_all(cls):
          r=cls.query.all()
          result=[]

          for i in r:
               result.append(i.data)
          return result
     
     @classmethod
     def get_by_id(cls,id):
          print(f"Fetching user with ID: {id}")
          user= cls.query.filter(cls.id == id).first()
          print("User found:", user)  # See if it returns a valid user
          return user
     @classmethod

     def get_by_team(cls, team_id):
          return cls.query.filter_by(team_id=team_id).all()