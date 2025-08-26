import re

pat = re.compile(r"(Failed password)", re.I)

with open("my_logs", "r") as file:
    for line in file:
        if pat.search(line):  # check if line contains "Failed password"
            with open("password.txt", "a") as failedfile:
                failedfile.write(line)