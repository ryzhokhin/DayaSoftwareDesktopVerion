import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from statistics import mean

mpl.use('macosx')
# mpl.use('TkAgg')  # or can use 'TkAgg', whatever you have/prefer
# from tester import carsJson
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
carsJson4test = {"Acura": ["Cl"],
                 "Alfa_Romeo": ["Stelvio", "Sportwagon", "159", "Giulietta", "Mito", "Brera", "155", "Spider", "156",
                                "147", "Gt"],
                 "Audi": ["Tt", "Rs3", "S8", "Rs", "Ttcoupe", "A4", "A1", "A5", "A6", "S1", "S4", "80", "S6", "A3",
                          "Q2", "A8", "Q7", "Rs5", "Q5", "Sq5", "Tts", "A7", "Q3", "Sq2", "S5", "S3"],
                 "BMW": ["3", "M6", "7", "5", "X5", "8", "M4", "X4", "X1", "2", "1", "4", "6", "I3", "X2", "M3", "Z4",
                         "X3", "X6", "Mini", "Z3", "X7"], "Bentley": ["BENTLEY", "-", "Continental", "Navy"],
                 "Bmw_Alpina": ["Xd3"], "Cadillac": ["Xt4", "Sts", "Eldorado", "Cade", "Srx", "Concourse"],
                 "Chevrolet": ["Sonic", "Astro", "Blazer", "Camaro", "Cvl"],
                 "Chrysler": ["Ypsilon", "Pt", "Durango", "300c", "Voyager", "300", "Grand", "Ram"],
                 "Citroen": ["Ds4", "Berlingo", "C5", "Grand", "Ds3", "Saxo", "C6", "C4", "C3", "Ds7"],
                 "Dodge": ["Nitro", "Magnum", "Te."],
                 "Daihatsu": ["Wake", "Hijet", "Be", "Storia", "Atrai", "Delta", "Sonica", "Naked", "Max", "Gran",
                              "Coo", "Copen", "Mira", "Opti", "Terios", "Esse", "Midget", "Move", "Boon", "Tanto",
                              "Cast", "Rocky", "Thor", "Taft"], "Ferrari": ["Roma", "F430"],
                 "Fiat": ["500", "New", "Panda", "500x", "Abarth"],
                 "Ford": ["Ecosport", "Focus", "Festiva", "FORD", "Expedition", "Escape", "Fiesta", "Explorer", "Fo",
                          "Mustang", "Lincoln", "Kuga"], "Gmc": ["GMC", "Express", "Chevrolet", "Cadillac", "Yukon"],
                 "Hino": ["Profia", "HINO", "Dutro", "Dutoro", "Ranger", "Blue", "Liesse"], "Hummer": ["H3"],
                 "Infiniti": ["G37", "In", "Fx35"],
                 "Jaguar": ["X", "E-pace", "F-pace", "Xf", "Xk", "F-type", "Xe", "Xj6"],
                 "Jeep": ["Renegade", "Commander", "Compass", "Cherokee", "Wrangler", "Patriot", "Grand"],
                 "Komatsu": ["KOMATSU"], "Lamborghini": ["Murcielago", "Gayarusp4w"], "Lancia": ["Dedra"],
                 "Land_Rover": ["Range", "Defender", "Freelander", "Lr", "Discovery"],
                 "Lexus": ["LX", "CT", "LC", "RC", "HS", "UX", "ES", "NX", "SC", "RX", "GS", "IS", "LS"],
                 "Lincoln": ["Navigation"],
                 "Mazda": ["Cx-5", "Efini", "Bongo", "Verisa", "Cx-8", "Cx-60", "Rx-8", "Mazda2", "Mazda6", "Az",
                           "Flair", "Spiano", "Demio", "Rx-7", "Scrum", "Cx-30", "Premacy", "Mx-30", "Eunos", "Mpv",
                           "Carol", "Proceed", "Speed", "Mazda3", "Porter", "Cx-3", "Atenza", "Titan", "Roadster",
                           "Capella", "Cx-7", "Familia", "Biante", "Axela"],
                 "Mitsubishi": ["Delica", "Fto", "Galant", "Combine", "Toppo", "Jeep", "Airtrek", "Wheel", "Mirage",
                                "Ek", "Town", "Grandis", "Triton", "I", "Legnum", "Chariot", "Bulldozer", "Diamante",
                                "I-miev", "G", "Canter", "Outlander", "Proudia", "Lancer", "Rvr", "Fuso", "Minica",
                                "Pajero", "Dion", "Eclipse", "Colt", "Gto", "Minicab"],
                 "Maserati": ["Levante", "Ghibli", "Quattroporte", "Gran"],
                 "Mercedes-Benz": ["Eqc", "Slc", "E", "Eqb", "Benz", "Gle", "Mb", "C", "Slk", "R", "Sl", "Glb", "Cla",
                                   "Cls", "G", "Cl", "Clk", "V", "Glk", "M", "S", "Amg", "Viano", "A", "Gla", "B",
                                   "Glc", "Gls", "E-class"], "Mg": ["Rv8"], "Mini": ["Yuatsu", "Mini"],
                 "Mitsuoka": ["Galue", "Viewt", "Ryoga"], "Nissan_Diesel_%28ud%29": ["Condor"],
                 "Peugeot": ["3008", "308", "406", "5008", "Rifter", "208", "Rcz", "207", "407", "508", "2008", "307",
                             "1007", "E-208"],
                 "Porsche": ["Macan", "718", "Cayenne", "Boxster", "911", "PORSCHE", "944", "Panamera"],
                 "Renault": ["Megane", "Captur", "Kangoo", "Twingo", "Lutecia"], "Rolls Royce": ["Phantom", "Rolls"],
                 "Nissan": ["Nv100", "Dayz", "X-trail", "Caravan", "Condor", "E-nv200", "Juke", "Laurel", "Sylphy",
                            "Wingroad", "Pulsar", "Infiniti", "Teana", "Fuga", "Figaro", "Gloria", "Homy", "Note",
                            "Nt450", "Rasheen", "Presage", "Atlas", "Stagea", "Cima", "Liberty", "Bluebird", "Micra",
                            "Skyline", "Vanette", "Leopard", "Avenir", "Pino", "Sunny", "Bassara", "Be-1", "Cube",
                            "Gt-r", "Sakura", "Kicks", "Lafesta", "Primera", "Roox", "180sx", "Nv350", "Latio", "Kix",
                            "Elgrand", "Expert", "K", "Tino", "Cefiro", "Datsun", "Safari", "March", "Ud", "Clipper",
                            "President", "Serena", "Fairlady", "Leaf", "Silvia", "Nv150", "Aura", "Terrano", "Moco",
                            "Otti", "Nv200", "Civilian", "S-cargo", "Dualis", "Nt100", "Murano", "Ad", "Tiida",
                            "Cedric"], "Rover": ["Mini"], "Saab": ["9-5x"],
                 "Smart": ["Fortwo", "Fourfour", "Coupe", "K", "Roadster"],
                 "VW": ["European", "T-cross", "Sirocco", "Bus", "New", "Polo", "Beetle", "Golf", "Vanagon", "Type",
                        "Up", "Touareg", "The", "Tiguan", "Arteon", "Lupo", "Up!", "Jetta", "T-roc", "Sharan",
                        "Passat"],
                 "Volvo": ["S60", "V90", "Xc60", "240", "Xc90", "V60", "S40", "960", "S90", "Xc70", "850", "Xc40",
                           "V50", "V70", "V40", "C70"],
                 "Honda": ["Freed", "Acty", "N-wgn", "Cr-v", "Airwave", "Freed+", "Inspire", "Fit", "S660", "Live", "N",
                           "E", "Accord", "Z", "Capa", "Hr-v", "Avancier", "Jade", "Zr-v", "Stream", "Zest", "Today",
                           "Edix", "Thats", "Element", "Vezel", "N-van", "Prelude", "Crossroad", "Shuttle", "Civic",
                           "Legend", "Electrical", "Grace", "Cr-z", "Odyssey", "Elysion", "Lagreat", "Mobilio",
                           "Stepwgn", "Integra", "Saber", "Vamos", "Gyro", "N-one", "Street", "N-box", "Insight",
                           "Torneo", "Life", "Domani", "Nsx", "Beat", "Logo", "S2000"],
                 "Isuzu": ["Coaster", "Bighorn", "ISUZU", "Gemini", "Bus", "Elf", "Forward", "Giga", "Como", "Fargo",
                           "Journey", "Wizard"],
                 "Subaru": ["R2", "Lucra", "Outback", "Trezia", "Wrx", "Stella", "Forester", "Alcyone", "Pleo",
                            "Sambar", "Exiga", "Levorg", "Dias", "Impreza", "Xv", "Dex", "Brz", "Leone", "R1",
                            "Chiffon", "Vivio", "Legacy"],
                 "Suzuki": ["Splash", "Every", "Twin", "Cervo", "Super", "Baleno", "Cruze", "Landy", "Palette", "Mr",
                            "Carry", "Mrwagon", "Jimny", "Aerio", "Ignis", "Solio", "Kei", "Mw", "Cappuccino", "Spacia",
                            "Swift", "Lapin", "Sx4", "Alto", "Wagon", "Hustler", "Xbee", "Escudo"],
                 "Toyota": ["Starlet", "Prius", "Gr", "Fj", "Granace", "Premio", "Avensis", "Wish", "Allex", "Brevis",
                            "Townace", "Corona", "Markx", "Vellfire", "Bb", "Succeed", "Celica", "Celsior", "Kluger",
                            "S", "Sprinter", "Grand", "Isis", "Rush", "Vitz", "Porte", "Ractis", "Toyoace", "Alphard",
                            "Gaya", "Camroad", "Platz", "Yaris", "Town", "Caldina", "Sequoia", "Copen", "Roomy", "Lite",
                            "Special", "Soarer", "Raize", "Ipsum", "Mirai", "Aristo", "Hilux", "TOYOTA", "Noah", "Tank",
                            "Battery", "Raum", "Voxy", "Esquire", "Estima", "Granvia", "Corolla", "Century", "Sai",
                            "Forklift", "Mr-s", "Pixis", "Probox", "Cresta", "Sparky", "Mr2", "Quick", "Shovel", "Fun",
                            "Verossa", "Cami", "Rav4", "Opa", "Chaser", "Sienta", "Cynos", "Crown", "Blade", "Ist",
                            "Aqua", "Tundra", "Supra", "Belta", "86", "Progres", "Hiace", "Allion", "Will", "Li-chi",
                            "Dyna", "Windom", "Carina", "Coaster", "Spade", "Mark", "Vanguard", "Tercel", "Regius",
                            "Passo", "Auris", "Land", "Altezza", "Iq", "Camry", "Vista", "Harrier", "C-hr", "Coms",
                            "Tacoma"]}


class Features():
    cars = {}

    def __init__(self):
        cars = carsJson

    def getDatForUserMakeReqPreReadyToGraph(self, name_of_req_model):
        models_for_request = Features.get_models_for_make(self, [f'{name_of_req_model}'])
        models_ready_for_x = []
        models_ready_for_y = []
        for i in models_for_request[0]:
            # print('Model' + i)
            try:
                counter = Features.getDeepSell(self, Features.final_filter(self, name_of_req_model, i))
                if counter > 0:
                    models_ready_for_x.append(i)
                    models_ready_for_y.append(counter)
            except:
                pass

        return models_ready_for_x, models_ready_for_y

    def get_final_x_y_fromWholeData(self, JsonStructModels):
        newCarsJson = Features.delete_makes_with_zero(self, JsonStructModels,
                                                      Features.graphing_makes(self, JsonStructModels))
        newModelsWithoutZero = list(newCarsJson.keys())
        return Features.getting_graph_for_makes(self, newModelsWithoutZero,
                                                Features.get_models_for_make(self, newModelsWithoutZero))

    # def category_count_old(self, make, model):
    #     f = open('Testicle/attempts.txt', 'r')
    #     atmptNum = int(f.readline()) - 1
    #     f.close()
    #     df = pd.read_csv(f'Testicle/out_{make}_{model}_{atmptNum}.csv')
    #     df = df[df['Year'] <= 1999]
    #     categories = ['A', 'B', 'C', 'D', 'E', 'F']
    #     cat_count = []
    #     price_list = []
    #     final_price_list = []
    #     counter = 0
    #     while len(cat_count) != len(categories):
    #         for i in categories:
    #             df_tmp = df[df['Category'] == i]
    #             cat_count.append(len(df_tmp))
    #
    #             tmp = df_tmp['Price'].tolist()
    #             try:
    #                 meane = mean(tmp)
    #                 mean_rounded = round(meane, 1)
    #                 price_list.append(mean_rounded)
    #             except:
    #                 price_list.append(0)
    #     return categories, cat_count, price_list

    def category_count(self, usrRequestedDfByCat):
        categories = ['A', 'B', 'C', 'D', 'E', 'F']
        cat_count = []
        price_list = []
        final_price_list = []
        counter = 0
        while len(cat_count) != len(categories):
            for i in categories:
                df_tmp = usrRequestedDfByCat[usrRequestedDfByCat['Category'] == i]
                cat_count.append(len(df_tmp))

                tmp = df_tmp['Price'].tolist()
                try:
                    meane = mean(tmp)
                    mean_rounded = round(meane, 1)
                    price_list.append(mean_rounded)
                except:
                    price_list.append(0)
        return categories, cat_count, price_list



    # collects only models below 1999 year made
    # gets model, make, returns df
    def final_filter(self, make, model):
        f = open('Testicle/attempts.txt', 'r')
        # atmptNum = int(f.readline()) - 1
        atmptNum = int(f.readline()) - 1
        f.close()
        df = pd.read_csv(f'Testicle/out_{make}_{model}_{atmptNum}.csv')
        df = df[df['Year'] <= 2025]
        # print(df)
        return df

    # Metric that counts depth sales based on model and make provided by user, for the latest scrap
    def getDeepSell(self, df):
        return df.count()[0]

    def getting_graph_for_makes(self, x, models_y):
        output_y = []
        curr = 0
        for i in x:
            currModelCounter = 0
            for j in models_y[curr]:
                try:
                    currModelCounter += Features.getDeepSell(self, Features.final_filter(self, i, j))
                except:
                    pass
            output_y.append(currModelCounter)
            curr += 1
        return x, output_y

    def graphing_makes(self, data):
        maker_count = []
        for i in data:
            df_counter = 0
            for j in data[i]:
                try:
                    df_counter += Features.getDeepSell(self, Features.final_filter(self, i, j))
                except:
                    pass
            maker_count.append(df_counter)
        return maker_count

    def get_models_for_make(self, x_tmp):
        models = []
        for i in x_tmp:
            models.append(carsJson[i])
        return models

    # print(graphing_makes(carsJson4test))
    #
    def delete_makes_with_zero(self, data, makeCount):
        outputData = {'ZeroItem': 0, 'ZeroItemTwo': 0, }
        counter = 0
        for i in data:
            if makeCount[counter] != 0:
                outputData[i] = data[i]
            counter += 1
        outputData.pop('ZeroItem')
        outputData.pop('ZeroItemTwo')

        return outputData

    # Function for category set1 changer - category by miles
    # gets make, model, returns dataFrame with category column
    def setting_cat_by_usrReq(self, make, model, cat_key):
        df = Features.final_filter(self, make, model)
        df_category = []
        if cat_key == 'Miles':
            for index, row_series in df.iterrows():
                # print(row_series['Miles'])
                if row_series['Miles'] <= 50000:
                    df_category.append('A')
                elif row_series['Miles'] <= 100000:
                    df_category.append('B')
                elif row_series['Miles'] <= 150000:
                    df_category.append('C')
                elif row_series['Miles'] <= 200000:
                    df_category.append('D')
                elif row_series['Miles'] <= 250000:
                    df_category.append('E')
                else:
                    df_category.append('F')
        elif cat_key == 'Price':
            for index, row_series in df.iterrows():
                # print(row_series['Miles'])
                if row_series['Price'] <= 2500:
                    df_category.append('A')
                elif row_series['Price'] <= 5000:
                    df_category.append('B')
                elif row_series['Price'] <= 7500:
                    df_category.append('C')
                elif row_series['Price'] <= 10000:
                    df_category.append('D')
                elif row_series['Price'] <= 15000:
                    df_category.append('E')
                else:
                    df_category.append('F')

        df.insert(6, "Category", df_category, True)
        return df



#creates a new df with user-requesed filter
    def filter_by_usrReq(self, dfIn, search_key):
        filter_search = dfIn['Make&Model'].str.contains(search_key)
        idx_list = filter_search[filter_search].index.tolist()
        filtered_search = dfIn.loc[idx_list]
        return filtered_search


    # x, y= get_final_x_y_fromWholeData(carsJson4test)

    # x_all_models_for_use = ['BMW','Toyota', 'Honda', 'Jeep', 'Cadillac']
    # x_1,y_1 = getting_graph_for_makes(x_all_models_for_use, get_models_for_make(x_all_models_for_use))

    # <<<<<  - - - -- - -- - - -  ->>>>>

    # Takes list of X and list of Y's and graphs the bars
    def graphingData(self, x_req, y_req):
        def addlabels(x_req, y_req):
            for i in range(len(x_req)):
                plt.text(i, y_req[i], y_req[i])

        plt.bar(x_req, y_req)

        # calling the function to add value labels
        addlabels(x_req, y_req)

        # giving title to the plot
        plt.title("Cars and their sales")

        # giving X and Y labels
        plt.xlabel("models")
        plt.ylabel("Number of sales")

        # visualizing the plot
        plt.show()


# tmp = Features()
# print(tmp.filter_by_usrReq('BMW', '3', '328i'))

    #
    # graphingData(x,y)
    # graphingData(x_1,y_1)

    # <<<<<< - - -- - - -- - - -  - -- - - ->>>

    # def userRequest(self, request_usr):
    #     if request_usr == 'All':
    #         x_all_makes, y_all_makes = get_final_x_y_fromWholeData(self, carsJson4test)
    #         graphingData(self, x_all_makes, y_all_makes)
    #     else:
    #         try:
    #             x_usr_req, y_usr_req = getDatForUserMakeReqPreReadyToGraph(request_usr)
    #             graphingData(x_usr_req, y_usr_req)
    #         except:
    #             print('Something went wrong')

# **********************************************
# ****************ILYA's CODE*******************
# **********************************************


# def average_price(make):
#     x_usr_req, y_usr_req = getDatForUserMakeReqPreReadyToGraph(make)
#     for i in x_usr_req:
#         f = open('Testicle/attempts.txt', 'r')
#         atmptNum = int(f.readline()) - 1
#         f.close()
#         model = i
#         df = pd.read_csv(f'Testicle/out_{make}_{model}_{atmptNum}.csv')
#         df = df[df['Year'] <= 1999]
#         prices = []
#         categories = []
#         category_count = []
#         category = df['Category']
#         for j in category:
#                 price = df[j['Price']]
#                 cunt = df[j].count()[0]
#                 prices.append(price)
#                 categories.append(j)
#                 category_count.append(cunt)
#     return prices, categories, category_count
#
#
# print(average_price('Toyota'))


# def category_count(make, model):
#     f = open('Testicle/attempts.txt', 'r')
#     atmptNum = int(f.readline()) - 1
#     f.close()
#     df = pd.read_csv(f'Testicle/out_{make}_{model}_{atmptNum}.csv')
#     df = df[df['Year'] <= 1999]
#     categories = ['A', 'B', 'C', 'D', 'E', 'F']
#     cat_count = []
#     counter = 0
#     while len(cat_count) != len(categories):
#         for i in categories:
#             df_tmp = df[df['Category'] == i]
#             cat_count.append(len(df_tmp))
#             # for j in df:
#             #     if j[5] == i:
#             #         counter +=1
#             # cat_count.append(counter)
#
#     return cat_count, categories


# print(category_count('Toyota', 'Tacoma'))


# usrReq = ''
# while usrReq != 'STOP':
#     usrReq = input('Enter make or All BIG POPPA: ')
#     userRequest(usrReq)

# RADIO BUTTON GRAPH


# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.widgets import RadioButtons
#
# # plotting between the interval -π and π
#
#
# x_all_models_for_use = ['BMW','Toyota', 'Honda', 'Jeep']
# # x,y = getting_graph_for_makes(x_all_models_for_use, get_models_for_make(x_all_models_for_use))
# #
# # p = []
#
# x = x_all_models_for_use
#
# p = [45, 21,43,65]
# q = [34, 54, 23, 54]
# r = [12, 34, 21, 24]
# s = [54, 23, 12, 27]
#
# fig, ax = plt.subplots()
# l, = ax.plot(x, p, lw=3, color='green')
# plt.subplots_adjust(left=0.3)
#
# rax = plt.axes([0.05, 0.7, 0.15, 0.2])
# radio = RadioButtons(rax, x_all_models_for_use)
#
# tmp = {}
#
#
# # function performed on clicking the radio buttons
# def sinefunc(label):
#     sindict = {'BMW': p,
#                'Toyota': q,
#                'Honda': r,
#                'Jeep': s}
#     data = sindict[label]
#     # l.set_ydata(data)
#     plt.draw()
#
#
# radio.on_clicked(sinefunc)
#
# # plot grid
# ax.grid()
# plt.show()
#


# Data
# groups = ['G1', 'G2', 'G3', 'G4', 'G5']
# values1 = [54, 19, 14, 27, 16]
# values2 = [21, 30, 15, 17, 20]
# values3 = [35, 13, 21, 14, 26]
# values4 = [12, 0, 0, 0, 0]
#
# width = 0.25
#
# fig, ax = plt.subplots()
#
# # Stacked bar chart
# ax.bar(groups, values4, width = width, )
# ax.bar(groups, values3, width = width, )
# ax.bar(groups, values2, width = width,)
# ax.bar(groups, values1, width = width)
#
# plt.show()

#
# import numpy as np
#
# # Fixing random state for reproducibility
# np.random.seed(19680801)
#
#
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# x, y = np.random.rand(2, 100) * 4
# hist, xedges, yedges = np.histogram2d(x, y, bins=4, range=[[0, 4], [0, 4]])
#
# # Construct arrays for the anchor positions of the 16 bars.
# xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
# xpos = xpos.ravel()
# ypos = ypos.ravel()
# zpos = 0
#
# # Construct arrays with the dimensions for the 16 bars.
# dx = dy = 0.5 * np.ones_like(zpos)
# dz = hist.ravel()
#
# ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average')
#
# plt.show()
#
# print(dropping_zeroes(graphing_makes(carsJson), carsJson4test))


# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.widgets import RadioButtons
#
#
# t = np.arange(0.0, 2.0, 0.01)
# s0 = np.sin(2*np.pi*t)
# s1 = np.sin(4*np.pi*t)
# s2 = np.sin(8*np.pi*t)
#
# fig, ax = plt.subplots()
# l, = ax.plot(t, s0, lw=2, color='red')
# fig.subplots_adjust(left=0.3)
#
# axcolor = 'lightgoldenrodyellow'
# rax = fig.add_axes([0.05, 0.7, 0.15, 0.15], facecolor=axcolor)
# radio = RadioButtons(rax, ('1 Hz', '2 Hz', '4 Hz'),
#                      label_props={'color': 'cmy', 'fontsize': [12, 14, 16]},
#                      radio_props={'s': [16, 32, 64]})
#
#
# def hzfunc(label):
#     hzdict = {'1 Hz': s0, '2 Hz': s1, '4 Hz': s2}
#     ydata = hzdict[label]
#     l.set_ydata(ydata)
#     fig.canvas.draw()
# radio.on_clicked(hzfunc)
#
# rax = fig.add_axes([0.05, 0.4, 0.15, 0.15], facecolor=axcolor)
# radio2 = RadioButtons(
#     rax, ('red', 'blue', 'green'),
#     label_props={'color': ['red', 'blue', 'green']},
#     radio_props={
#         'facecolor': ['red', 'blue', 'green'],
#         'edgecolor': ['darkred', 'darkblue', 'darkgreen'],
#     })
#
#
# def colorfunc(label):
#     l.set_color(label)
#     fig.canvas.draw()
# radio2.on_clicked(colorfunc)
#
# rax = fig.add_axes([0.05, 0.1, 0.15, 0.15], facecolor=axcolor)
# radio3 = RadioButtons(rax, ('-', '--', '-.', ':'))
#
#
# def stylefunc(label):
#     l.set_linestyle(label)
#     fig.canvas.draw()
# radio3.on_clicked(stylefunc)
#
# plt.show()
