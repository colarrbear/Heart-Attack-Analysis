from model import *
from view import HeartDiseaseView


class HDController:
    """to connect the model and view"""
    def __init__(self):
        self.load_data = DataLoader()
        self.model = PlotGraphs(self.load_data)
        self.view = HeartDiseaseView(self.model)
        # if user response is from tab "Data Information Tab" then model will be HDInformation
        # if user response is from tab "Statistics Tab" then model will be Statistics
        # self.current_tab = None

    # def switch_model_based_on_tab(self, tab):
    #     """Switch the model based on the selected tab."""
    #     if tab == "Data Information":
    #         self.model = HDInformation()
    #     elif tab == "Statistics":
    #         self.model = Statistics()

    def run(self):
        self.view.run()
