class Anagram:
    def __init__(self, word):
        self.word = word
    def match(self,listItems):
        similar=[]
        for item in listItems:
            if sorted(self.word.lower()) == sorted(item.lower()) and self.word.lower() != item.lower():
                similar.append(item)
        return similar
