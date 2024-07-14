class Artist:
    def __init__(self,name,no_of_awards) -> None:
        self.name=name
        self.no_of_awards=no_of_awards
    def display(self):
        print("Name: {}".format(self.name))
        print("Number of awards: {}".format(self.no_of_awards))

#creating object Taylor of class Artist
Taylor=Artist('Taylor Swift', 324)
print(Taylor.name)
print(Taylor.no_of_awards)