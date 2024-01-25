import csv
from seleniumwire import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

def linkGrabber(htmlSegment):
    splitSegment = htmlSegment.split('"')
    return ("https://www.facebook.com" + splitSegment[3])


def url_modifier(make, model, daysSinceListed, city):
    titles = {'make': make, 'model': model, 'year': '1998'}
    a_string = str(titles['model'])
    matches = [" ", "  "]

    if any([x in a_string for x in matches]):
        model_mod = str(titles['model']).split()
        facebookMarketUrl1 = f'https://www.facebook.com/marketplace/{city}/search?availability=out%20of%20stock'
        facebookMarketUrl2 = '&' + 'minPrice=1000&maxPrice=55000' + '&' + f'daysSinceListed={daysSinceListed}' + '&'
        facebookMarketUrl3 = 'query=' + str(titles['make']) + '%20' + model_mod[0] + '%20' + model_mod[1] + '%20'\
                             + str(titles['year'])
        facebookMarketUrl4 = '&' + 'exact=' + 'false'
    else:
        # url = 'https://www.facebook.com/marketplace/category/search?availability=out%20of%20stock&query=tesla%20model%203&exact=false'
        facebookMarketUrl1 = f'https://www.facebook.com/marketplace/{city}/search?availability=out%20of%20stock'
        facebookMarketUrl2 = '&' + 'minPrice=1000&maxPrice=55000' + '&' + f'daysSinceListed={daysSinceListed}' + '&'
        facebookMarketUrl3 = 'query=' + str(titles['make']) + '%20' + str(titles['model']) + '%20' + str(titles['year'])
        facebookMarketUrl4 = '&' + 'exact=' + 'false'

    fb_url = facebookMarketUrl1 + facebookMarketUrl2 + facebookMarketUrl3 + facebookMarketUrl4

    return fb_url


def facebookScraper(make, model, daysListed, location):
    print('begin')
    candidates = []
    containerSplit = []
    tempLinkHolder = []
    package = []

    PATH = 'C:\\Users\\ilyanus\\.wdm\\drivers\\chromedriver\\win32\\114.0.5735.90\\chromedriver.exe'

    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server=185.130.105.112:10007')

    driver = uc.Chrome(
        options=options,
        headless=True,
    )

    driver.get(url_modifier(make, model, daysListed, location))
    # url = "https://2ip.ru"
    # driver.get(url)

    time.sleep(3)

    email = 'molokic228@hotmail.com'
    password = 'Facebook_huy228'


    if EC.visibility_of_element_located((By.XPATH, "//button[contains(@type, 'submit')]")) == True:
        driver.find_element(By.XPATH, "//input[contains(@aria-label, 'Email')]").send_keys(email)
        driver.find_element(By.XPATH, "//input[contains(@aria-label, 'Password')]").send_keys(password)
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[contains(@type, 'submit')]").click()
        time.sleep(10)
        driver.get(url_modifier(make, model, daysListed, location))
    else:
        pass

    # if EC.visibility_of_element_located((By.XPATH, "//input[contains(@aria-label, 'Enter ZIP Code')]")):
    #     driver.find_element(By.XPATH, "//input[contains(@aria-label, 'Enter ZIP Code')]").send_keys(zipcode)
    #     WebDriverWait(driver, 20).until(
    #         EC.visibility_of_element_located((By.XPATH, "//ul[contains(@aria-label, '1 suggested search')]")))
    #     driver.find_element(By.XPATH, "//ul[contains(@aria-label, '1 suggested search')]").click()
    #
    #     time.sleep(2)
    #     driver.find_element(By.XPATH, "//div[contains(@aria-label, 'Shop local')]").click()
    # else:
    #     pass

    time.sleep(1)

    # for i in range(int(scrollDownLength)):
    #     driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #     time.sleep(1)
    # while EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div[3]/div[2]/div[1]/div/span/text()")) == False:
    #     driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    while not (EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div[3]/div[2]/div[1]/div/span/text()"))):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


    containers = driver.find_elements(By.CLASS_NAME, "x3ct3a4")

    for container in containers:
        tempLinkHolder.append(linkGrabber(container.get_attribute("innerHTML")))

    for container in containers:
        # print(container.text)
        candidates.append(container.text)

    i = 0

    def gettingTheFinalTypeDataFrame(data_subset):
        def transform_entry(entry):
            # Split by newline
            split_entry = entry.split('\n')

            # Check for second price value and remove if found
            if "$" in split_entry[2] and "$" in split_entry[3]:
                split_entry.pop(3)

            # Extract year from fourth column
            year = split_entry[3][:4]
            split_entry.insert(3, year)

            return split_entry

        # Apply transformation to the data
        transformed_data = [transform_entry(item) for item in data_subset]

        def further_transform_entry(entry):
            # Removing the first four digits (year) from the 5th column
            entry[4] = entry[4][5:]
            return entry

        # Apply further transformation to the transformed data
        final_transformed_data = [further_transform_entry(item) for item in transformed_data]

        def final_transform_entry(entry):
            # Removing 'miles' and 'K' from the last column
            mileage = entry[-1].replace('miles', '').replace('K', '').replace('M', '').strip()
            # Convert mileage to integer after multiplying by 1000 if 'K' was present
            if 'K' in entry[-1]:
                entry[-1] = int(float(mileage) * 1000)
            elif 'M' in entry[-1]:
                entry[-1] = int(float(mileage) * 1000000)
            else:
                entry[-1] = int(float(mileage))
            entry[2] = int(entry[2].replace('$', '').replace(',', ''))

            return entry

        # Apply final transformation to the data
        final_data = []
        for item in final_transformed_data:
            if len(item) == 6:
                print(item)
            else:
                try:
                    final_data.append(final_transform_entry(item))
                except:
                    print(item)

        final_data_with_category = []
        for subdata in final_data:
            if int(subdata[2]) <= 5000:
                subdata.append('A')
            elif int(subdata[2]) <= 10000:
                subdata.append('B')
            elif int(subdata[2]) <= 15000:
                subdata.append('C')
            elif int(subdata[2]) <= 20000:
                subdata.append('D')
            elif int(subdata[2]) <= 25000:
                subdata.append('E')
            else:
                subdata.append('F')
            final_data_with_category.append(subdata)

        def generateFinalTable(data):
            df = pd.DataFrame(data)
            df = df.drop(columns=1)
            column_names = {
                0: 'Contract',
                2: 'Price',
                3: 'Year',
                4: 'Make&Model',
                5: 'Location',
                6: 'Miles',
                7: 'Category'
            }

            df.rename(columns=column_names, inplace=True)

            # Convert 'Year' and 'Miles' columns to integer
            df['Year'] = df['Year'].astype(int)
            df['Miles'] = df['Miles'].astype(int)

            # for i in df:
            #     if int(i['Year']) > 1999:
            #         i.drop()

            return df

        return generateFinalTable(final_data_with_category)


    split_data = gettingTheFinalTypeDataFrame(candidates)
    time.sleep(5)
    # if EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div[3]/div[2]/div[1]/div/span/text()")):
    driver.close()

    print('end')
    return split_data




# нет ты пидор
# make_request = 'Chevrolet'
# model_request = 'Camaro'
# data_package = facebookScraper(make_request, model_request, 30 )
# print(data_package.tail())
# #
# data_package.to_csv('out148898.csv', index=False)