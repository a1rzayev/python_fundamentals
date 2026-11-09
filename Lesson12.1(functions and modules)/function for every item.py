def shout(text:str):
    return text.upper() + "!"

def apply_to_everything(items, function):
    result = []
    for item in items:
        result.append(function(item))
    return result

print(apply_to_everything(["Asif", "Muradkhan"], shout))
print(apply_to_everything([1.23453, 1.799], round))