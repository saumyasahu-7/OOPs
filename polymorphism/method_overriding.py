# Python code to demonstrate polymorphism

#parent class
class Artist:
    def __init__(self,name,no_of_awards) -> None:
        self.name=name
        self.no_of_awards=no_of_awards
    def display(self):
        print("Name: {}".format(self.name))
        print("Number of awards: {}".format(self.name))

# child class
class Singer(Artist):
    def __init__(self, name, label, no_of_awards, no_of_songs):
        self.label = label
        self.no_of_songs = no_of_songs

        # invoking the __init__ of the parent class
        Artist.__init__(self, name, no_of_awards)
    #method overrirding
    def display(self):
        print("Name: {}".format(self.name))
        print("Number of awards: {}".format(self.name))
        print("Music label: {}".format(self.label))
        print("Number of songs: {}".format(self.no_of_songs))


# creation of an object variable or an instance
Taylor = Singer('Taylor Swift','Universal Music Group' , 324, 262)

Taylor.display()
