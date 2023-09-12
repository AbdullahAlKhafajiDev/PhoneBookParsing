def phoneBookify(namesAndNumbers):
    phoneBook = {}
    nameAndNumber = []
    
    for entry in namesAndNumbers:
        nameAndNumber = entry.split(' ')
        
        name = nameAndNumber[0]
        number = nameAndNumber[1]
        
        phoneBook[name] = number
        
    return phoneBook
    
def parseQueries(parsedArray, numberOfEntries):
    queries = []
    
    for i in range(int(numberOfEntries) + 1, len(parsedArray)):
        queries.append(parsedArray[i])
        
    return queries
    
def parseString(string):
    parsedArray = string.split('\n')
    numberOfEntries = parsedArray[0]
    namesAndNumbers = []
    
    #parse the numbers and names and put into array.
    
    for i in range(1, int(numberOfEntries) + 1):
        namesAndNumbers.append(parsedArray[i])
    
    phoneBook = phoneBookify(namesAndNumbers)
    
    queries = parseQueries(parsedArray, numberOfEntries)
    
    return numberOfEntries, phoneBook, queries
    
def checkPhoneNumber(phoneBook, queries):
    for query in queries:
        if query in phoneBook:
            print(query + '=' + phoneBook[query])
        else:
            print('Not found')
    
def main():
    STDIN = '''3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry'''
    numberOfEntries, phoneBook, queries = parseString(STDIN)
    
    checkPhoneNumber(phoneBook, queries)
    
    
    
main()
