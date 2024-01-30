from musicapp import database
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declared_attr


class BaseModel:
   # __abstract__ = True
    id = database.Column(database.Integer, primary_key=True)
    created_at = database.Column(database.DateTime(timezone=True), default=func.now())
    updated_at = database.Column(database.DateTime(timezone=True), default=func.now(), nullable=False)


    def __str__(self):
        return f'{self.__dict__}'

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        time = "%Y-%m-%dT%H:%M:%S.%f"
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
