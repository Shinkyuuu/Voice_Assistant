from notion.client import NotionClient
from notion.block import TodoBlock

#~~~~~~~~~~~~~~~~Global Variables~~~~~~~~~~~~~~~~#
dayIDs = {
    'sunday' : '3b52a38d-b717-45cf-a21e-a100f5a68822',
    'monday' : '21682141-e368-45d2-8ea7-606b82dddb3e',
    'tuesday' : '1bae7f39-bcbe-4bca-8dde-c0e0007098f7',
    'wednesday' : '374b27c9-d405-4d62-bc20-fe7e4b71afb7',
    'thursday' : '7e8d1973-3ffa-44f7-813d-937065a758b7',
    'friday' : 'cd2f595f-763b-4e52-9934-9268a74af31b',
    'saturday' : '2ee471d2-ed90-4aed-a740-1c24d6f94811'
}

classes = {
    '303' : 'CS 303',
    '225' : 'EC 225',
    '345' : 'MA 345',
    '250' : 'PS 250',
    '253' : 'PS 253',
    '300' : 'SE 300'
}

#~~~~~~~~~~~~~~~~Initialize Notion~~~~~~~~~~~~~~~~#
tokenPC='f443acf3104fc3090475db915c2b3d2a5ba7c19ae7985677cb29920aa077beb7b9e63b3785d17dc2f89ebf67cfee1ad1e0a5dc1ae632a12a5cd608f7439db945724eb7831c10e54cc92d053b5584'
tokenLaptop='afd1cbcdaf3e3e448d978792e4d46f1f7bab281e70d653aef669eb6aa0c87186bb979acf0320cfce3a062f8871cca0fb17c11e96972818a6a3b00e5953b33d9bf4aca7d40ab4e37a7eb75fda1035'
notionClient = NotionClient(token_v2=tokenPC)
notionUrl = 'https://www.notion.so/Homework-89cc88c788254843bda8217cd56458e5'
page = notionClient.get_block(notionUrl)


#~~~~~~~~~~~~~~Notion Task Functions~~~~~~~~~~~~~~#
def formatClassName(oldTask):
    oldTask = oldTask.title()
    newTask = oldTask.split("Add")
    formattedTask = newTask[1]

    if "To" in formattedTask:
        formattedTask = formattedTask.split("To")
        formattedTask = formattedTask[0]

    for key, value in classes.items():
        if key in formattedTask:   
            index = formattedTask.index(key) + 3
            formattedTask = value + formattedTask[index:]
            break

    return formattedTask


def addToNotion(voice_data):
    block = page
    day = "New"

    for key, value in dayIDs.items():
        if key in voice_data:
            day = key.title()
            block = notionClient.get_block(value)

    taskTitle = formatClassName(voice_data)
    newTask = page.children.add_new(TodoBlock, title=taskTitle)

    if day == "Sunday":
        newTask.move_to(block, "after")
    else:    
        newTask.move_to(block, "last-child")

    return str("Added {} to {}".format(taskTitle, day))
   

#~~~~~~~~~~~~~~~~Notion Meta~~~~~~~~~~~~~~~~#
def printNotionData():
    for child in page.children:
        try:
            print("Child:", child.title, "\n", child.id)
        except:
            print("Child:", child.id)
            for baby in child.children:
                try:
                    print("Baby:", baby.title)
                except:
                    print("Baby:", baby.id)
                    for fetus in baby.children:
                        try:
                            print("Fetus:", fetus.title, "\n", fetus.id)
                        except:
                            print("Fetus:", fetus.id)
                            
