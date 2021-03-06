# -*- coding: utf-8 -*-

"""
    healthoslib.models.exercises_response
 
    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ) on 02/18/2017
"""
import healthoslib.models.base_model

class ExercisesResponse(healthoslib.models.base_model.BaseModel):

    """Implementation of the 'ExercisesResponse' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        category (string): TODO: type description here.
        calory_count (string): TODO: type description here.
        cardio_subcategory (string): TODO: type description here.
        primary_muscle_group (string): TODO: type description here.
        exercise_id (string): TODO: type description here.
        search_score (float): TODO: type description here.

    """

    def __init__(self, 
                 name = None,
                 category = None,
                 calory_count = None,
                 cardio_subcategory = None,
                 primary_muscle_group = None,
                 exercise_id = None,
                 search_score = None):
        """Constructor for the ExercisesResponse class"""
        
        # Initialize members of the class
        self.name = name
        self.category = category
        self.calory_count = calory_count
        self.cardio_subcategory = cardio_subcategory
        self.primary_muscle_group = primary_muscle_group
        self.exercise_id = exercise_id
        self.search_score = search_score

        # Create a mapping from Model property names to API property names
        self.names = {
            "name" : "name",
            "category" : "category",
            "calory_count" : "calory_count",
            "cardio_subcategory" : "cardio_subcategory",
            "primary_muscle_group" : "primary_muscle_group",
            "exercise_id" : "exercise_id",
            "search_score" : "search_score",
        }


    @classmethod
    def from_dictionary(cls, 
                        dictionary):
        """Creates an instance of this model from a dictionary
       
        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.
            
        Returns:
            object: An instance of this structure class.
            
        """
        if dictionary == None:
            return None
        else:
            # Extract variables from the dictionary
            name = dictionary.get("name")
            category = dictionary.get("category")
            calory_count = dictionary.get("calory_count")
            cardio_subcategory = dictionary.get("cardio_subcategory")
            primary_muscle_group = dictionary.get("primary_muscle_group")
            exercise_id = dictionary.get("exercise_id")
            search_score = dictionary.get("search_score")
            # Return an object of this model
            return cls(name,
                       category,
                       calory_count,
                       cardio_subcategory,
                       primary_muscle_group,
                       exercise_id,
                       search_score)


