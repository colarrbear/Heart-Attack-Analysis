"""handles the User interface of the application"""
import tkinter as tk
import PIL
from tkinter import ttk
from model import *
from PIL import Image, ImageTk


class HeartDiseaseView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.data_loader = controller.data
        self.plotter = PlotGraphs(self.data_loader)
        self.title("GoodHeart")
        self.init_components()
        self.create_quit_button()
        self.configure_window()

    def configure_window(self):
        """Configure the window settings."""
        self.geometry("1080x725")
        self.resizable(True, True)

    def init_components(self):
        # Feature Tabs
        self.feature_tabs = ttk.Notebook(self)
        self.feature_tabs.configure(padding=10)
        self.feature_tabs.pack(fill="both", expand=True)
        self.tabs()

    def tabs(self):
        """Create tabs for the application."""
        # Home Tab
        self.home_tab = ttk.Frame(self.feature_tabs)
        self.feature_tabs.add(self.home_tab, text="Home")
        self.init_home_tab()

        # Data Information Tab
        self.data_information_tab = ttk.Frame(self.feature_tabs)
        self.feature_tabs.add(self.data_information_tab,
                              text="Data Information")
        self.init_data_information_tab()

        # Statistics Tab
        self.statistics_tab = ttk.Frame(self.feature_tabs)
        self.feature_tabs.add(self.statistics_tab, text="Statistics")
        self.init_statistics_tab()

        # Graph Tab
        self.adv_graph_tab = ttk.Frame(self.feature_tabs)
        self.feature_tabs.add(self.adv_graph_tab, text="Graph")
        self.init_advance_graph_tab()

        # Data Storytelling Tab
        self.data_storytelling_tab = ttk.Frame(self.feature_tabs)
        self.feature_tabs.add(self.data_storytelling_tab, text="Knowledge")
        self.init_data_storytelling_tab()

    def init_data_storytelling_tab(self):
        """Initialize the Data Storytelling (knowledge) tab."""
        # text to explain this page is showing trend of happening heart attack
        # based on the data.
        data_storytelling_text = (
            "This page depicts the trend of heart attack occurrences based on age and sex. \n"
            "Analysis reveals that, on average, males tend to experience fewer heart attacks \n"
            "compared to females across various age groups.")
        data_storytelling_label = ttk.Label(self.data_storytelling_tab,
                                            text=data_storytelling_text,
                                            foreground="#5A60A5")
        data_storytelling_label.pack(side="top", fill="x", padx=10, pady=10)

        # Create another frame for the graph canvas
        self.data_storytelling_canvas_frame = tk.Frame(
            self.data_storytelling_tab, width=1020,
            height=400)
        self.data_storytelling_canvas_frame.pack(side="bottom", fill="both",
                                                 expand=True)

        self.plotter.plot_line_data_storytelling(
            self.data_storytelling_canvas_frame)

    def init_home_tab(self):
        """Initialize the Home tab."""
        self.home_bg()
        self.home_combobox_description()

    def home_bg(self):
        """Set the background image for the Home tab."""
        # Load the image
        bg_image = Image.open("bgs/home_bg.png")
        bg_image_tk = ImageTk.PhotoImage(bg_image)

        # Create a Canvas to display the image
        self.canvas = tk.Canvas(self.home_tab, width=bg_image.width - 50,
                                height=bg_image.height)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.pack()

        self.canvas.bind("<Configure>", self.home_on_canvas_resize)

        # Display the image on the Canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=bg_image_tk)
        self.canvas.image = bg_image_tk  # Keep a reference to the image

    def home_on_canvas_resize(self, event):
        """Adjust the size and position of the components (of home tab) when the canvas is resized."""
        # Get the new size of the canvas
        canvas_width = event.width
        canvas_height = event.height

        # Update the size and position of the Combobox
        self.__home_attribute_combobox.place(x=canvas_width / 2 - 100,
                                             y=canvas_height / 1.375)
        self.__home_attribute_combobox.config(width=canvas_width // 50)

    def home_combobox_description(self):
        """Place a combobox inside the background image."""
        # Create a combobox to select attributes
        self.__home_attribute_combobox = ttk.Combobox(self.home_tab,
                                                      values=self.data_loader.get_column_names)
        self.__home_attribute_combobox.place(x=425, y=450)
        self.__home_attribute_combobox.set(
            self.data_loader.get_column_names[0])
        self.__home_attribute_combobox.bind("<<ComboboxSelected>>",
                                            self.home_display_attribute_description)

    def home_display_attribute_description(self, event):
        # print(selected_attribute)
        """Display the description of the selected attribute."""
        attribute_descriptions = {
            "age": "Age of the patient (in years)",
            "sex": "Sex of the patient "
                   "\n1 = male\n"
                   "0 = female",
            "cp": "Chest pain type\n"
                  "Value 1: typical angina\n"
                  "Value 2: atypical angina\n"
                  "Value 3: non-anginal pain\n"
                  "Value 4: asymptomatic",
            "trtbps": "Resting blood pressure (in mm Hg on admission to the hospital)",
            "chol": "Serum cholesterol in mg/dl",
            "fbs": "Fasting blood sugar (> 120 mg/dl)\n"
                   "1 = true"
                   "\n0 = false",
            "restecg": "Resting electrocardiographic results\n"
                       "Value 0: normal\n"
                       "Value 1: having ST-T wave abnormality (T wave inversion"
                       "s and/or ST elevation or depression of > 0.05 mV)\n"
                       "Value 2: showing probable or definite left ventricu"
                       "lar hypertrophy by Estes' criteria",
            "thalachh": "Maximum heart rate achieved",
            "exng": "Exercise induced angina\n"
                    "1 = yes"
                    "\n0 = no",
            "oldpeak": "ST depression induced by exercise relative to rest",
            "slope": "The slope of the peak exercise ST segment\n"
                     "Value 1: upsloping\n"
                     "Value 2: flat\n"
                     "Value 3: downsloping",
            "caa": "Number of major vessels (0-3) colored by fluoroscopy",
            "thall": "Thal rate",
            "output": "Target variable\n"
                      "0 = Less chance"
                      "\n1 = More chance of heart attack"}

        # Update the description label with the description of
        # the selected attribute
        selected_attribute = self.__home_attribute_combobox.get()
        description = attribute_descriptions[selected_attribute]

        # Check if a description window already exists, then destroy it
        for widget in self.winfo_children():
            if (isinstance(widget,
                           tk.Toplevel) and widget.title() ==
                    "GoodHeart Description"):
                widget.destroy()

        # Create a Toplevel window for the description
        description_window = tk.Toplevel(self)
        description_window.title("GoodHeart Description")

        # Set the geometry of the description window
        description_window_width = 400
        description_window_height = 200
        x_coordinate = self.winfo_x() + 100
        y_coordinate = self.winfo_y() + 100

        description_window.geometry(
            f"{description_window_width}x{description_window_height}"
            f"+{x_coordinate}+{y_coordinate}")

        # Label with the description text for the selected attribute
        description_label = tk.Label(description_window, text=description,
                                     wraplength=280)
        description_label.config(font=("TkDefaultFont", 12))
        description_label.config(foreground="#F27A79")
        description_label.pack(pady=20)

        # Button to close the popup window
        close_button = tk.Button(description_window, text="Quit",
                                 command=description_window.destroy)
        close_button.pack(pady=10, side="bottom")

    def init_data_information_tab(self):
        """Initialize the Data Information tab."""
        self.data_info_bg()

        # Add a label for the combobox in Data Information tab
        self.__attributes_label = ttk.Label(self.data_information_tab,
                                            text="Select Attribute:")
        self.__attributes_label.config(font=("TkDefaultFont", 13))
        self.__attributes_label.config(foreground="#F27A79")
        self.__attributes_label.place(x=500, y=260)

        column = self.data_loader.get_column_names

        # Add a combobox to select attributes in Data Information tab
        self.__attribute_combobox = ttk.Combobox(self.data_information_tab,
                                                 values=column)
        self.__attribute_combobox.place(x=450, y=290)
        self.__attribute_combobox.set(column[0])  # Set default value
        self.__attribute_combobox.bind("<<ComboboxSelected>>", lambda
            event: self.data_info_handle_attribute_selection(
            self.__attribute_combobox.get()))

        self.canvas.bind("<Configure>", self.data_info_on_canvas_resize)

    def data_info_on_canvas_resize(self, event):
        """Adjust the size and position of the components
        (in data infomation tab)
        when the canvas is resized."""

        # Get the new size of the canvas
        canvas_width = event.width
        canvas_height = event.height

        # Update the size and position of the Combobox
        self.__attribute_combobox.place(x=canvas_width / 2 - 70,
                                        y=canvas_height / 2)
        self.__attribute_combobox.config(width=canvas_width // 50)

        # Update the size and position of the Label
        self.__attributes_label.place(x=canvas_width / 2 - 20,
                                      y=canvas_height / 2 - 30)

        # Update the size and position of the Output Frame
        self.output_frame.place(x=canvas_width / 2 - 80,
                                y=canvas_height / 2 + 30)

    def data_info_bg(self):
        """Set the background image for the Home tab."""
        # Load the image
        data_info_bg_image = Image.open("bgs/datainfo_bg.png")
        data_info_bg_image_tk = ImageTk.PhotoImage(data_info_bg_image)

        # Set canvas dimensions to match image dimensions
        canvas_width = data_info_bg_image.width
        canvas_height = data_info_bg_image.height

        # Create a Canvas to display the image
        self.canvas = tk.Canvas(self.data_information_tab, width=canvas_width,
                                height=canvas_height)
        self.canvas.pack(fill="both", expand=True)

        # Display the image on the Canvas
        self.canvas.create_image(0, 0, anchor=tk.NW,
                                 image=data_info_bg_image_tk)
        self.canvas.image = data_info_bg_image_tk
        # Keep a reference to the image

        # Add a frame within the canvas for output
        self.output_frame = tk.Frame(self.canvas)
        self.canvas.create_window(0, 0, window=self.output_frame)
        self.output_frame.pack(side="left", padx=20, pady=20, fill="both",
                               expand=True)

    def data_info_handle_attribute_selection(self, selected_attribute):
        """
        Handle the selection of an attribute in
        the combobox of the Data Information tab.
        """
        data_info = self.controller.summary_statistics()[selected_attribute]
        self.data_info_update_data_information_tab(data_info)

    def data_info_update_data_information_tab(self, selected_atb):
        """Update the Data Information tab with the given data information."""
        data_info = selected_atb

        # Clear existing labels in the output frame
        for child in self.output_frame.winfo_children():
            child.destroy()

        # Create labels for data information and place them in the output frame
        for i, (stat, value) in enumerate(data_info.items()):
            # Create a label with the background color matching
            # the frame's background color
            label = ttk.Label(self.output_frame, text=f"{stat}:   {value:.4g}")
            color = "#F27A79"
            label.config(font=("TkDefaultFont", 13), foreground=color)
            label.pack(side="top", fill="x", padx=5, pady=2, expand=True,
                       anchor="ne")

    def init_statistics_tab(self):
        """Initialize the Statistics tab."""
        # Create a frame for visual separation
        separator_frame = tk.Frame(self.statistics_tab, height=10)
        separator_frame.pack(side="bottom", pady=10)

        # Create another frame for the graph canvas
        self.stat_graph_canvas_frame = tk.Frame(self.statistics_tab, width=800,
                                                height=400)
        self.stat_graph_canvas_frame.pack(side="bottom", fill="both", expand=True)

        # Create the menu box
        menu_label = ttk.Label(self.statistics_tab,
                               text="Select Visualization:")
        menu_label.pack(side="top", fill="x", padx=5, pady=5)

        menu_var = tk.StringVar()
        menu_var.set("Select Visualization")
        # menu_combobox = ttk.Combobox(self.statistics_tab,
        #                              textvariable=menu_var,
        #                              values=["Bar Charts", "Histogram",
        #                                      "Correlations",
        #                                      "Stack Bar graph"])
        menu_combobox = ttk.Combobox(self.statistics_tab,
                                     textvariable=menu_var,
                                     values=["Bar Charts", "Histogram",
                                             "Correlations",])
        menu_combobox.pack(side="top", fill="x", padx=5, pady=5)
        menu_combobox.bind("<<ComboboxSelected>>",
                           self.stat_handle_menu_selection)

        # Create the label for the first attribute combobox
        left_label = ttk.Label(self.statistics_tab,
                               text="Select 1st attribute:")
        left_label.pack(side="left", fill="x", padx=5, pady=5, expand=True)

        # Create the attribute comboboxes
        self.left_attribute_combobox = ttk.Combobox(self.statistics_tab,
                                                    state="disabled")
        self.left_attribute_combobox.pack(side="left", fill="x", padx=5,
                                          pady=5, expand=True)

        # Create the label for the second attribute combobox
        right_label = ttk.Label(self.statistics_tab,
                                text="Select 2nd attribute:")
        right_label.pack(side="left", fill="x", padx=5, pady=5, expand=True)

        self.right_attribute_combobox = ttk.Combobox(self.statistics_tab,
                                                     state="disabled")
        self.right_attribute_combobox.pack(side="left", fill="x", padx=5,
                                           pady=5, expand=True)

        # Create the button to create the graph
        create_graph_button = ttk.Button(self.statistics_tab,
                                         text="Plot Graph",
                                         command=self.stat_create_graph)
        create_graph_button.pack(side="right", padx=5, pady=5)

    def stat_create_graph(self):
        """Create a graph based on the self.__selected visualization."""
        self.__selected = self.selected_visualization
        left = self.left_attribute_combobox.get()
        right = None

        # If the selected visualization is "Bar Charts",
        # fetch the right attribute
        if (self.__selected == "Bar Charts" or
                self.__selected == "Stack Bar graph"):
            right = self.right_attribute_combobox.get()

        # Clear the existing graph canvas
        for widget in self.stat_graph_canvas_frame.winfo_children():
            widget.destroy()

        # Plot the graph based on the selected visualization
        if self.__selected == "Bar Charts":
            self.plotter.plot_bar_chart(left, right, self.stat_graph_canvas_frame)
        elif self.__selected == "Histogram":
            self.plotter.plot_histogram(left, self.stat_graph_canvas_frame)
        elif self.__selected == "Correlations":
            self.disable_comboboxes()
            self.plotter.plot_correlation(self.stat_graph_canvas_frame)
        # elif self.__selected == "Stack Bar graph":
        #     self.plotter.plot_stack_bar_graph(left, right,
        #                                       self.stat_graph_canvas_frame)

    def stat_handle_menu_selection(self, event):
        """Handle the selection of a visualization in the Statistics tab."""
        selected = event.widget.get()
        self.selected_visualization = selected

        if selected == "Histogram":
            self.enable_comboboxes()
            self.disable_right_combobox()

            column = self.data_loader.get_column_names
            self.left_attribute_combobox["values"] = column
            self.left_attribute_combobox.set(column[0])

        # elif selected == "Stack Bar graph":
        #     self.enable_comboboxes()
        #
        #     column = self.data_loader.get_column_names
        #     # if numerical, use range instead
        #     numerical_columns = ['age', 'trtbps', 'thalachh', 'oldpeak', 'caa', 'thall']
        #
        #     # Clear the values of comboboxes
        #     self.left_attribute_combobox["values"] = ()
        #     self.right_attribute_combobox["values"] = ()
        #
        #     if self.left_attribute_combobox.get() not in numerical_columns:
        #         # If left attribute is not numerical, add all columns to the comboboxes
        #         self.left_attribute_combobox["values"] = column
        #         self.right_attribute_combobox["values"] = column
        #     else:
        #         # If left attribute is numerical, enable range selection
        #         self.enable_range_selection()
        #
        #         # Set default values for comboboxes
        #     self.left_attribute_combobox.set(column[0])
        #     self.right_attribute_combobox.set(column[1])
        #
        #     # Bind events for combobox selection
        #     self.left_attribute_combobox.bind("<<ComboboxSelected>>", self.validate_comboboxes)
        #     self.right_attribute_combobox.bind("<<ComboboxSelected>>", self.validate_comboboxes)

            # column = self.data_loader.get_column_names
            # self.left_attribute_combobox["values"] = column
            # self.left_attribute_combobox.set(column[0])
            # self.left_attribute_combobox.bind("<<ComboboxSelected>>",
            #                                   self.validate_comboboxes)
            # self.right_attribute_combobox["values"] = column
            # self.right_attribute_combobox.bind("<<ComboboxSelected>>",
            #                                    self.validate_comboboxes)

        if selected == "Bar Charts":
            self.enable_comboboxes()

            allowed_attributes = ["sex", "output", "fbs", "slp"]
            self.left_attribute_combobox["values"] = allowed_attributes
            self.left_attribute_combobox.set(allowed_attributes[0])
            self.left_attribute_combobox.bind("<<ComboboxSelected>>",
                                              self.validate_comboboxes)
            self.right_attribute_combobox["values"] = allowed_attributes
            self.right_attribute_combobox.bind("<<ComboboxSelected>>",
                                               self.validate_comboboxes)

        elif selected == "Correlations":
            pass


    def enable_comboboxes(self):
        """Enable the comboboxes."""
        self.left_attribute_combobox["state"] = "normal"
        self.right_attribute_combobox["state"] = "normal"

    def disable_right_combobox(self):
        """Disable the right combobox."""
        self.right_attribute_combobox.set("")
        self.right_attribute_combobox["state"] = "disabled"

    def disable_comboboxes(self):
        """Disable all the comboboxes."""
        self.left_attribute_combobox.set("")
        self.right_attribute_combobox.set("")
        self.left_attribute_combobox["state"] = "disabled"
        self.right_attribute_combobox["state"] = "disabled"

    def validate_comboboxes(self, event):
        """Validate the selected attributes in the comboboxes."""
        selected_left = self.left_attribute_combobox.get()
        selected_right = self.right_attribute_combobox.get()

        left_enabled = self.left_attribute_combobox["state"] == "normal"
        right_enabled = self.right_attribute_combobox["state"] == "normal"

        # Check if both comboboxes have selections
        if selected_left and selected_right:
            if selected_left == selected_right:
                messagebox.showerror("Error",
                                     "Select different attributes.")
                self.right_attribute_combobox.set("")
        elif not selected_left:
            messagebox.showerror("Error",
                                 "Select an attribute for the left combobox.")
        elif not selected_right and right_enabled:
            messagebox.showerror("Error",
                                 "Select an attribute for the right combobox.")

    def create_quit_button(self):
        """ Button to gracefully exit"""
        self.quit_button = ttk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack(side="bottom", padx=10, pady=10)

    def init_advance_graph_tab(self):
        """This function initializes the graph tab:
        let user create their own interesting in any attributes."""
        # Create another frame for the graph canvas
        self.graph_tab_graph_canvas_frame = tk.Frame(self.adv_graph_tab, width=1020,
                                                     height=400)
        self.graph_tab_graph_canvas_frame.grid(row=5, column=0, columnspan=10,
                                               sticky="nsew", padx=5, pady=5)
        self.adv_graph_tab.rowconfigure(5, weight=1)
        self.adv_graph_tab.columnconfigure(0, weight=1)

        # Create the menu box for selecting the graph type
        graph_type_label = ttk.Label(self.adv_graph_tab, text="Select Graph Type:")
        graph_type_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.graph_type_combobox = ttk.Combobox(self.adv_graph_tab,
                                                values=["Distribution Graph",
                                                        "Scatter Plot",
                                                        "Stack Bar Graph"])
        self.graph_type_combobox.set("Distribution Graph")
        self.graph_type_combobox.grid(row=0, column=1, columnspan=1, padx=5,
                                      pady=5, sticky="ew")
        self.graph_type_combobox.columnconfigure(0, weight=1)
        self.graph_type_combobox.bind("<<ComboboxSelected>>",
                                      self.selected_graph_type_handler)

        # Create the menu box for the 1st attribute
        adv_attr1_label = ttk.Label(self.adv_graph_tab,
                                    text="Select 1st Attribute:")
        adv_attr1_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        # Create the menu box for the 1st attribute
        self.adv_attr1_combobox = ttk.Combobox(self.adv_graph_tab)
        self.adv_attr1_combobox.set(self.data_loader.get_column_names[0])
        self.adv_attr1_combobox.grid(row=1, column=1, columnspan=1, padx=5,
                                     pady=5,
                                     sticky="ew")
        self.adv_attr1_combobox.columnconfigure(0, weight=1)
        self.adv_attr1_combobox.rowconfigure(0, weight=1)

        # Create the menu box for the 2nd attribute
        adv_attr2_label = ttk.Label(self.adv_graph_tab,
                                    text="Select 2nd Attribute:")
        adv_attr2_label.grid(row=1, column=3, padx=5, pady=5, sticky="w")
        adv_attr2_label.bind("<<ComboboxSelected>>",
                             self.update_right_slider_value)

        self.adv_attr2_combobox = ttk.Combobox(self.adv_graph_tab)
        self.adv_attr2_combobox.grid(row=1, column=4, columnspan=1, padx=5,
                                     pady=5,
                                     sticky="ew")
        self.adv_attr2_combobox.columnconfigure(0, weight=1)
        self.adv_attr2_combobox.rowconfigure(0, weight=1)

        # Create labels for attribute range sliders
        adv_left_range_label = ttk.Label(self.adv_graph_tab,
                                         text="Select Range for 1st attribute:")
        adv_left_range_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        adv_right_range_label = ttk.Label(self.adv_graph_tab,
                                          text="Select Range for 2nd attribute:")
        adv_right_range_label.grid(row=2, column=3, padx=5, pady=5, sticky="w")

        # Create range sliders for attribute selection
        self.adv_left_range_slider = ttk.Scale(self.adv_graph_tab, from_=0, to=100,
                                               length=200,
                                               command=self.update_left_slider_value)
        self.adv_left_range_slider.grid(row=2, column=1, padx=5, pady=5,
                                        sticky="w")

        self.adv_right_range_slider = ttk.Scale(self.adv_graph_tab, from_=0,
                                                to=100, length=200,
                                                command=self.update_right_slider_value)
        self.adv_right_range_slider.grid(row=2, column=4, padx=5, pady=5,
                                         sticky="w")

        # Create labels to display current range slider values
        self.adv_left_range_value_label = ttk.Label(self.adv_graph_tab, text="0")
        self.adv_right_range_value_label = ttk.Label(self.adv_graph_tab, text="0")

        # Button to clear range
        clear_button = ttk.Button(self.adv_graph_tab, text="Clear Range",
                                  command=self.clear_range)
        clear_button.grid(row=3, column=0, columnspan=1, padx=5, pady=5)

        self.__create_graph_button = ttk.Button(self.adv_graph_tab,
                                                text="Plot Graph",
                                                command=self.graph_tab_plot_graph)
        self.__create_graph_button.grid(row=3, column=0, padx=5, pady=5,
                                        sticky="w")

        # Create check button to enable attribute selection
        adv_check_label = ttk.Label(self.adv_graph_tab, text="Choose Range?")
        adv_check_label.grid(row=0, column=3, padx=5, pady=5, sticky="w")

        self.adv_check_var = tk.BooleanVar()
        adv_check_button = ttk.Checkbutton(self.adv_graph_tab,
                                           variable=self.adv_check_var,
                                           command=self.toggle_attribute_selection)
        adv_check_button.grid(row=0, column=4, padx=5, pady=5, sticky="w")

        # Initially disable range sliders
        self.toggle_attribute_selection()

    def selected_graph_type_handler(self, event):
        """Handle the selection of a graph type in the Graph tab."""
        graph_selected_graph = self.graph_type_combobox.get()
        if graph_selected_graph == "Distribution Graph":
            self.adv_attr1_combobox["values"] = "age"
            self.adv_attr1_combobox.set("age")
            self.adv_attr2_combobox["values"] = "thalachh"
            self.adv_attr2_combobox.set("thalachh")

        elif graph_selected_graph == "Scatter Plot":
            # scatter_attributes = ["chol", "exng", "trtbps", "thalachh", "caa"]
            scatter_attributes = ["chol", "exng", "trtbps", "thalachh", "caa",
                                  "age", "sex", "output"]
            self.adv_attr1_combobox["values"] = scatter_attributes
            self.adv_attr1_combobox.set(scatter_attributes[0])
            self.adv_attr1_combobox.bind("<<ComboboxSelected>>",
                                         self.graph_validate_comboboxes)
            # if selected already on the first attribute,
            # the second attribute will not be the same as the first attribute.
            self.adv_attr2_combobox["values"] = scatter_attributes
            self.adv_attr2_combobox.bind("<<ComboboxSelected>>",
                                         self.graph_validate_comboboxes)

        elif graph_selected_graph == "Stack Bar Graph":
            column = self.data_loader.get_column_names
            self.adv_attr1_combobox['values'] = column
            self.adv_attr1_combobox.set(column[0])
            self.adv_attr1_combobox.bind("<<ComboboxSelected>>",
                                            self.graph_validate_comboboxes)
            self.adv_attr2_combobox['values'] = column
            self.adv_attr2_combobox.bind("<<ComboboxSelected>>",
                                            self.graph_validate_comboboxes)

    def graph_validate_comboboxes(self, event):
        """Validate the selected attributes in the comboboxes."""
        selected_left = self.adv_attr1_combobox.get()
        selected_right = self.adv_attr2_combobox.get()

        left_enabled = self.adv_attr1_combobox["state"] == "normal"
        right_enabled = self.adv_attr2_combobox["state"] == "normal"

        # Check if both comboboxes have selections
        if selected_left and selected_right:
            if selected_left == selected_right:
                messagebox.showerror("Error", "Select different attributes.")
                self.adv_attr2_combobox.set("")
        elif not selected_left:
            messagebox.showerror("Error",
                                 "Select an attribute for the left combobox.")
        elif not selected_right and right_enabled:
            messagebox.showerror("Error",
                                 "Select an attribute for the right combobox.")

    def clear_range(self):
        """Function to clear the range sliders"""
        self.adv_left_range_slider.set(0)
        self.adv_right_range_slider.set(0)

    def toggle_attribute_selection(self):
        """Enable or disable attribute selection based on the checkbox state"""
        state = "normal" if self.adv_check_var.get() else "disabled"
        self.adv_left_range_slider.config(state=state)
        self.adv_right_range_slider.config(state=state)
        # Show or hide range slider value labels based on the checkbox state
        self.adv_left_range_value_label.grid(row=3, column=1, padx=1, pady=1,
                                             sticky="w")
        self.adv_right_range_value_label.grid(row=3, column=4, padx=1, pady=1,
                                              sticky="w")

    def update_left_slider_value(self, event):
        """Update the label to display the current value of the left range slider"""
        selected_attribute = self.adv_attr1_combobox.get()
        max_value = self.controller.get_max_value(selected_attribute)
        self.adv_left_range_slider.config(to=max_value)
        self.adv_left_range_value_label.config(
            text=str(self.adv_left_range_slider.get()))

    def update_right_slider_value(self, event):
        """Update the label to display the current value of the right range slider"""
        selected_attribute = self.adv_attr2_combobox.get()
        max_value = self.controller.get_max_value(selected_attribute)
        self.adv_right_range_slider.config(to=max_value)
        self.adv_right_range_value_label.config(
            text=str(self.adv_right_range_slider.get()))

    def graph_tab_plot_graph(self):
        """Function to plot the graph based on selected attributes and ranges"""
        # Get the selected graph type
        selected_graph = self.graph_type_combobox.get()

        # Get the selected attributes
        selected_left = self.adv_attr1_combobox.get()
        selected_right = self.adv_attr2_combobox.get()

        # Get the selected ranges
        left_range = self.adv_left_range_slider.get()
        right_range = self.adv_right_range_slider.get()

        # Clear the existing graph canvas
        for widget in self.graph_tab_graph_canvas_frame.winfo_children():
            widget.destroy()

        # Determine if range selection is enabled
        if self.adv_check_var.get():  # If checkbox is checked
            # Plot the graph based on the selected graph type and range
            if selected_graph == "Distribution Graph":
                self.plotter.plot_distribution(selected_left, selected_right,
                                               left_range, right_range,
                                               self.graph_tab_graph_canvas_frame)
            elif selected_graph == "Scatter Plot":
                self.plotter.plot_scatter(selected_left, selected_right,
                                          left_range, right_range,
                                          self.graph_tab_graph_canvas_frame)
            elif selected_graph == "Stack Bar Graph":
                self.plotter.plot_stack_bar_graph(selected_left, selected_right,
                                                  left_range, right_range,
                                                  self.graph_tab_graph_canvas_frame)
        else:  # If checkbox is not checked
            # Plot the graph without considering range
            if selected_graph == "Distribution Graph":
                self.plotter.plot_distribution(selected_left, selected_right,
                                               None, None,
                                               self.graph_tab_graph_canvas_frame)
            elif selected_graph == "Scatter Plot":
                self.plotter.plot_scatter(selected_left, selected_right, None,
                                          None, self.graph_tab_graph_canvas_frame)
            elif selected_graph == "Stack Bar Graph":
                self.plotter.plot_stack_bar_graph(selected_left, selected_right,
                                                  None, None,
                                                  self.graph_tab_graph_canvas_frame)

    def run(self):
        self.mainloop()
