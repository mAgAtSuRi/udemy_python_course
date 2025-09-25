#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# to print the current working path:
# import os
# print(os.getcwd())

with open("./Intermediate/Mail Automation/Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
    content = file.read() 

with open("./Intermediate/Mail Automation/Mail Merge Project Start/Input/Names/invited_names.txt") as name_file:
    list_names = name_file.readlines()
    for name in list_names:
        clean_name = name.strip()
        with open(f"{clean_name} invitation letter.txt", 'w') as birthday_letter:
            new_content = content.replace("[name]", f"{clean_name}")
            birthday_letter.write(new_content)
