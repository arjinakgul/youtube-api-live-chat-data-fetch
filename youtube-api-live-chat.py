import pytchat
videoid = "youtube video id"
file_name = "chat.csv"
chat = pytchat.create(video_id=videoid)

while chat.is_alive():
    chatData = chat.get()
    for c in chatData.items:
        print(f"{c.datetime} [{c.author.name}]- {c.message}")
        # write to csv file 
        # column 1: datetime 
        # column 2: author name
        # column 3: message
        open(file_name, "a").write(f"{c.datetime};{c.author.name};{c.message}\n")
print("Chat data finished.")