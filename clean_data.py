import os
import json
import codecs

dir = 'facebook-leloykun/messages/inbox/'
child_dir = next(os.walk(dir))[1]
# print(child_dir)

my_name = "Franz Louis Cesista"

for convo_dir in child_dir:
    message_path = os.path.join(dir, convo_dir, 'message.json')
    if not os.path.isfile(message_path):
        continue
    message_json = open(message_path).read()
    raw_data = json.loads(message_json)

    participants = [name["name"] for name in raw_data["participants"]]
    messages = raw_data["messages"]

    print(".", end='')

    if len(messages) >= 5:
        for message in messages:
            if not message.get("content"):
                continue
            if message["sender_name"] == my_name:
                with codecs.open('me.txt', 'a', 'utf-8') as f:
                    content = '[end]'.join(message["content"].split("\n"))
                    f.write(content + '\n')
            else:
                with codecs.open('notme.txt', 'a', 'utf-8') as f:
                    content = '-[endline]-'.join(message["content"].split("\n"))
                    f.write(content + '\n')

print('')
