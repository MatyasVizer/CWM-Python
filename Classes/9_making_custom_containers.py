class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):  # can return values
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):  # can modify values
        self.tags[tag.lower()] = count

    def __len__(self):  # can get the lenght of tags
        return len(self.tags)

    def __iter__(self):  # makes it iterable
        iter(self.tags)


cloud = TagCloud()
cloud["python"] = 10
cloud.add("Python")
cloud.add("python")
cloud.add("python")
cloud.add("computing")

print(cloud.tags)
print(len(cloud.tags))
