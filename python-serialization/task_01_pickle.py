#!/usr/bin/env python3
"""
Module for serializing and deserializing
a custom Python object using pickle.
"""

import pickle


class CustomObject:
    """
    A custom class representing a person.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize the object attributes.

        Args:
            name (str): Person's name
            age (int): Person's age
            is_student (bool): Student status
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object attributes.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current object into a file.

        Args:
            filename (str): File where object is saved

        Returns:
            None if an error occurs
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (pickle.PickleError, OSError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file.

        Args:
            filename (str): File containing serialized object

        Returns:
            CustomObject: Loaded object
            None: If file does not exist or is malformed
        """
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError,
                pickle.PickleError,
                EOFError,
                OSError):
            return None
