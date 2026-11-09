def shout(text:str):
    return text.upper() + "!"

def whisper(text:str):
    return text.lower() + "....."

def speak(text:str, style):
    return style(text)

print(speak("Hello Muradkhan", shout))
print(speak("Hello Muradkhan", whisper))
print(speak("Hello Muradkhan", str.title))
print(speak("Hello Muradkhan", str.capitalize))