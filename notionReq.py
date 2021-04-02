from notion.client import NotionClient
from notion.block import TodoBlock


#~~~~~~~~~~~~~~~~Initialize Notion~~~~~~~~~~~~~~~~#
tokenv2='f443acf3104fc3090475db915c2b3d2a5ba7c19ae7985677cb29920aa077beb7b9e63b3785d17dc2f89ebf67cfee1ad1e0a5dc1ae632a12a5cd608f7439db945724eb7831c10e54cc92d053b5584'
notionClient = NotionClient(token_v2=tokenv2)
notionUrl = 'https://www.notion.so/Homework-89cc88c788254843bda8217cd56458e5'
page = notionClient.get_block(notionUrl)


#~~~~~~~~~~~~~~Notion Task Functions~~~~~~~~~~~~~~#
def addToNotion(voice_data):
    cut_data = voice_data.split("add")
    cut_data = cut_data[1].split("to")
    newTask = page.children.add_new(TodoBlock, title=cut_data[0])

    if "sunday" in voice_data:
        block = notionClient.get_block('580c8cf6-3e31-41e6-8e8f-ae572ab5020d')
    elif "monday" in voice_data:
        block = notionClient.get_block('693553cb-19be-4a2e-9a75-45a4dec4ff38')
    elif "tuesday" in voice_data:
        block = notionClient.get_block('10eb90c4-c1ad-4779-b115-b22809c8fdd1')
    elif "wednesday" in voice_data:
        block = notionClient.get_block('c031801a-9653-49ec-a470-5e64048df3a7')
    elif "thursday" in voice_data:
            block = notionClient.get_block('0490faca-70e5-4b57-a2a7-1888bcd50fd6')
    elif "friday" in voice_data:
        block = notionClient.get_block('4cf5d4c8-3021-4605-a670-627c6a1563d8')
    elif "saturday" in voice_data:
            block = notionClient.get_block('058defef-b6ba-49ba-bc59-9871962bd97e')

    newTask.move_to(block, "after")


#~~~~~~~~~~~~~~~~Notion Meta~~~~~~~~~~~~~~~~#
def printNotionData():
    for child in page.children:
        try:
            print("Child:", child.title)
        except:
            print("Child:", child.id)
            for baby in child.children:
                try:
                    print("Baby:", baby.title)
                except:
                    print("Baby:", baby.id)
                    for fetus in baby.children:
                        try:
                            print("Fetus:", fetus.title)
                        except:
                            print("Fetus:", fetus.id)
                            
