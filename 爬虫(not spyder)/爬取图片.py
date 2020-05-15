import requests
import os
root = "D://照片//"
url = "https://img.ltn.com.tw/Upload/ent/page/800/2019/07/03/phpxoCKEz.jpg"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("Successful!")
    else:
        print("Already exist!")
except:
    print("Failed!")
