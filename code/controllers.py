from model import *
from view import HeartDiseaseView


class HDController:
    """to connect the model and view"""
    def __init__(self, ):
        self.model = HDInformation()
        self.view = HeartDiseaseView(self.model)

    def run(self):
        self.view.run()
