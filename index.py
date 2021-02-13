import pypresence
from time import sleep
import json

presence = pypresence.Presence('809886974503551056')

presetPath="/home/molten/Documents/Presets"
presetData = {
        
}

def save(preset):
    large_image = input("Large image name >>> ")
    large_text = input("Image tooltip >>> ")
    small_image = input("Small image name >>> ")
    small_text = input("Small image tooltip >>> ")
    details = input("First line >>> ")
    state = input("Second line >>> ")
    presetData = {
            "large_image": large_image,
            "large_text": large_text,
            "small_image": small_image,
            "small_text": small_text,
            "state": state,
            "details": details
            }

    f = open(presetPath + "/" + preset + ".json", 'w+')
    json.dump(presetData, f)
    f.close()

def load(preset):
    f = open(presetPath + "/" + preset + ".json", 'r')
    presetData = json.loads(f.read())
    f.close()
    presence.connect()
    presence.update(large_image=presetData.get("large_image"), large_text=presetData.get("large_text"), small_image=presetData.get("small_image"), small_text=presetData.get("small_text"), state=presetData.get("state"), details=presetData.get("details"))

while True:
    print("Welcome to the Molten's presence shop, what do you want to do")
    print("1 - create a new preset")
    print("2 - load a preset")
    print("3 - exit the program")
    
    selected = int(input(">>> "))

    if selected == 1:
        save(input("Enter the name of the preset >>> "))    
    if selected == 2:
        load(input("Enter the name of the preset >>> "))    
    if selected == 3:
        presence.close()
        exit() 
        
presence.close()
exit()
