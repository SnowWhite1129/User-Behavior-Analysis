import preprocess
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def predict(train, test):
    n = 0
    index = 0
    for i in range(len(train)):
        similarity = cosine_similarity(train[i], test)
        if similarity > n:
            n = similarity
            index = i
    return index


def trainDNS(name):
    query = []
    for i in range(1, 7):
        query.append(preprocess.processJSON('./Train/Person_' + str(i), name))
    vectorizer = TfidfVectorizer()
    DNS = vectorizer.fit_transform(query).toarray()
    print(vectorizer.get_feature_names())
    return DNS


def trainID(name):
    processID = []
    for i in range(1, 7):
        processID.append(preprocess.processXML('./Train/Person_' + str(i), name))
    return processID


if __name__ == '__main__':
    print(trainDNS('Wireshark'))
    '''
    print(trainID('Sysmon'))
    print(trainID('Security'))
    '''

