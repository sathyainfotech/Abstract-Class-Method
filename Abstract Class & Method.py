from abc import ABC,abstractmethod

class Library(ABC):

    @abstractmethod
    def add_books(self):
        pass

    @abstractmethod
    def view_books(self):
        pass

    @abstractmethod
    def issue_books(self):
        pass

    @abstractmethod
    def return_books(self):
        pass

    @abstractmethod
    def delete_books(self):
        pass

class College(Library):

    def __init__(self,books):
        self.books=books

    def check(self):
        print("Hi Python")

    def add_books(self):
        if self.books == []:
            count = int(input("\nHow many books would you like to add ? : "))
            print("\nEnter Books Name:")
            for i in range(count):
                bname = input()
                self.books.append(bname)
            print("Your Books is Added")
        else:
            print("\nEnter Books Name:")
            self.books.append(input())
            print("Your Book is Added")

    def view_books(self):
        print("\nList of Books")
        for sno, name in enumerate(self.books, 1):
            print("{}.{}".format(sno, name))

    def issue_books(self):
        ibook = input("\nWhich book you want to issue ? : ")
        if ibook in self.books:
            self.books.remove(ibook)
            print("Book Issued")
        else:
            print("Invalid Book Name..!!!")

    def return_books(self):
        rbook = input("\nWhich book you receive? : ")
        self.books.append(rbook)
        print("Book Received")

    def delete_books(self):
        dbook = input("\nWhich book you want to remove ? : ")
        if dbook in self.books:
            self.books.remove(dbook)
            print("Book Removed")
        else:
            print("Invalid Book Name..!!!")

books=[]
obj=College(books)
obj.check()

while True:
    print("\n")
    print("1.Add Books")
    print("2.View Books")
    print("3.Issue Books")
    print("4.Return Books")
    print("5.Delete Books")
    print("6.Exit")

    data=int(input("\nPlease Enter Your Operation:"))

    if(data==1):
        obj.add_books()
    elif(data==2):
        obj.view_books()
    elif(data==3):
        obj.issue_books()
    elif (data == 4):
        obj.return_books()
    elif (data == 5):
        obj.delete_books()
    else:
        quit()



