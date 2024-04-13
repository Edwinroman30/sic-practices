''' 
    nyc_weather.csv contains new york city weather for first few days in the month of January.Write a program that can answer following,
    What was the average temperature in first week of Jan
    What was the maximum temperature in first 10 days of Jan
    Figure out data structure that is best for this problem
'''
def load_file():
    file_path = "./data/nyc_weather.csv"
    data : list = []
    #ETL 
    
    #EXTRACT
    with open(file_path, "r") as file:
        for value in file.readlines():
            try:
                resul = value.split(",")
                data.append(float(resul[1]))
            except:
                print("Value cannot be process...")
    #Transform
    #data = list( map(lambda x: (x[0], float(x[1].replace(",","."))), data) ) #Replacing the "," by "." and converting from str to float.
    return data #Load
    
def average_temperature():
    ''' What was the average temperature in first week of Jan '''
    avg = 0.0
    data = load_file()
    
    for x in range(8):
        avg += data[x]
    
    avg = sum( data[:7] )
    print("Sum: ",avg ," and average: ",avg/7 )

def maximum_temp(data: list = []):
    # What was the maximum temperature in first 10 days of Jan
    data = load_file()
    print("The max temp: ", max(data) )
    
average_temperature()
maximum_temp()

''' 
nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
    What was the temperature on Jan 9?
    What was the temperature on Jan 4?
Figure out data structure that is best for this problem '''
from datastructures.HashTable import HashTablev1

def load() -> HashTablev1:
    file_path = "./data/nyc_weather.csv"
    nyc_temp = HashTablev1(11)
    
    try:
        with open(file_path, "r") as file:
            is_firts = True
            
            for data in file.readlines():
                if is_firts:
                    is_firts = False
                    continue
                
                value = data.split(",")
                nyc_temp[value[0]] = value[1]   
    except:
        print("Something went wrong...")
        
    return nyc_temp

#loadedData = load()
##What was the temperature on Jan 9?
#print("What was the temperature on Jan 9? ", loadedData["Jan 9"])
#What was the temperature on Jan 4?
#print("What was the temperature on Jan 4? ", loadedData["Jan 4"])

def poem():
    ''' 
    poem.txt Contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in python and print every 
    word and its count as show below. Think about the best data structure that you can use to solve this problem and figure out 
    why you selected that specific data structure.
    Hint:
        'diverged': 2,
        'in': 3,
        'I': 8
    '''
    path = "./data/poem.txt"
    list_words = []
    words_dict = {}
    
    with open(path, "r") as file:
        try:
            for val in file.readlines():
                list_words.extend( val.split() )
        except:
            print("Line cannot be process...")
            
    # Dropping out the repeated ones....
    list_repeated_words = list_words
    list_words = list( set(list_words) )
    
    for word in list_words:
        words_dict.setdefault(word, list_repeated_words.count(word))
    
    print(words_dict)
    
#poem()