from functools import wraps

def login_required(func):

    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get("is_authenticated"):
            print("Access denied")
            return None
        
        return func(user, *args, **kwargs)
    return wrapper

@login_required
def dashboard(user):
    print("Welcome to your dashboard!")

user = {
    "username": "Asif",
    "is_authenticated": True
}

dashboard(user)