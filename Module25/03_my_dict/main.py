class MyDict(dict):

    def get(self, key):
        if key not in self:
            return 0


new_dict = MyDict()
new_dict[1] = 1
new_dict[2] = 2

print(new_dict.get(3))

