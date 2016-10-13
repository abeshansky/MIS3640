def bisect(Word, List):
    Original = List
    while True:
        middle = len(List) / 2
        if Word > List[middle]:
            List = List[middle:]
        elif Word < List[middle]:
            List = List[:middle]
        elif Word == List[middle]:
            return Original.index(myWord)