LANGUAGES = ["English", "Azərbaycanca", "Русский"]
current = 0

def translate(key, **values):
    return TEXTS[key][current].format(**values)

def allergen(name):
    if(name in ALLERGEN_NAMES):
        return ALLERGEN_NAMES[name][current]
    else:
        name

TEXTS = {
    "title": ("Canteen Allergy Manager", "Yeməkxana Allergiya Meneceri", "Менеджер аллергий столовой"),
    "footer": ("This tool supports staff decisions. Always verify allergy information directly.",
               "Bu proqram işçilərə kömək edir. Allergiya məlumatlarını həmişə birbaşa yoxlayın.",
               "Программа помогает сотрудникам. Всегда проверяйте информацию об аллергиях напрямую."),
    "username": ("Username:", "İstifadəçi adı:", "Имя пользователя:"),
    "password": ("Password:", "Şifrə:", "Пароль:"),
    "login": ("Log in", "Daxil ol", "Войти"),
    "logout": ("Log out", "Çıxış", "Выйти"),
    "wrong_login": ("Wrong username or password.", "İstifadəçi adı və ya şifrə yanlışdır.",
                    "Неверное имя пользователя или пароль."),
    "students": ("Students", "Şagirdlər", "Ученики"),
    "meals": ("Meals", "Yeməklər", "Блюда"),
    "assignments": ("Assignments", "Təyinatlar", "Назначения"),
    "name": ("Name", "Ad", "Имя"),
    "allergens": ("Allergens", "Allergenlər", "Аллергены"),
    "meal": ("Meal", "Yemək", "Блюдо"),
    "add": ("Add...", "Əlavə et...", "Добавить..."),
    "save": ("Save", "Yadda saxla", "Сохранить"),
    "auto": ("Auto-assign safe meals", "Təhlükəsiz yeməkləri təyin et", "Назначить безопасные блюда"),
    "assign": ("Assign selected meal", "Seçilmiş yeməyi təyin et", "Назначить выбранное блюдо"),
    "safe": ("Safe", "Təhlükəsiz", "Безопасно"),
    "unsafe": ("No safe meal", "Təhlükəsiz yemək yoxdur", "Нет безопасного блюда"),
    "none": ("none", "yoxdur", "нет"),
    "no_meal": ("No meal yet", "Hələ yemək yoxdur", "Блюдо ещё не назначено"),
    "no_safe_meal": ("No safe meal for: {names}", "Təhlükəsiz yemək yoxdur: {names}",
                     "Нет безопасного блюда для: {names}"),
    "select": ("Please select a row first.", "Əvvəlcə sətir seçin.", "Сначала выберите строку."),
    "error": ("Error", "Xəta", "Ошибка"),
    "your_meal": ("Your meal:", "Sizin yeməyiniz:", "Ваше блюдо:"),
    "your_allergies": ("Your allergies:", "Allergiyalarınız:", "Ваши аллергии:"),
    "err.empty": ("The name can't be empty.", "Ad boş ola bilməz.", "Имя не может быть пустым."),
    "err.exists": ("That name already exists.", "Bu ad artıq var.", "Такое имя уже есть."),
    "err.unsafe": ("This meal is UNSAFE for this student (contains: {allergens}).",
                   "Bu yemək bu şagird üçün TƏHLÜKƏLİDİR (tərkibində: {allergens}).",
                   "Это блюдо ОПАСНО для ученика (содержит: {allergens})."),
}

ALLERGEN_NAMES = {
    "celery": ("celery", "kərəviz", "сельдерей"),
    "gluten": ("gluten", "qlüten", "глютен"),
    "crustaceans": ("crustaceans", "xərçəngkimilər", "ракообразные"),
    "eggs": ("eggs", "yumurta", "яйца"),
    "fish": ("fish", "balıq", "рыба"),
    "lupin": ("lupin", "lupin", "люпин"),
    "milk": ("milk", "süd", "молоко"),
    "molluscs": ("molluscs", "molyusklar", "моллюски"),
    "mustard": ("mustard", "xardal", "горчица"),
    "tree nuts": ("tree nuts", "qoz-fındıq", "орехи"),
    "peanuts": ("peanuts", "yer fındığı", "арахис"),
    "sesame": ("sesame", "küncüt", "кунжут"),
    "soya": ("soya", "soya", "соя"),
    "sulphites": ("sulphites", "sulfitlər", "сульфиты"),
}
