def histrogramCharacters():

    #open file in read mode
    file = open("content.txt", "r")

    #read the content of file
    data = file.read()
    data = data.lower()
    print("The text read is:"+data)
    
    Dict=dict()

    for word in data:

        if word not in Dict:

            Dict[word]=1

        else:

            Dict[word]=Dict[word]+1

    print(Dict)

    for key, val in Dict.items():

        print(key, '\t', '*' *val)
        
histrogramCharacters()