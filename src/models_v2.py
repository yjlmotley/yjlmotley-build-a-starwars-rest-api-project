from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    favorites=db.relationship("Favorite", backref="user")

    def __repr__(self):
        return '<User %r>' % self.username
    
    def serialize(self):
        return {
            "id": self.id, 
            "username": self.username,
            "email": self.email,
            "favorites": [favorite.serialize() for favorite in self.favorites]
        }

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    hair_color = db.Column(db.String(50), nullable=True)
    height = db.Column(db.String(50), nullable=True)
    weight = db.Column(db.Integer, nullable=True)
    favorites=db.relationship("Favorite", backref="character")

    def serialize(self):
        return {
            "id": self.id, 
            "name": self.name,
            "hair_color": self.hair_color,
            "height": self.height,
            "weight": self.weight,
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    diameter = db.Column(db.String(50), nullable=True)
    terrain = db.Column(db.String(50), nullable=True)
    climate = db.Column(db.String(50), nullable=True)
    favorites=db.relationship("Favorite", backref="planet")

    def serialize(self):
        return {
            "id": self.id, 
            "name": self.name,
            "diameter": self.diameter,
            "terrain": self.terrain,
            "climate": self.climate,
        }
    
class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id", ondelete="CASCADE"), nullable=True)
    character_id = db.Column(db.Integer, db.ForeignKey("character.id", ondelete="CASCADE"), nullable=True)

    def serialize(self):
        return {
            "id": self.id, 
            "name": self.character.name if self.character else self.planet.name,
            "user_id": self.user_id,
            "character": self.character.serialize() if self.character else None,
            "planet": self.planet.serialize() if self.planet else None,
        
        }
