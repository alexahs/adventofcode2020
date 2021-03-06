import numpy as np

with open("input.txt", "r") as input:
    data = input.readlines()

class Password:
    def __init__(self, low, high, letter, psw):
        self.low = low
        self.high = high
        self.letter = letter
        self.psw = psw

    def is_valid_1(self):
        count = self.psw.count(self.letter)
        if count >= self.low and count <= self.high:
            return 1
        else:
            return 0

    def is_valid_2(self):
        idx1 = self.psw[self.low-1] == self.letter
        idx2 = self.psw[self.high-1] == self.letter
        if idx1 ^ idx2:
            return 1
        else:
            return 0

def parse(data):
    passwords = []
    for line in data:
        line = line.split(' ')
        nums = line[0].split('-')
        low = int(nums[0])
        high = int(nums[1])

        letter = line[1][0]
        psw = line[2][:-1]
        passwords.append(Password(low, high, letter, psw))
    return passwords


n_valid1 = 0
n_valid2 = 0

passwords = parse(data)

for psw in passwords:
    n_valid1 += psw.is_valid_1()
    n_valid2 += psw.is_valid_2()


print(f"(1) Valid passwords: {n_valid1}/{len(data)}")
print(f"(2) Valid passwords: {n_valid2}/{len(data)}")
