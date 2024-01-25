import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from features_full import Features

usr = Features()

carsJson = {"Acura": ["Cl"],
            "Alfa_Romeo": ["Stelvio", "Sportwagon", "159", "Giulietta", "Mito", "Brera", "155", "Spider", "156", "147",
                           "Gt"],
            "Audi": ["Tt", "Rs3", "S8", "Rs", "Ttcoupe", "A4", "A1", "A5", "A6", "S1", "S4", "80", "S6", "A3", "Q2",
                     "A8", "Q7", "Rs5", "Q5", "Sq5", "Tts", "A7", "Q3", "Sq2", "S5", "S3"],
            "BMW": ["3", "M6", "7", "5", "X5", "8", "M4", "X4", "X1", "2", "1", "4", "6", "I3", "X2", "M3", "Z4", "X3",
                    "X6", "Mini", "Z3", "X7"], "Bentley": ["BENTLEY", "-", "Continental", "Navy"],
            "Bmw_Alpina": ["Xd3"], "Cadillac": ["Xt4", "Sts", "Eldorado", "Cade", "Srx", "Concourse"],
            "Chevrolet": ["Sonic", "Astro", "Blazer", "Camaro", "Cvl"],
            "Chrysler": ["Ypsilon", "Pt", "Durango", "300c", "Voyager", "300", "Grand", "Ram"],
            "Citroen": ["Ds4", "Berlingo", "C5", "Grand", "Ds3", "Saxo", "C6", "C4", "C3", "Ds7"],
            "Dodge": ["Nitro", "Magnum", "Te."],
            "Daihatsu": ["Wake", "Hijet", "Be", "Storia", "Atrai", "Delta", "Sonica", "Naked", "Max", "Gran", "Coo",
                         "Copen", "Mira", "Opti", "Terios", "Esse", "Midget", "Move", "Boon", "Tanto", "Cast", "Rocky",
                         "Thor", "Taft"], "Ferrari": ["Roma", "F430"],
            "Fiat": ["500", "New", "Panda", "500x", "Abarth"],
            "Ford": ["Ecosport", "Focus", "Festiva", "FORD", "Expedition", "Escape", "Fiesta", "Explorer", "Fo",
                     "Mustang", "Lincoln", "Kuga"], "Gmc": ["GMC", "Express", "Chevrolet", "Cadillac", "Yukon"],
            "Hino": ["Profia", "HINO", "Dutro", "Dutoro", "Ranger", "Blue", "Liesse"], "Hummer": ["H3"],
            "Infiniti": ["G37", "In", "Fx35"], "Jaguar": ["X", "E-pace", "F-pace", "Xf", "Xk", "F-type", "Xe", "Xj6"],
            "Jeep": ["Renegade", "Commander", "Compass", "Cherokee", "Wrangler", "Patriot", "Grand"],
            "Komatsu": ["KOMATSU"], "Lamborghini": ["Murcielago", "Gayarusp4w"], "Lancia": ["Dedra"],
            "Land_Rover": ["Range", "Defender", "Freelander", "Lr", "Discovery"],
            "Lexus": ["LX", "CT", "LC", "RC", "HS", "UX", "ES", "NX", "SC", "RX", "GS", "IS", "LS"],
            "Lincoln": ["Navigation"],
            "Mazda": ["Cx-5", "Efini", "Bongo", "Verisa", "Cx-8", "Cx-60", "Rx-8", "Mazda2", "Mazda6", "Az", "Flair",
                      "Spiano", "Demio", "Rx-7", "Scrum", "Cx-30", "Premacy", "Mx-30", "Eunos", "Mpv", "Carol",
                      "Proceed", "Speed", "Mazda3", "Porter", "Cx-3", "Atenza", "Titan", "Roadster", "Capella", "Cx-7",
                      "Familia", "Biante", "Axela"],
            "Mitsubishi": ["Delica", "Fto", "Galant", "Combine", "Toppo", "Jeep", "Airtrek", "Wheel", "Mirage", "Ek",
                           "Town", "Grandis", "Triton", "I", "Legnum", "Chariot", "Bulldozer", "Diamante", "I-miev",
                           "G", "Canter", "Outlander", "Proudia", "Lancer", "Rvr", "Fuso", "Minica", "Pajero", "Dion",
                           "Eclipse", "Colt", "Gto", "Minicab"],
            "Maserati": ["Levante", "Ghibli", "Quattroporte", "Gran"],
            "Mercedes-Benz": ["Eqc", "Slc", "E", "Eqb", "Benz", "Gle", "Mb", "C", "Slk", "R", "Sl", "Glb", "Cla", "Cls",
                              "G", "Cl", "Clk", "V", "Glk", "M", "S", "Amg", "Viano", "A", "Gla", "B", "Glc", "Gls",
                              "E-class"], "Mg": ["Rv8"], "Mini": ["Yuatsu", "Mini"],
            "Mitsuoka": ["Galue", "Viewt", "Ryoga"], "Nissan_Diesel_%28ud%29": ["Condor"],
            "Peugeot": ["3008", "308", "406", "5008", "Rifter", "208", "Rcz", "207", "407", "508", "2008", "307",
                        "1007", "E-208"],
            "Porsche": ["Macan", "718", "Cayenne", "Boxster", "911", "PORSCHE", "944", "Panamera"],
            "Renault": ["Megane", "Captur", "Kangoo", "Twingo", "Lutecia"], "Rolls Royce": ["Phantom", "Rolls"],
            "Nissan": ["Nv100", "Dayz", "X-trail", "Caravan", "Condor", "E-nv200", "Juke", "Laurel", "Sylphy",
                       "Wingroad", "Pulsar", "Infiniti", "Teana", "Fuga", "Figaro", "Gloria", "Homy", "Note", "Nt450",
                       "Rasheen", "Presage", "Atlas", "Stagea", "Cima", "Liberty", "Bluebird", "Micra", "Skyline",
                       "Vanette", "Leopard", "Avenir", "Pino", "Sunny", "Bassara", "Be-1", "Cube", "Gt-r", "Sakura",
                       "Kicks", "Lafesta", "Primera", "Roox", "180sx", "Nv350", "Latio", "Kix", "Elgrand", "Expert",
                       "K", "Tino", "Cefiro", "Datsun", "Safari", "March", "Ud", "Clipper", "President", "Serena",
                       "Fairlady", "Leaf", "Silvia", "Nv150", "Aura", "Terrano", "Moco", "Otti", "Nv200", "Civilian",
                       "S-cargo", "Dualis", "Nt100", "Murano", "Ad", "Tiida", "Cedric"], "Rover": ["Mini"],
            "Saab": ["9-5x"], "Smart": ["Fortwo", "Fourfour", "Coupe", "K", "Roadster"],
            "VW": ["European", "T-cross", "Sirocco", "Bus", "New", "Polo", "Beetle", "Golf", "Vanagon", "Type", "Up",
                   "Touareg", "The", "Tiguan", "Arteon", "Lupo", "Up!", "Jetta", "T-roc", "Sharan", "Passat"],
            "Volvo": ["S60", "V90", "Xc60", "240", "Xc90", "V60", "S40", "960", "S90", "Xc70", "850", "Xc40", "V50",
                      "V70", "V40", "C70"],
            "Honda": ["Freed", "Acty", "N-wgn", "Cr-v", "Airwave", "Freed+", "Inspire", "Fit", "S660", "Live", "N", "E",
                      "Accord", "Z", "Capa", "Hr-v", "Avancier", "Jade", "Zr-v", "Stream", "Zest", "Today", "Edix",
                      "Thats", "Element", "Vezel", "N-van", "Prelude", "Crossroad", "Shuttle", "Civic", "Legend",
                      "Electrical", "Grace", "Cr-z", "Odyssey", "Elysion", "Lagreat", "Mobilio", "Stepwgn", "Integra",
                      "Saber", "Vamos", "Gyro", "N-one", "Street", "N-box", "Insight", "Torneo", "Life", "Domani",
                      "Nsx", "Beat", "Logo", "S2000"],
            "Isuzu": ["Coaster", "Bighorn", "ISUZU", "Gemini", "Bus", "Elf", "Forward", "Giga", "Como", "Fargo",
                      "Journey", "Wizard"],
            "Subaru": ["R2", "Lucra", "Outback", "Trezia", "Wrx", "Stella", "Forester", "Alcyone", "Pleo", "Sambar",
                       "Exiga", "Levorg", "Dias", "Impreza", "Xv", "Dex", "Brz", "Leone", "R1", "Chiffon", "Vivio",
                       "Legacy"],
            "Suzuki": ["Splash", "Every", "Twin", "Cervo", "Super", "Baleno", "Cruze", "Landy", "Palette", "Mr",
                       "Carry", "Mrwagon", "Jimny", "Aerio", "Ignis", "Solio", "Kei", "Mw", "Cappuccino", "Spacia",
                       "Swift", "Lapin", "Sx4", "Alto", "Wagon", "Hustler", "Xbee", "Escudo"],
            "Toyota": ["Starlet", "Prius", "Gr", "Fj", "Granace", "Premio", "Avensis", "Wish", "Allex", "Brevis",
                       "Townace", "Corona", "Markx", "Vellfire", "Bb", "Succeed", "Celica", "Celsior", "Kluger", "S",
                       "Sprinter", "Grand", "Isis", "Rush", "Vitz", "Porte", "Ractis", "Toyoace", "Alphard", "Gaya",
                       "Camroad", "Platz", "Yaris", "Town", "Caldina", "Sequoia", "Copen", "Roomy", "Lite", "Special",
                       "Soarer", "Raize", "Ipsum", "Mirai", "Aristo", "Hilux", "TOYOTA", "Noah", "Tank", "Battery",
                       "Raum", "Voxy", "Esquire", "Estima", "Granvia", "Corolla", "Century", "Sai", "Forklift", "Mr-s",
                       "Pixis", "Probox", "Cresta", "Sparky", "Mr2", "Quick", "Shovel", "Fun", "Verossa", "Cami",
                       "Rav4", "Opa", "Chaser", "Sienta", "Cynos", "Crown", "Blade", "Ist", "Aqua", "Tundra", "Supra",
                       "Belta", "86", "Progres", "Hiace", "Allion", "Will", "Li-chi", "Dyna", "Windom", "Carina",
                       "Coaster", "Spade", "Mark", "Vanguard", "Tercel", "Regius", "Passo", "Auris", "Land", "Altezza",
                       "Iq", "Camry", "Vista", "Harrier", "C-hr", "Coms", "Tacoma"]}

IS_CATEGORY_SET = False
CATEGORY_TYPE = ''


def getCategory_Type():
    return CATEGORY_TYPE


def setCategory_Type(tmp):
    global CATEGORY_TYPE
    CATEGORY_TYPE = tmp


def plotingdata():
    ax.clear()
    USER_REQUEST_TEXT_BOX = text_box_1.get(1.0, "end-1c")
    x_usr_req, y_usr_req = '', ''
    if USER_REQUEST_TEXT_BOX == 'All':
        x_usr_req, y_usr_req = usr.get_final_x_y_fromWholeData(carsJson)
    else:
        try:
            x_usr_req, y_usr_req = usr.getDatForUserMakeReqPreReadyToGraph(USER_REQUEST_TEXT_BOX)
        except:
            print('something went wrong')

    # ax.bar(range(len(x_usr_req)), y_usr_req)
    # ax.xticks(range(len(x_usr_req)), x_usr_req, rotation='vertical')
    ax.bar(x_usr_req, y_usr_req)
    # ax.bar(x, y)
    ax.set_xticklabels(x_usr_req, rotation=70)
    print(x_usr_req, y_usr_req)
    canvas.draw()


def plotingdata_func2():
    if IS_CATEGORY_SET:
        ax.clear()
        USER_REQUEST_TEXT_BOX_MAKE = textbox_func2_make.get(1.0, "end-1c")
        USER_REQUEST_TEXT_BOX_MODEL = textbox_func2_model.get(1.0, "end-1c")
        x1_usr_req, y1_usr_req = '', ''
        try:
            dfBasedOnUserReq = usr.setting_cat_by_usrReq(USER_REQUEST_TEXT_BOX_MAKE, USER_REQUEST_TEXT_BOX_MODEL,
                                                         CATEGORY_TYPE)
            x1_usr_req, y1_usr_req, y2_usr_req = usr.category_count(dfBasedOnUserReq)
            get_deep_info_dataFrame(dfBasedOnUserReq, USER_REQUEST_TEXT_BOX_MAKE, USER_REQUEST_TEXT_BOX_MODEL)
        except:
            print('something went wrong')
        ax.bar(x1_usr_req, y1_usr_req)
        canvas.draw()

    else:
        messagebox.showerror("Error", "Set a category first")


def plotingdata_func3():
    if IS_CATEGORY_SET:
        ax.clear()
        USER_REQUEST_TEXT_BOX_MAKE = textbox_func2_make.get(1.0, "end-1c")
        USER_REQUEST_TEXT_BOX_MODEL = textbox_func2_model.get(1.0, "end-1c")
        x1_usr_req, y2_usr_req = '', ''
        try:
            dfBasedOnUserReq = usr.setting_cat_by_usrReq(USER_REQUEST_TEXT_BOX_MAKE, USER_REQUEST_TEXT_BOX_MODEL,
                                                         CATEGORY_TYPE)
            x1_usr_req, y1_usr_req, y2_usr_req = usr.category_count(dfBasedOnUserReq)
            get_deep_info_dataFrame(dfBasedOnUserReq, USER_REQUEST_TEXT_BOX_MAKE, USER_REQUEST_TEXT_BOX_MODEL)
        except:
            print('something went wrong')
        ax.bar(x1_usr_req, y2_usr_req)
        canvas.draw()
    else:
        messagebox.showerror("Error", "Set a category first")


def set_category():
    setCategory_Type(textbox_cat.get(1.0, "end-1c"))
    global IS_CATEGORY_SET
    IS_CATEGORY_SET = True
    messagebox.showinfo("showinfo", "Category is been updated")


def get_deep_info_dataFrame(df, make, model):
    sub_data_table = tk.Toplevel()
    sub_data_table.title(f"{make} - {model}")
    sub_data_table.geometry("600x200")
    tv = ttk.Treeview(sub_data_table)
    tv.place(relwidth=1, relheight=1)
    treescrolly = tk.Scrollbar(sub_data_table, orient="vertical", command=tv.yview)
    treescrollx = tk.Scrollbar(sub_data_table, orient="horizontal", command=tv.xview)
    tv.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
    treescrollx.pack(side="bottom", fill="x")
    treescrolly.pack(side="right", fill="y")
    tv["column"] = list(df.columns)
    tv["show"] = "headings"
    for column in tv["columns"]:
        tv.heading(column, text=column)
    d_rows = df.to_numpy().tolist()
    for row in d_rows:
        tv.insert("", "end", values=row)


root = tk.Tk()
root.geometry('1080x720')
fig, ax = plt.subplots(figsize=(20, 10))

frameGraph = tk.Frame(root)
frameUser = tk.Frame(root)
# framefunc1 = tk.Frame(frameUser)

# Graph frame elements
canvas = FigureCanvasTkAgg(fig, master=frameGraph)

# Graphing all elements into GraphFrame
canvas.get_tk_widget().pack()

# User Frame Elements

# First func
label = tk.Label(frameUser, text="Functions")
label_func1 = tk.Label(frameUser, text="Enter \'All\' or name of the make")
btn = tk.Button(frameUser, text="Graph", command=plotingdata)
text_box_1 = tk.Text(frameUser, height=1.4, width=20)
label_donation = tk.Label(frameUser, text="Please donate to our project NOW or we will block ur PC", fg="red")
label_donation1 = tk.Label(frameUser, text="Zelle: +14242495650", fg="red")
label_donation2 = tk.Label(frameUser, text="Zelle: +12179333015", fg="red")

# Setting category
btn_set_cat = tk.Button(frameUser, text='Category', command=set_category)
textbox_cat = tk.Text(frameUser, height=1.4, width=10)
label_cat = tk.Label(frameUser, text="Type of category - ")

# count by category in user requested model
# avarge price by category in user requested model
label_func2 = tk.Label(frameUser, text="Enter make and model")
textbox_func2_make = tk.Text(frameUser, height=1.4, width=10)
textbox_func2_model = tk.Text(frameUser, height=1.4, width=10)
btn_func2 = tk.Button(frameUser, text="Count", command=plotingdata_func2)
btn_func3 = tk.Button(frameUser, text="Average Price", command=plotingdata_func3)
label_make = tk.Label(frameUser, text="Make - ")
label_model = tk.Label(frameUser, text="Model - ")

# Graphing all elements into UserFrame
n = 0.2

# Func 1
label.place(relx=0.4, rely=0.03)
label_func1.place(relx=0.02, rely=0.1)
text_box_1.place(relx=0.02, rely=0.13)
btn.place(relx=0.02, rely=0.16)

# Func 2 beg
label_func2.place(relx=0.3, rely=0.25)
label_make.place(relx=0.02, rely=0.3)
textbox_func2_make.place(relx=0.25, rely=0.3)
label_model.place(relx=0.02, rely=0.33)

# Categories
textbox_func2_model.place(relx=0.25, rely=0.33)
textbox_cat.place(relx=0.4, rely=0.37)
label_cat.place(relx=0.02, rely=0.37)
btn_set_cat.place(relx=0.02, rely=0.4)

#  Func 2 ends
btn_func2.place(relx=0.02, rely=0.36 + n)
btn_func3.place(relx=0.02, rely=0.4 + n)

label_donation.place(rely=0.7)
label_donation1.place(rely=0.8)
label_donation2.place(rely=0.9)

# Graphing all frames
frameGraph.place(relx=0.3, relwidth=0.7, relheight=1)
frameUser.place(relwidth=0.3, relheight=1)
root.mainloop()

# window = tk.Tk()
# window.title('Test Test Test')
#
# window.mainloop()
