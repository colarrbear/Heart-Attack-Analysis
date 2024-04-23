"""connects the model and view"""

from model import HeartDiseaseModel
from view import HeartDiseaseView


class HeartDiseaseController:
    def __init__(self):
        self.model = HeartDiseaseModel()
        self.view = HeartDiseaseView(self)

    def get_summary(self):
        return self.model.summary_statistics()

    def get_correlations(self):
        return self.model.correlations()

    def filter_data(self, filters):
        return self.model.filter_data(filters)

    def run(self):
        self.view.run()
