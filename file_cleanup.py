import os

folder_original = 'C:/Users/Superuser/Downloads'
folder_destination = 'C:/Users/Superuser/Downloads/CleanedUp'

os.mkdir(folder_destination)

for entry in os.scandir(folder_original):
    location_original = os.path.join(folder_original, entry.name)
    location_destination = os.path.join(folder_destination, entry.name)

    if os.path.isfile(location_original):
        os.rename(location_original, location_destination) 
        
entries = os.scandir(folder_original)
for entry in entries:
    print(entry.name)
    if os.path.isfile(entry):
        print('File:', entry.name)
        os.rename(entry.path, os.path.join(folder_destination, entry.name))
    elif os.path.isdir(entry):
        print('Directory:', entry.name)
