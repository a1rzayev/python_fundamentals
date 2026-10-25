import tkinter
from tkinter import messagebox, ttk

import database
import translator
import logic
from translator import translate


def show_error(parent, message):
    messagebox.showerror(translate("error"), message, parent=parent)


def top_bar(frame, app, title):
    bar = ttk.Frame(frame)
    bar.pack(fill="x", pady=(0, 8))
    ttk.Label(bar, text=title, font="TkHeadingFont").pack(side="left")
    if(app.user == True):
        ttk.Button(bar, text=translate("logout"), command=app.logout).pack(side="right")
    box = ttk.Combobox(bar, values=translator.LANGUAGES, state="readonly", width=13)
    box.current(translator.current)
    box.bind("<<ComboboxSelected>>", lambda e: app.set_language(box.current()))
    box.pack(side="right", padx=8)
    ttk.Label(frame, text=translate("footer")).pack(side="bottom", pady=(8, 0))


def make_table(parent, headings):
    tree = ttk.Treeview(parent, columns=headings, show="headings", height=12)
    for heading in headings:
        tree.heading(heading, text=heading, anchor="w")
    tree.tag_configure("safe", background="#c9efc9", foreground="black") 
    tree.tag_configure("unsafe", background="#f6b8b8", foreground="black") 
    tree.pack(fill="both", expand=True)
    return tree


def allergen_text(names):
    return ", ".join(translator.allergen(name) for name in sorted(names)) or translate("none")


class LoginScreen(ttk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, padding=20)
        self.app = app
        top_bar(self, app, translate("title"))
        form = ttk.Frame(self)
        form.pack(expand=True)
        self.username = tkinter.StringVar()
        self.password = tkinter.StringVar()
        ttk.Label(form, text=translate("username")).grid(row=0, column=0, sticky="e", pady=4)
        user_entry = ttk.Entry(form, textvariable=self.username)
        user_entry.grid(row=0, column=1, pady=4)
        ttk.Label(form, text=translate("password")).grid(row=1, column=0, sticky="e", pady=4)
        password_entry = ttk.Entry(form, textvariable=self.password, show="*")
        password_entry.grid(row=1, column=1, pady=4)
        ttk.Button(form, text=translate("login"), command=self.login).grid(row=2, column=1, pady=8)
        for entry in (user_entry, password_entry):
            entry.bind("<Return>", lambda e: self.login())
        user_entry.focus_set()

    def login(self):
        user = database.login(self.app.conn, self.username.get(), self.password.get())
        if(user is None):
            show_error(self, translate("wrong_login"))
        else:
            self.app.login(user)


class StaffScreen(ttk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, padding=10)
        top_bar(self, app, translate("title"))
        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True)
        for tab in (ListTab(notebook, app, "student"), ListTab(notebook, app, "meal"), AssignTab(notebook, app)):
            notebook.add(tab, text=translate(tab.title))
            tab.refresh()
        notebook.bind("<<NotebookTabChanged>>", lambda e: notebook.nametowidget(notebook.select()).refresh())


class ListTab(ttk.Frame):

    def __init__(self, parent, app, kind):
        super().__init__(parent, padding=10)
        self.conn = app.conn
        self.kind = kind
        self.title = kind + "s" 
        buttons = ttk.Frame(self)
        buttons.pack(fill="x", pady=(0, 6))
        ttk.Button(buttons, text=translate("add"), command=self.add).pack(side="left")
        self.tree = make_table(self, [translate("name"), translate("allergens")])

    def refresh(self):
        self.tree.delete(*self.tree.get_children())
        for row in database.list_all(self.conn, self.kind):
            allergens = allergen_text(database.allergens_of(self.conn, self.kind, row["id"]))
            self.tree.insert("", "end", iid=row["id"], values=(row["name"], allergens))

    def add(self):
        AddDialog(self, self.kind)
        self.refresh()


class AddDialog(tkinter.Toplevel):

    def __init__(self, parent, kind):
        super().__init__(parent)
        self.parent = parent
        self.kind = kind
        self.title(translate("add"))
        self.name = tkinter.StringVar()
        ttk.Label(self, text=translate("name")).grid(row=0, column=0, padx=8, pady=8, sticky="w")
        entry = ttk.Entry(self, textvariable=self.name, width=30)
        entry.grid(row=0, column=1, columnspan=2, pady=8, sticky="w")
        self.ticks = {}
        for i, name in enumerate(database.ALLERGENS):
            self.ticks[name] = tkinter.BooleanVar()
            ttk.Checkbutton(self, text=translator.allergen(name), variable=self.ticks[name]).grid(
                row=1 + i % 7, column=1 + i // 7, sticky="w", padx=8)
        ttk.Button(self, text=translate("save"), command=self.save).grid(row=9, column=2, pady=8, sticky="e")
        self.bind("<Return>", lambda e: self.save())
        self.bind("<Escape>", lambda e: self.destroy())
        entry.focus_set()
        self.wait_visibility()
        self.grab_set() 
        self.wait_window() 

    def save(self):
        ticked = [name for name, var in self.ticks.items() if var.get()]
        try:
            database.add(self.parent.conn, self.kind, self.name.get(), ticked)
        except ValueError as error:
            return show_error(self, str(error))
        self.destroy()


class AssignTab(ttk.Frame):
    title = "assignments"

    def __init__(self, parent, app):
        super().__init__(parent, padding=10)
        self.conn = app.conn
        bar = ttk.Frame(self)
        bar.pack(fill="x", pady=(0, 6))
        ttk.Button(bar, text=translate("auto"), command=self.auto).pack(side="left")
        self.meal_box = ttk.Combobox(bar, state="readonly", width=25)
        self.meal_box.pack(side="left", padx=(20, 6))
        ttk.Button(bar, text=translate("assign"), command=self.assign).pack(side="left")
        self.tree = make_table(self, [translate("name"), translate("allergens"), translate("meal"), translate("safe")])

    def refresh(self):
        self.meals = database.list_all(self.conn, "meal")
        self.meal_box["values"] = [meal["name"] for meal in self.meals]
        self.tree.delete(*self.tree.get_children())
        for student in database.list_all(self.conn, "student"):
            meal = database.assigned_meal(self.conn, student["id"])
            if meal: 
                meal_name, safety, colour = meal["name"], translate("safe"), "safe"
            elif logic.safe_meals(self.conn, student["id"]):
                meal_name, safety, colour = translate("no_meal"), "", ""
            else:
                meal_name, safety, colour = translate("no_meal"), translate("unsafe"), "unsafe"
            allergens = allergen_text(database.allergens_of(self.conn, "student", student["id"]))
            self.tree.insert("", "end", iid=student["id"], tags=(colour,),
                             values=(student["name"], allergens, meal_name, safety))

    def auto(self):
        missing = logic.auto_assign(self.conn)
        self.refresh()
        if missing:
            show_error(self, translate("no_safe_meal", names=", ".join(missing)))

    def assign(self):
        selection = self.tree.selection()
        if not selection or self.meal_box.current() < 0:
            return show_error(self, translate("select"))
        meal_id = self.meals[self.meal_box.current()]["id"]
        try:
            logic.assign_meal(self.conn, int(selection[0]), meal_id)
        except ValueError as error:
            show_error(self, str(error))
        self.refresh()

class StudentScreen(ttk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, padding=20)
        conn, student_id = app.conn, app.user["student_id"]
        name = conn.execute("SELECT name FROM students WHERE id = ?", (student_id,)).fetchone()["name"]
        top_bar(self, app, name)
        meal = database.assigned_meal(conn, student_id)
        ttk.Label(self, text=translate("your_meal")).pack(anchor="w")
        ttk.Label(self, text=meal["name"] if meal else transa("no_meal"), font="TkHeadingFont").pack(anchor="w", pady=(0, 12))
        ttk.Label(self, text=translate("your_allergies")).pack(anchor="w")
        ttk.Label(self, text=allergen_text(database.allergens_of(conn, "student", student_id))).pack(anchor="w")
