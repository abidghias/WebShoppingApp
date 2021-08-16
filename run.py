from market import app,db



class Apps(db.Model):
    App = db.Column(db.String(length=90),    unique=True,primary_key=True)
    Category = db.Column(db.String(length=50),    unique=True)
 
    Rating = db.Column(db.String(length=50),    unique=True)
    Reviews = db.Column(db.String(length=50),    unique=True)
    Size = db.Column(db.String(length=50),    unique=True)

    Installs = db.Column(db.String(length=50),    unique=True)
    Type = db.Column(db.String(length=50),   unique=True)
    Price = db.Column(db.String(length=50),   unique=True)
    Content_Rating =db.Column(db.String(length=50),   unique=True)

    Genres = db.Column(db.String(length=50),   unique=True)
    Last_uploaded = db.Column(db.String(length=50),  unique=True)
    Current_Ver = db.Column(db.String(length=50),   unique=True)
    Android_Ver = db.Column(db.String(length=50), unique=True)
    
    def __repr__(self):
        return '<App %r>' % self.App1

#Checks if the run.py file has executed directly and not imported
if __name__ == '__main__':
    app.run(debug=True)
