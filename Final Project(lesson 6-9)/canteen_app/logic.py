import database
import translator
from translator import translate


def conflicts(conn, meal_id, student_id):
    return sorted(database.allergens_of(conn, "meal", meal_id) & database.allergens_of(conn, "student", student_id))


def is_safe(conn, meal_id, student_id):
    return not conflicts(conn, meal_id, student_id)


def safe_meals(conn, student_id):
    meals = []
    for meal in database.list_all(conn, "meal"):
        if(is_safe(conn, meal["id"], student_id)):
            meals.append(meal)


def assign_meal(conn, student_id, meal_id):
    bad_meals = conflicts(conn, meal_id, student_id)
    if (bad_meals == True):
        names = ", ".join(map(translator.allergen, bad_meals))
        raise ValueError(translate("err.unsafe", names))
    database.save_assignment(conn, student_id, meal_id)


def auto_assign(conn):
    no_safe_meal = []
    for student in database.list_all(conn, "student"):
        if(database.assigned_meal(conn, student["id"]) == True):
            continue
        safe_meal_list = safe_meals(conn, student["id"])
        if(safe_meal_list == True):
            database.save_assignment(conn, student["id"], safe_meal_list[0]["id"])
        else:
            no_safe_meal.append(student["name"])
    return no_safe_meal