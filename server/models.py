from flask_sqlalchemy import SQLAlchemy # type: ignore
from sqlalchemy import MetaData # type: ignore

# contains definitions of tables and associated schema constructs
metadata = MetaData()

# create the Flask SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)

# define a model class by inheriting from db.Model.


class Pet(db.Model):
    _tablename_ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)

    def _repr_(self):
        return f'<Pet {self.id}, {self.name}, {self.species}>'