import math
import time
import random
import os
import yaml

main_data = []

save_directory = "saves/"

# Add this code to the existing script

def load_config():
    config_data = {}
    try:
        with open("config.yml", "r") as config_file:
            config_data = yaml.load(config_file, Loader=yaml.FullLoader)
    except FileNotFoundError:
        print("Config file not found. Using default settings.")

    # Use config_data to set configurations in the script

load_config()

def clear_lists():
    main_data.clear()

def save_data():
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    all_data = []
    for item in main_data:
        all_data.append({'id': item['id'], 'name': item['name'], 'other_info': item['other_info']})

    with open(save_directory + "data.yml", "w") as yaml_file:
        yaml.dump(all_data, yaml_file)

def load_data():
    try:
        with open(save_directory + "data.yml", "r") as yaml_file:
            all_data = yaml.load(yaml_file, Loader=yaml.FullLoader)

        for item in all_data:
            main_data.append(item)

    except FileNotFoundError:
        print("YAML file not found. Starting with empty list.")

def main():
    num = "{:03d}-{:03d}-{:03d}".format(random.randint(0,999), random.randint(0,999), random.randint(0,999))
    name = input("Enter a name to associate with the ID: ")
    other_info = input("Enter additional information: ")
    main_data.append({'id': num, 'name': name, 'other_info': other_info})
    print("\033[34mYour Unique ID Number Is: \033[0m" + num)
    ask()

def ask():
    prompt = input("What would you like to do? (g - generate new ID, l - lookup ID, c - clear lists, s - save to yaml, ls - load from yaml): ")
    if prompt == "g":
        main()
    elif prompt == "l":
        search_input = input("Enter ID or name to lookup: ")
        found = False
        for item in main_data:
            if search_input in item['id'] or search_input in item['name']:
                print("\033[32mRecord found in the list: \033[0m" + "\033[4m" + item['id'] + "\033[0m - \033[4m" + item['name'] + "\033[0m - \033[4m" + item['other_info'] + "\033[0m")
                found = True
                break
        if not found:
            print("\033[31mRecord not found in the list.\033[0m")
    elif prompt == "c":
        clear_lists()
        print("\033[32mLists have been cleared.\033[0m")
    elif prompt == "s":
        save_data()
        print("\033[32mData has been saved to yaml file.\033[0m")
    elif prompt == "ls":
        load_data()
        print("\033[32mData has been loaded from yaml file.\033[0m")

    ask()

load_data()
main()
