import simplejson as json
import os

if os.path.isfile("./example.json") and os.stat("./example.json").st_size != 0:
    existed_file = open("./example.json", "r+")
    data = json.loads(existed_file.read())
    data["point"] = data["point"] + 1
    print("point is", data["point"])
else:
    existed_file = open("./example.json", "w+")
    data = {"style": "heart", "point": 2}
    print("point is ", data["point"])

existed_file.seek(0)
existed_file.write(json.dumps(data))

