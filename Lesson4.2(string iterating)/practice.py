text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Morbi aliquam velit ipsum, in laoreet tortor suscipit a. 
Sed sit amet imperdiet purus. Etiam finibus magna et urna 
feugiat, nec volutpat sem imperdiet. Phasellus finibus 
massa augue, pretium sagittis neque molestie at. Sed eu 
sollicitudin turpis. Nunc porta volutpat quam, sed sagittis 
lacus condimentum quis. Ut metus tortor, imperdiet vel 
finibus at, tempus a quam. Nulla mollis pellentesque egestas.

Cras porttitor condimentum semper. Donec sodales sem et diam rhoncus, nec consectetur nisi congue. Quisque sed placerat metus. Donec finibus enim ac bibendum posuere. Nunc ac urna sagittis, posuere magna non, scelerisque libero. Sed in dapibus dui. Morbi feugiat odio sed bibendum hendrerit. In arcu elit, iaculis et rhoncus a, sagittis a quam. Nunc fermentum, elit non placerat lobortis, ex quam consectetur dui, ut semper libero risus a orci. Phasellus venenatis nunc lectus, in consectetur nunc congue in. Sed ligula eros, tincidunt sed tristique a, gravida porta neque. Nullam a varius nunc. Integer sed purus libero. Nam posuere pellentesque quam, in tristique nulla tristique non.

Sed in felis est. Aliquam at consequat dui, a consequat lectus. Sed tempus, ipsum eget lobortis cursus, ligula nunc tempor mi, non finibus neque quam sed ligula. Praesent at justo dui. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Sed varius dolor at ante suscipit eleifend. In ultrices condimentum tortor in tempus. Quisque ullamcorper quis quam in molestie. Proin sit amet ipsum a tortor lacinia efficitur egestas nec sem. Praesent eu luctus urna.

Nullam suscipit luctus congue. Integer eu porta augue. Nullam sagittis ligula sed eros fermentum iaculis. In ullamcorper in nunc vel finibus. Nullam mi turpis, bibendum nec tincidunt eu, lacinia nec diam. Quisque ultrices porta velit, vulputate elementum nunc vestibulum sit amet. Curabitur eros sapien, pellentesque nec lacinia ac, venenatis eu erat. Cras vitae interdum nunc. Nunc a bibendum lacus. Maecenas condimentum, elit in porttitor auctor, nisl dui ornare nunc, a varius sem ipsum et quam. Aliquam dictum ullamcorper eleifend. Suspendisse erat nibh, porttitor at tempus ut, convallis laoreet turpis. Pellentesque nec tortor sed nibh sodales cursus. Nunc quis mauris nec ligula dictum iaculis. Duis malesuada volutpat orci, viverra scelerisque neque gravida eu. Phasellus eros risus, elementum ac lorem et, egestas gravida arcu.

Vivamus elit lectus, porttitor et dui et, vestibulum consectetur felis. Cras ultrices odio eu lorem porta, eget bibendum enim posuere. Duis sed est tellus. Curabitur sit amet aliquam ex. In sapien erat, facilisis eget accumsan vitae, tempor ac mauris. Nam tortor enim, imperdiet quis turpis vel, cursus pretium ligula. Etiam eu ornare elit. Morbi nulla dui, convallis non porta a, lobortis sed justo.
"""

keyword = "lorem"
word_count = 0

# Hello. How are you, Muradkhan

text_list = text.split(".") 
print(text_list, "\n\n")  # ["Hello", "How are you, Muradkhan"]

text_list = text.split(",")
print(text_list, "\n\n") # ["Hello", "How are you", "Muradkhan"]

text_list = text.split()
print(text_list, "\n\n") # ["Hello", "How", "are", "you", "Muradkhan"]

print(text_list)
for word in text_list:
    if(word == keyword):
        word_count += 1
print(word_count)
