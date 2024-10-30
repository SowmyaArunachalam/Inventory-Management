from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///posts.db'
db=SQLAlchemy(app)

class Product(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(20),nullable=False)
    description=db.Column(db.Text,nullable=False)
    category=db.Column(db.String(20),nullable=False)
    quantity=cost_price=db.Column(db.Integer, nullable=False)
    cost_price=db.Column(db.Integer, nullable=False)
    selling_price=db.Column(db.Integer, nullable=False)
    supplier=cost_price=db.Column(db.String(20), nullable=False)
    
    def __repr__(self):
        return 'Blogpost'+ str(self.id)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/posts')
def posts():
    return render_template("posts.html")

if __name__ == "__main__":
    app.run(debug=True)
