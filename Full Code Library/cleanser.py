import pandas as pd
import os
carJsonTMP = {"BMW": ["3", "M6", "7", "5", "X5", "8", "M4", "X4", "X1", "2", "1", "4", "6", "I3", "X2", "M3", "Z4", "X3",
                    "X6", "Mini", "Z3", "X7"], "Mazda": ["Cx-5", "Efini", "Bongo", "Verisa", "Cx-8", "Cx-60", "Rx-8", "Mazda2", "Mazda6", "Az", "Flair",
                      "Spiano", "Demio", "Rx-7", "Scrum", "Cx-30", "Premacy", "Mx-30", "Eunos", "Mpv", "Carol",
                      "Proceed", "Speed", "Mazda3", "Porter", "Cx-3", "Atenza", "Titan", "Roadster", "Capella", "Cx-7",
                      "Familia", "Biante", "Axela"]}
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
# tmp

def inferior_model_cleaner(carsList):
    f = open('Testicle/attempts.txt', 'r+')
    atmptNum = int(f.readline()) - 1
    for i in carsList:
        for j in carsList[i]:
            new_df = pd.DataFrame(columns=['Contract', 'Price', 'Year', 'Make&Model', 'Location', 'Miles', 'Category'])
            try:
                df = pd.read_csv(f'Testicle/out_{i}_{j}_{atmptNum}.csv')
                print(i,j)
                print('<<<<------>>>>')
                for index, row_series in df.iterrows():
                    lst_tmp = row_series['Make&Model'].split()
                    count = False
                    for i_1 in lst_tmp:
                        if str(i_1).lower() == j.lower():
                            count = True
                    print(row_series.tolist())
                    print('< < < < < < < < < - - - - - - - - - - > > > > > > > >')
                    if count:
                        new_df.loc[len(new_df)] = row_series
                        print('yes')
                    else: print('no')
                # new_df = new_df.drop(df.columns[0], axis=1)
                # new_df = new_df.reset_index(drop=True)
                new_df.to_csv(f'Testicle/out_{i}_{j}_{atmptNum + 1}.csv', index=False)
                print(new_df)
                print('\n <<<<------>>>>')
            except:
                pass
    f.seek(0)
    f.write(str(atmptNum+2))
    f.close()


# inferior_model_cleaner(carsJson)


def delete_bugs(carList):
    f = open('Testicle/attempts.txt', 'r+')
    atmptNum = int(f.readline()) - 1
    for i in carList:
        for j in carList[i]:
            try:
                os.remove(f'Testicle/out_{i}_{j}_{atmptNum}.csv')
            except:
                print(i, j, atmptNum)

def deleteCategory(carsList):
    f = open('Testicle/attempts.txt', 'r+')
    atmptNum = int(f.readline()) - 1
    for i in carsList:
        for j in carsList[i]:
            try:
                df = pd.read_csv(f'Testicle/out_{i}_{j}_{atmptNum}.csv')
                new_df = df.drop(columns=['Category'])
                new_df.to_csv(f'Testicle/out_{i}_{j}_{atmptNum + 1}.csv', index=False)
            except:
                pass
    f.seek(0)
    f.write(str(atmptNum + 2))
    f.close()

deleteCategory(carsJson)
# delete_bugs(carsJson)


# testDf = pd.read_csv('Testicle/out_Mazda_Cx-3_1.csv')
# newTestDf = pd.DataFrame(columns=['Contract', 'Price', 'Year', 'Make&Model', 'Location', 'Miles', 'Category'])
# for index, row in testDf.iterrows():
#     # newTestDf = pd.concat(row, ignore_index=True)
#     lst = row['Make&Model'].split()
#     print(lst)
#     newTestDf.loc[len(newTestDf)] = row.tolist()
# print(testDf.head())

# print('/')
# print(newTestDf.head())
#
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#     print(testDf)
#     print(newTestDf)
