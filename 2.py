class Computer:
    def __init__(self, brand, os):
        self.brand = brand
        self.__os = os
    
    def install_os(self, os):
        self.__os = os
        print(f"{os} Dar compyteri {self.brand} nasb shudaast.")

my_computer = Computer("Dell", "Windows 11")
my_computer.install_os("Win")