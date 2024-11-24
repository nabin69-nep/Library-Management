class Library:
    def __init__(self,title=None,author=None,genre=None,year=None):
        self.title=title
        self.author=author
        self.genre=genre
        self.year=year
        if title and author and genre and year :
            self.addToFile()
    def addToFile(self):
        with open("library.txt","a+") as f:
            f.write(f"Title: {self.title} Author: {self.author} Genre: {self.genre} Year: {self.year}\n") 
            print("Added Succesfully")
    
    def show_books(self):
        with open("library.txt","r") as f:
            details=f.read()
            print("Your Books are:\n",details)



a=int(input("Enter your choice\n 1.Add Books\n 2.View Books\n"))

if(a==1):
    title=input("Enter Title of your Books ")
    author=input("Enter Author of your Books ")
    genre=input("Enter Genre of your Books ")
    year=input("Enter Year of your Books ")
    Library(title,author,genre,year)

elif(a==2):
    data=Library()
    data.show_books()

else:
    print("Invalid Choice")