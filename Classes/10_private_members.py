class TagCloud:
    def __init__(self):
        self.__tags = {}  # made it private with "__"

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):  # can return values
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):  # can modify values
        self.__tags[tag.lower()] = count

    def __len__(self):  # can get the lenght of tags
        return len(self.__tags)

    def __iter__(self):  # makes it iterable
        iter(self.__tags)


cloud = TagCloud()
print(cloud.__dict__)  # __dict__ holds all attributes
print(cloud._TagCloud__tags)
