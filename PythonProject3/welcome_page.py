import customtkinter as ctk

class WelcomePage(ctk.CTkFrame):
    def __init__(self, controller):
        super().__init__(controller)
        self.controller = controller

        self.label = ctk.CTkLabel(self, text="Welcome to Belfast Celtic FC", font=("Arial", 24), text_color="green")
        self.label.pack(pady=20)

        self.login_button = ctk.CTkButton(self, text="Log In", command=self.controller.show_login_page)
        self.login_button.pack(pady=10)

        self.signup_button = ctk.CTkButton(self, text="Sign Up", command=self.controller.show_signup_page)
        self.signup_button.pack(pady=10)
