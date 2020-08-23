import requests
wenjiann='data'
with  open("dalo.sh","r",encoding="utf-8") as f:
    for line in f:
        if "wget" in line and r"${http}" in line:
            line= line.replace(r"${http}","http:/")
            line= line.replace(r"${host}","radius-1253794729.cosgz.myqcloud.com")
            line= line.replace(r"${wenjiann}",wenjiann)
            line= line.replace(r"wget","")
            line = line.strip()
            filename=line.split("/")[-1]
            print(filename)
            with open("data/"+filename,"wb") as b:
                b.write(requests.get(line).content)
            print(line)