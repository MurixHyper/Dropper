import sys
from subprocess import check_output

us = check_output("chcp 861 && net user", shell=True).decode('cp1252')

for i, u in enumerate(us.split("\n")):
    print(i, u)
