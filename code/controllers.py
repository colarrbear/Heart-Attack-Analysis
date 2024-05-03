# """connects the model and view"""
#
# from model import HeartDiseaseModel
# from view import HeartDiseaseView
#
#
# class HeartDiseaseController:
#     def __init__(self):
#         self.model = HeartDiseaseModel()
#         self.view = HeartDiseaseView(self)
#
#     def __init__(self):
#         self.model = HeartDiseaseModel()
#         self.view = HeartDiseaseView(self)
#
#     def get_summary_statistics(self):
#         return self.model.summary_statistics()
#
#     def get_correlations(self):
#         return self.model.calculate_correlations()
#
#     def run(self):
#         self.view.run()
#
#     # def get_summary(self):
#     #     return self.model.summary_statistics()
#     #
#     # def get_correlations(self):
#     #     return self.model.correlations()
#     #
#     # def filter_data(self, filters):
#     #     return self.model.filter_data(filters)

from model import HeartDiseaseModel
# from view_ttkthemes import HeartDiseaseView
from view import HeartDiseaseView


class HeartDiseaseController:
    """to connect the model and view"""
    def __init__(self):
        self.model = HeartDiseaseModel()
        self.view = HeartDiseaseView(self)

    def run(self):
        self.view.run()

    # Additional functions can be added here to handle user interactions
    # For example:
    # def show_summary_statistics(self):
    #     summary = self.model.summary_statistics()
    #     self.view.display_summary_statistics(summary)

    # def show_correlations(self):
    #     correlations = self.model.correlations()
    #     self.view.display_correlations(correlations)

    # def apply_filter(self, filters):
    #     filtered_data = self.model.filter_data(filters)
    #     self.view.display_filtered_data(filtered_data)

