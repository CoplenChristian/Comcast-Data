from scraper import ComcastLogin

user = input("Please enter your Xfinity username (this data will not be stored, promise!): ")
password = input("Please enter your Xfinity password (again, this data will not be stored, you can check the files of the program.): ")

ComcastLogin(user, password)
