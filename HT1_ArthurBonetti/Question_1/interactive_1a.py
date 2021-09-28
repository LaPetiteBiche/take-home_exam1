print("-----METERS TO YARDS CONVERTER-----")
print("")
try:
    meters = float(input('Write a distance in meters, for example "4.73" --> '))
    yards = 1.09361 * meters
    print(f'{meters} meters = {round(yards,5)} yards')
except ValueError:
    print("Hey, that wasn't a number !")
except:
    print("Something went wrong, please try again")