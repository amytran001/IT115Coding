#Import from json file
import json

data = {
    
    'name': 'John Doe', 
    'age': 30,
    'city': 'New York, NY',
    'interests': ['Golf','Running','Football','Traveling'],
    'is_student': False
}

#Create a file named data.json 
with open('data.json','w') as json_file:
#Dump the files from line 4 thrpugh 11 into the new file
    json.dump(data,json_file,indent=4)
#Print all data in new file and run the code so it shows the test below
print("Data has been written to data2.json")
    


#Open the data.json file 
with open('data.json','r') as json_file:
    
    #Load new data so we are able to add data into it
    loaded_data = json.load(json_file)

#Print text below if everything is working and also print loaded data 
print("Succesfully able to read data.json")
print(loaded_data)


loaded_data['age'] = 34 
loaded_data['interests'].append('History')

#loaded_data['interests'].remove('Put Your String Here')

#Rewrite the changes to the json file. 
with open('data.json','w') as json_file:
    
    json.dump(loaded_data,json_file,indent=4)
    
print("Data has been re-written to data.json")


