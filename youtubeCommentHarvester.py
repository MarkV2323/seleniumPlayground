import tkinter
import customtkinter

"""
Author: Mark Vincent
Summary: This program will take a youtube video URL and produce a text file containing all
         of the comments posted onto the video.
"""


# Youtube Scrape Pipeline
def youtube_scrape_pipeline(url_scrape: str, save_path: str):
    pass


# Main Application Window Declaration
class MainApp(customtkinter.CTk):
    # MainApp Constants
    APPEARANCE_MODE = "dark"
    DEFAULT_COLOR_THEME = "dark-blue"
    WINDOW_TITLE = "Youtube Comment Scraper by Mark!"
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 240

    # initialization of MainApp Window
    def __init__(self):
        # MainApp Constants
        _FRAME_X_PAD = 20
        _FRAME_Y_PAD = 20
        _COMMON_X_PAD = 10
        _COMMON_Y_PAD = 10

        # perform default init settings
        super().__init__()

        # setup default appearance and theme
        customtkinter.set_appearance_mode(MainApp.APPEARANCE_MODE)
        customtkinter.set_default_color_theme(MainApp.DEFAULT_COLOR_THEME)

        # configure MainApp window settings
        self.title(MainApp.WINDOW_TITLE)
        self.geometry(f"{MainApp.WINDOW_WIDTH}x{MainApp.WINDOW_HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # Calls on_closing when application closed by X.
        self.minsize(MainApp.WINDOW_WIDTH, MainApp.WINDOW_HEIGHT)
        self.maxsize(MainApp.WINDOW_WIDTH, MainApp.WINDOW_HEIGHT)

        # build widget frame
        self.widget_frame = customtkinter.CTkFrame(master=self)
        self.widget_frame.grid(row=0, column=0, sticky="nswe",
                               padx=_FRAME_X_PAD,
                               pady=_FRAME_Y_PAD)

        # build title_label
        self.title_label = customtkinter.CTkLabel(master=self.widget_frame,
                                                  width=MainApp.WINDOW_WIDTH - 2 * _FRAME_X_PAD - 2 * _COMMON_X_PAD,
                                                  text="Youtube Comment Scraper",
                                                  text_font=("Roboto Medium", -26))  # font name and size in px
        self.title_label.grid(row=0, column=0, padx=_COMMON_X_PAD, pady=_COMMON_Y_PAD)

        # build url_entry
        self.url_entry = customtkinter.CTkEntry(master=self.widget_frame,
                                                width=MainApp.WINDOW_WIDTH - 2 * _FRAME_X_PAD - 2 * _COMMON_X_PAD,
                                                placeholder_text="Paste Youtube video URL here!")
        self.url_entry.grid(row=1, column=0, columnspan=2, padx=_COMMON_X_PAD, pady=_COMMON_Y_PAD)

        # build save_path_entry
        self.save_path_entry = customtkinter.CTkEntry(master=self.widget_frame,
                                                      width=MainApp.WINDOW_WIDTH - 2 * _FRAME_X_PAD - 2 * _COMMON_X_PAD,
                                                      placeholder_text="Paste path to save text file at here!")
        self.save_path_entry.grid(row=2, column=0, columnspan=2, padx=_COMMON_X_PAD, pady=_COMMON_Y_PAD)

        # build start_button
        self.start_button = customtkinter.CTkButton(master=self.widget_frame,
                                                    text="Start Scrape",
                                                    border_width=2,  # <- custom border_width
                                                    command=self.on_start_button_click)
        self.start_button.grid(row=3, column=0, padx=_COMMON_X_PAD, pady=_COMMON_Y_PAD)

    # things to do on start_button being clicked
    def on_start_button_click(self):
        # disable entries
        self.url_entry.config(state="disabled")
        self.save_path_entry.config(state="disabled")

        # ensure input from url_entry is valid youtube video url.
        url_text = self.url_entry.get()
        save_path = self.save_path_entry.get()
        if "https://www.youtube.com/watch?v=" not in url_text:
            # throw error popup for invalid URL.
            print(f"Invalid url_text!")

        # call scrape pipeline with input as parameters.
        youtube_scrape_pipeline(url_text, save_path)

        # cleanup
        self.url_entry.config(state="normal")
        self.save_path_entry.config(state="normal")

    # things to do on closing of MainApp Window
    def on_closing(self, event=0):
        self.destroy()


# run MainApp program.
if __name__ == "__main__":
    mainApp = MainApp()
    mainApp.mainloop()
