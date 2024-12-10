import random
from sty import fg, bg, rs


foreground_colors = [
    fg.red, fg.green, fg.blue, fg.yellow, fg.magenta, fg.cyan, fg.white, fg.black
]


background_colors = [
    bg.red, bg.green, bg.blue, bg.yellow, bg.magenta, bg.cyan, bg.white, bg.black
]

# Fonction pour générer une couleur random
def random_color_text(text):
    fg_color = random.choice(foreground_colors)  
    bg_color = random.choice(background_colors)  
    return f"{fg_color}{bg_color}{text}{rs.all}"  


print(random_color_text("Hello, bad World! 😅"))
print(random_color_text("This is a random colored damn  text 😁"))
