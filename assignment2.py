import socket

class Assignment2:
    def __init__(self, year):
        self.year = year

    def tellAge(self, currentYear):
        age = currentYear - self.year
        print(f'Your age is {age}')

    def listAnniversaries(self):
        currentYear = 2022
        anniversary_years = [i for i in range(10, currentYear - self.year + 1, 10)]
        return anniversary_years

    def modifyYear(self, n):
        year_str = str(self.year)
        odd_year_str = str(self.year * n)
        result_str = (year_str[:2] * n) + ''.join([odd_year_str[i] for i in range(len(odd_year_str)) if i % 2 == 0])
        return result_str

    @staticmethod
    def checkGoodString(string):
        if len(string) >= 9 and string[0].islower() and sum([1 for char in string if char.isdigit()]) == 1:
            return True
        else:
            return False

    @staticmethod
    def connectTcp(host, port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            s.close()
            return True
        except socket.error:
            return False
