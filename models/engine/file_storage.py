#!/usr/bin/python3
"""
FileStorage class for serializing and deserializing objects to/from JSON file
"""
import json

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def clear(self):
        """Clears all objects and resets the JSON file"""
        self.__objects = {}
        with open(self.__file_path, "w") as f:
            json.dump({}, f)

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            from models.base_model import BaseModel
            from models.user import User
            from models.amenity import Amenity
            from models.city import City
            from models.place import Place
            from models.review import Review
            from models.state import State

            classes = {
                'BaseModel': BaseModel,
                'User': User,
                'Amenity': Amenity,
                'City': City,
                'Place': Place,
                'Review': Review,
                'State': State,
            }

            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
                self.__objects = {}  # Clear existing objects before reloading
                for key, value in obj_dict.items():
                    if value['__class__'] in classes:
                        self.__objects[key] = classes[value['__class__']](**value)
        except FileNotFoundError:
            pass
