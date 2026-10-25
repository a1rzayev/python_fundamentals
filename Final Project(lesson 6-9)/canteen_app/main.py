import tkinter
import database
import translator
import ui

class App:
    def __init__(self, root, conn):
        self.root = root
        self.conn = conn
        self.user = None
        self.screen = None
        root.geometry("900x550")
        self.show_screen()

    def show_screen(self):
        typed = ("", "")
        if(isinstance(self.screen, ui.LoginScreen)):
            typed = (self.screen.username.get(), self.screen.password.get())
        if(self.screen is not None):
            self.screen.destroy()
        if(self.user is None):
            self.screen = ui.LoginScreen(self.root, self, *typed)
        elif(self.user["role"] == "staff"):
            self.screen = ui.StaffScreen(self.root, self)
        else:
            self.screen = ui.StudentScreen(self.root, self)
        self.screen.pack(fill="both", expand=True)
        self.root.title(translator.translate("title"))

    def login(self, user):
        self.user = user
        self.show_screen()

    def logout(self):
        self.user = None
        self.show_screen()

    def set_language(self, index):
        translator.current = index
        self.root.after_idle(self.show_screen)

if __name__ == "__main__":
    root = tkinter.Tk()
    App(root, database.connect())
    root.mainloop()
