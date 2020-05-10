# -*- coding: utf-8 -*-

"""
    healthoslib.health_os_client

    This file was automatically generated by APIMATIC BETA v2.0 on 02/18/2017
"""
from .decorators import lazy_property
from .controllers.medicines_controller import MedicinesController
from .controllers.lab_tests_controller import LabTestsController
from .controllers.generics_controller import GenericsController
from .controllers.food_controller import FoodController
from .controllers.exercises_controller import ExercisesController
from .controllers.drug_interactions_controller import DrugInteractionsController
from .controllers.diseases_controller import DiseasesController
from .controllers.chat_controller import ChatController
from .controllers.autocomplete_controller import AutocompleteController
from .controllers.authentication_controller import AuthenticationController
from .configuration import Configuration

class HealthOSClient(object):

    @lazy_property
    def medicines(self):
        return MedicinesController()

    @lazy_property
    def lab_tests(self):
        return LabTestsController()

    @lazy_property
    def generics(self):
        return GenericsController()

    @lazy_property
    def food(self):
        return FoodController()

    @lazy_property
    def exercises(self):
        return ExercisesController()

    @lazy_property
    def drug_interactions(self):
        return DrugInteractionsController()

    @lazy_property
    def diseases(self):
        return DiseasesController()

    @lazy_property
    def chat(self):
        return ChatController()

    @lazy_property
    def autocomplete(self):
        return AutocompleteController()

    @lazy_property
    def authentication(self):
        return AuthenticationController()


    def __init__(self, 
                 host = None,
                 o_auth_access_token = None):
        # type: (object, object) -> object
        if host != None:
            Configuration.host = host
        if o_auth_access_token != None:
            Configuration.o_auth_access_token = o_auth_access_token

