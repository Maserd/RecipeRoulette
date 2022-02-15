import random
from tkinter import *
from tkinter.ttk import *

''' Opens the text file that the functions will write a https://www.simplyrecipes.com/ to for the microservice'''
r = open("input.txt", 'r+')
t = open("tester.txt", 'r+')


def mainPage():
    """ Window configurations for the main page """
    window = Tk()
    window.columnconfigure(0, weight=1, minsize=250)
    window.rowconfigure([0, 6], weight=1, minsize=100)
    window.title('Recipe Roulette')
    window.geometry('750x750')

    ''' Style profile for the labels '''
    style = Style()
    style.configure('W.TLabel', font=('times news roman', 24, 'bold'),
                    fg='Black')

    ''' Style profile for the buttons '''
    style = Style()
    style.configure('W.TButton', font=('times news roman', 12, 'bold'),
                    fg='Black')

    prompt = Label(text="How would you like to filter your result?",
                   style='W.TLabel')
    prompt.grid(row=0, column=0)

    ''' Button 1'''
    opt1 = Button(window, text='The Base of the Dish',
                  style='W.TButton',
                  command=baseDishWindow)
    opt1.grid(row=3, column=0, pady=10, padx=100)

    ''' Button 2'''

    opt2 = Button(window, text='The Region of Origin',
                  style='W.TButton',
                  command=regionWindow)
    opt2.grid(row=4, column=0, pady=10, padx=100)

    ''' Button 3'''

    opt3 = Button(window, text='Neither',
                  style='W.TButton',
                  command=randomWindow)
    opt3.grid(row=5, column=0, pady=10, padx=100)

    window.mainloop()


def baseDishWindow():
    baseDishWindow = Tk()
    baseDishWindow.columnconfigure(0, weight=1, minsize=250)
    baseDishWindow.rowconfigure([0, 8], weight=1, minsize=100)
    baseDishWindow.title('Filter by Base')
    baseDishWindow.geometry('750x750')


    ''' Style profile for the buttons '''
    style = Style()
    style.configure('W.TButton', font=('times news roman', 12, 'bold'),
                    fg='Black')

    ''' Button 1'''
    chx = Button(baseDishWindow, text='Chicken',
                 style='W.TButton',
                 command=chickenRecipe)
    chx.grid(row=1, column=0, pady=10, padx=100)

    ''' Button 2'''
    beef = Button(baseDishWindow, text='Beef',
                  style='W.TButton',
                  command=beefRecipe)
    beef.grid(row=2, column=0, pady=10, padx=100)

    ''' Button 3'''
    pork = Button(baseDishWindow, text='Pork',
                  style='W.TButton')
    pork.grid(row=3, column=0, pady=10, padx=100)

    ''' Button 4'''
    fish = Button(baseDishWindow, text='Fish',
                  style='W.TButton',
                  command=fishRecipe)
    fish.grid(row=4, column=0, pady=10, padx=100)

    ''' Button 5'''
    seafood = Button(baseDishWindow, text='Seafood',
                     style='W.TButton',
                     command=seafoodRecipe)
    seafood.grid(row=5, column=0, pady=10, padx=100)

    ''' Button 6'''
    pasta = Button(baseDishWindow, text='Pasta',
                   style='W.TButton',
                   command=pastaRecipe)
    pasta.grid(row=6, column=0, pady=10, padx=100)

    ''' Button 7'''
    meatSub = Button(baseDishWindow, text='Meat Substitute',
                     style='W.TButton',
                     command=meatSubRecipe)
    meatSub.grid(row=7, column=0, pady=10, padx=100)


def regionWindow():
    regionWindow = Tk()
    regionWindow.columnconfigure(0, weight=1, minsize=250)
    regionWindow.rowconfigure([0, 7], weight=1, minsize=100)
    regionWindow.title('Filter by Region')
    regionWindow.geometry('750x750')

    ''' Style profile for the buttons '''
    style = Style()
    style.configure('W.TButton', font=('times news roman', 12, 'bold'),
                    fg='Black')

    ''' Button 1'''
    nAmerica = Button(regionWindow, text='North America',
                      style='W.TButton',
                      command=nAmericanRecipe)
    nAmerica.grid(row=1, column=0, pady=10, padx=100)

    ''' Button 2'''
    sAmerica = Button(regionWindow, text='South America',
                      style='W.TButton',
                      command=sAmericanRecipe)
    sAmerica.grid(row=2, column=0, pady=10, padx=100)

    ''' Button 3'''
    africa = Button(regionWindow, text='Africa',
                    style='W.TButton',
                    command=africaRecipe)
    africa.grid(row=3, column=0, pady=10, padx=100)

    ''' Button 4'''
    europe = Button(regionWindow, text='Europe',
                    style='W.TButton',
                    command=europeRecipe)
    europe.grid(row=4, column=0, pady=10, padx=100)

    ''' Button 5'''
    asia = Button(regionWindow, text='Asia',
                  style='W.TButton',
                  command=asiaRecipe)
    asia.grid(row=5, column=0, pady=10, padx=100)

    ''' Button 6'''
    australia = Button(regionWindow, text='Australia',
                       style='W.TButton',
                       command=australiaRecipe)
    australia.grid(row=6, column=0, pady=10, padx=100)


def randomWindow():
    randomWindow = Tk()
    randomWindow.columnconfigure(0, weight=1, minsize=250)
    randomWindow.rowconfigure(0, weight=1, minsize=100)
    randomWindow.title('Random Recipe')
    randomWindow.geometry('750x750')
    back = Button(randomWindow, text='Back', command=randomWindow.destroy)
    back.pack()

    recipes = ["smothered-chicken-thighs-in-onion-gravy-recipe-5203984",
               "recipes/slow_cooker_beef_bourguignon/",
               "/recipes/pressure_cooker_mexican_pulled_pork/",
               "grilled-whole-fish-stuffed-with-herbs-and-chilies-recipe-5203428",
               "recipes/clam_chowder/",
               "recipes/pasta_with_butternut_parmesan_sauce/",
               "spicy-tofu-stir-fry-recipe-5115374",
               "recipes/moroccan_pot_roast/",
               "recipes/skirt_steak_with_avocado_chimichurri/",
               "recipes/african_chicken_peanut_stew/",
               "recipes/venison_sauerbraten/",
               "recipes/grilled_chicken_satay_with_peanut_sauce/",
               "crash-hot-potatoes-with-smoked-salmon-recipe-5211692"]
    choice = random.randint(0, 12)
    try:
        r = open("input.txt", 'r+')
        r.write("https://www.simplyrecipes.com/" + recipes[choice])
        r.close()
    except IOError:
        print("File not found.")
    if t.seek(0) is not None:
        write = Label(randomWindow,
                      text=t.read())
        write.pack()


def chickenRecipe():
    recipes = ["smothered-chicken-thighs-in-onion-gravy-recipe-5203984"]
    choice = random.randint(0, 0)
    try:
        r = open("input.txt", 'r+')
        r.write("https://www.simplyrecipes.com/" + recipes[choice])
        r.close()
    except IOError:
        print("File not found.")
    if t.seek(0) is not None:
        write = Label(Tk(),
                      text=t.read())
        write.pack()


def beefRecipe():
    recipes = ["recipes/slow_cooker_beef_bourguignon/"]
    choice = random.randint(0, 0)

    r.write("https://www.simplyrecipes.com/" + recipes[choice])
    if t.seek(0) is not None:
        write = Label(Tk(),
                      text=t.read())
        write.pack()


def porkRecipe():
    recipes = ["/recipes/pressure_cooker_mexican_pulled_pork/"]
    choice = random.randint(0, 0)
    try:
        r = open("input.txt", 'r+')
        r.write("https://www.simplyrecipes.com/" + recipes[choice])
        r.close()
    except IOError:
        print("File not found.")
    if t.seek(0) is not None:
        write = Label(Tk(),
                      text=t.read())
        write.pack()


def fishRecipe():
    recipes = ["grilled-whole-fish-stuffed-with-herbs-and-chilies-recipe-5203428"]
    choice = random.randint(0, 0)
    try:
        r = open("input.txt", 'r+')
        r.write("https://www.simplyrecipes.com/" + recipes[choice])
        r.close()
    except IOError:
        print("File not found.")
    if t.seek(0) is not None:
        write = Label(Tk(),
                      text=t.read())
        write.pack()


def seafoodRecipe():
    recipes = ["recipes/clam_chowder/"]
    choice = random.randint(0, 0)
    try:
        r = open("input.txt", 'r+')
        r.write("https://www.simplyrecipes.com/" + recipes[choice])
        r.close()
    except IOError:
        print("File not found.")
    if t.seek(0) is not None:
        write = Label(Tk(),
                      text=t.read())
        write.pack()


def pastaRecipe():
    recipes = ["recipes/pasta_with_butternut_parmesan_sauce/"]
    choice = random.randint(0, 0)
    try:
        r = open("input.txt", 'r+')
        r.write("https://www.simplyrecipes.com/" + recipes[choice])
        r.close()
    except IOError:
        print("File not found.")
    if t.seek(0) is not None:
        write = Label(Tk(),
                      text=t.read())
        write.pack()


def meatSubRecipe():
    recipes = ["spicy-tofu-stir-fry-recipe-5115374"]
    choice = random.randint(0, 0)
    try:
        r = open("input.txt", 'r+')
        r.write("https://www.simplyrecipes.com/" + recipes[choice])
        r.close()
    except IOError:
        print("File not found.")
    if t.seek(0) is not None:
        write = Label(Tk(),
                      text=t.read())
        write.pack()


def nAmericanRecipe():
    recipes = ["recipes/moroccan_pot_roast/"]
    choice = random.randint(0, 0)
    try:
        r = open("input.txt", 'r+')
        r.write("https://www.simplyrecipes.com/" + recipes[choice])
        r.close()
    except IOError:
        print("File not found.")
    if t.seek(0) is not None:
        write = Label(Tk(),
                      text=t.read())
        write.pack()


def sAmericanRecipe():
    recipes = ["recipes/skirt_steak_with_avocado_chimichurri/"]
    choice = random.randint(0, 0)
    try:
        r = open("input.txt", 'r+')
        r.write("https://www.simplyrecipes.com/" + recipes[choice])
        r.close()
    except IOError:
        print("File not found.")
    if t.seek(0) is not None:
        write = Label(Tk(),
                      text=t.read())
        write.pack()


def africaRecipe():
    recipes = ["recipes/african_chicken_peanut_stew/"]
    choice = random.randint(0, 0)
    try:
        r = open("input.txt", 'r+')
        r.write("https://www.simplyrecipes.com/" + recipes[choice])
        r.close()
    except IOError:
        print("File not found.")
    if t.seek(0) is not None:
        write = Label(Tk(),
                      text=t.read())
        write.pack()


def europeRecipe():
    recipes = ["recipes/venison_sauerbraten/"]
    choice = random.randint(0, 0)
    try:
        r = open("input.txt", 'r+')
        r.write("https://www.simplyrecipes.com/" + recipes[choice])
        r.close()
    except IOError:
        print("File not found.")
    if t.seek(0) is not None:
        write = Label(Tk(),
                      text=t.read())
        write.pack()


def asiaRecipe():
    recipes = ["recipes/grilled_chicken_satay_with_peanut_sauce/"]
    choice = random.randint(0, 0)
    try:
        r = open("input.txt", 'r+')
        r.write("https://www.simplyrecipes.com/" + recipes[choice])
        r.close()
    except IOError:
        print("File not found.")
    if t.seek(0) is not None:
        write = Label(Tk(),
                      text=t.read())
        write.pack()


def australiaRecipe():
    recipes = ["crash-hot-potatoes-with-smoked-salmon-recipe-5211692"]
    choice = random.randint(0, 0)
    try:
        r = open("input.txt", 'r+')
        r.write("https://www.simplyrecipes.com/" + recipes[choice])
        r.close()
    except IOError:
        print("File not found.")
    if t.seek(0) is not None:
        write = Label(Tk(),
                      text=t.read())
        write.pack()


mainPage()
