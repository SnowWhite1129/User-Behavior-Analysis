import xmltodict
import json
import os


def processJSON(path, name):
    filename = path + "/" + name +".json" 
    data = ""
    with open(filename) as fd:
        doc = json.load(fd)
        test = path + '/' + 'test'
        os.system('cat "' + filename + '" | grep \\\"dns.qry.name\\\" > "' + test + '"')
        with open(test) as result:
            lines = result.readlines()
            for line in lines:
                tmp = line.strip().strip(',')
                tmp = tmp.replace('"', '').replace('dns.qry.name:','').replace(' ','')
                data += tmp + ' '
    return data


def processXML(path, name):
    with open(path + "/" + name +".xml") as fd:
        try:
            doc = xmltodict.parse(fd.read())
            if name == 'Sysmon':
                for i in range(100000):
                    try:
                        data = doc["Events"]["Event"][i]["System"]["Execution"]['@ProcessID']
                    except:
                        continue
                    if data != None:
                        break
            else:
                for i in range(100000):
                    try:
                        data = doc["Events"]["Event"][i]["System"]["Correlation"]['@ActivityID']
                    except:
                        continue
                    if data != None:
                        break
        except:
            data = None
        return data


if __name__ == '__main__':
    processJSON("./Example Test/Test_1", 'Wireshark')
