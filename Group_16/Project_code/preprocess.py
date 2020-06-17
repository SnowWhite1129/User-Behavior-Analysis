import xmltodict
import json
import os


def processTFIDF():
    data = []
    with open('train.tfidf') as fd:
        lines = fd.readlines()
        person = {}
        for line in lines:
            if 'Person' in line :
                data.append(person)
                person = {}
            else:
                weight = line.split()
                person[weight[0]] = float(weight[1])
    return data

def processJSON(path, name):
    filename = path + "/" + name +".json" 
    data = ""
    with open(filename) as fd:
        test = path + '/' + 'test'
        os.system('cat "' + filename + '" | grep \\\"dns.qry.name\\\" > "' + test + '"')
        with open(test) as result:
            lines = result.readlines()
            if not lines:
                return data
            for line in lines:
                tmp = line.strip().strip(',')
                tmp = tmp.replace('"', '').replace('dns.qry.name:','').replace(' ','')
                if 'arpa' not in tmp:
                    domain = tmp.split('.')
                    if len(domain) >= 2:
                        domain = domain[-2] + '.' + domain[-1]
                        tmp = domain
                else:
                    domain = tmp.split('.')
                    domain = domain[0] + '.' + domain[1]
                    tmp = domain
                data += tmp + ' '
    return data


def processXML(path, name):
    data = None
    try:
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
                pass
    except:
        pass
    return data


if __name__ == '__main__':
#    processJSON("./Example Test/Test_1", 'Wireshark')
    print(processTFIDF())
