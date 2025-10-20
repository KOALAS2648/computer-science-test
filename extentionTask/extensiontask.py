import os
def get_data(filename):
    file_data = list(open(filename, "r"))
    #print(file_data)
    for idx, line in enumerate(file_data):
        file_data[idx] = line[:-1].split(",")

    libary_values = {}
    for values in file_data:
        values[2] = values[2] == "True"
        libary_values[int(values[0])] = {"name":values[1], "borrowed":values[2]}
    return libary_values
def write_to_file(filename, dict_to_write):
    filewrite = open(filename, "w")
    for i in dict_to_write:
        temp = dict_to_write[i]
        filewrite.write(f"{i},{temp['name']},{temp['borrowed']}\n")
def loan_a_book():
    data = get_data("server_data.txt")
    book_ID = int(input("what is the book ID  you are looking for?: "))

    try:
        if not data[book_ID]["borrowed"]:
            print("you can have that book")
            data[book_ID]["borrowed"] = True
            write_to_file("server_data.txt", data)
        else:
            print("you can't have that book as it is being borrowed")
    except KeyError:
        print("we do not have that book in this libeary")

def return_a_book():
    data = get_data("server_data.txt")
    bookID = int(input("enter the book ID of the book you want to return: "))
    try:
        data[bookID]["borrowed"] = False
        write_to_file("server_data.txt", data)
        print(f"{data[bookID]['name']} has been returned")
    except KeyError:
        print("cann't find that book in our server")

def view_books():
    data = get_data("server_data.txt")
    for i in data:
        print(f"{i}: is called {data[i]['name']} and is borrowed {data[i]['borrowed']}")

def main():
    while True:
        os.system("clear")
        ask = input("1.do you want to loan a book?\n2.Do you want to retrun a book? \n3.Do you want to exit the libary? ")
        os.system("clear")
        if ask == "1":

            view_books()
            loan_a_book()
        if ask == "2":
            view_books()
            return_a_book()
        if ask == "3" or ask=="exit":
            break

if __name__ == "__main__":
    main()