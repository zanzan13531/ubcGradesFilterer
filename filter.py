# import urllib.request, json 


# with urllib.request.urlopen("https://ubcgrades.com/api/v2/grades/UBCV/2021W") as url:
#     data = json.load(url)
#     print(data)

# https://ubcgrades.com/api/v2/grades/UBCV/2021W

# from urllib.request import Request, urlopen

# import json

# req = Request(
#     url='https://ubcgrades.com/api/v2/grades/UBCV/2021W', 
#     headers={'User-Agent': 'Mozilla/5.0'}
# )
# webpage = urlopen(req).read()

# data = json.load(webpage)
# print(data)


import json

threshold = 90 # threshhold to filter at
graduate = False # filter for non grad courses (500 or higher are grad courses)
writeToFile = True # whether or not to write to file

with open("2021W.json") as f: # paste data downloaded from https://ubcgrades.com/api/v2/grades/UBCV/2021W change last part to reflect the desired section
    data = json.load(f)
    #print(data)

    classes = []

    for course in data: # looks through data
        if (graduate == False) and (int(course["course"]) >= 500): # filter for non grad courses
            continue
        if (course["average"] >= threshold) and (course["section"] != "OVERALL"):
            classes.append(course["subject"] + " " + course["course"] + " " + course["section"] + ": " + "{:.1f}".format(course["average"])) # rounds average to 1 decimal

    print(classes)

    if writeToFile:
        with open('2021W90PlusNonGrad.txt', 'w') as out: #writes to output file (change file name if parameters are changed)
            for c in classes:
                out.write("%s\n" % c)