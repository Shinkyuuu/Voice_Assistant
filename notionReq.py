from notion.client import NotionClient
from notion.block import TodoBlock

#~~~~~~~~~~~~~~~~Global Variables~~~~~~~~~~~~~~~~#
dayIDs = {
    'sunday' : '3b52a38d-b717-45cf-a21e-a100f5a68822',
    'monday' : '693553cb-19be-4a2e-9a75-45a4dec4ff38',
    'tuesday' : '10eb90c4-c1ad-4779-b115-b22809c8fdd1',
    'wednesday' : 'c031801a-9653-49ec-a470-5e64048df3a7',
    'thursday' : '0490faca-70e5-4b57-a2a7-1888bcd50fd6',
    'friday' : '4cf5d4c8-3021-4605-a670-627c6a1563d8',
    'saturday' : 'ad08c41d-ef93-487b-989a-f6293a8608c6'
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
    newTask = oldTask.split("create")
    newTask = newTask[1].split("on")
    newTask = newTask[0].title()

    for key, value in classes.items():
        if key in newTask:   
            index = newTask.index(key) + 3
            formattedTask = value + newTask[index:]
            return formattedTask
    

def addToNotion(voice_data):
    for key, value in dayIDs.items():
        if key in voice_data:
            block = notionClient.get_block(value)

    taskTitle = formatClassName(voice_data)
    newTask = page.children.add_new(TodoBlock, title=taskTitle)

    newTask.move_to(block, "after")


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
                            
