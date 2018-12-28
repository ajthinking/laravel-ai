import sys
import os
from os import walk

root = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../..")
src = os.path.join(root, "src")
raw = os.path.join(root, "data/raw")
sys.path.append(src)
import coach.speak as s #pylint: disable=E0401
from Print import Print #pylint: disable=E0401
import Paths #pylint: disable=E0401

print = Print()





# for (path, users, filenames) in walk(raw):
#     for user in users:
#         print.info(user)
#         print.group()
#         for (raw_path, repos, filenames) in walk(os.path.join(raw, user)):
#             for repo in repos:
#                 print(repo)
#                 for (raw_path, repos, filenames) in walk(os.path.join(raw, user)):
#         print.ungroup()
#     break


# import os
# from glob import glob
# result = [y for x in os.walk(raw) for y in glob(os.path.join(x[0], '*.php'))]
# result = list(map(lambda r: os.path.realpath(r), result))
#print(result)
print(Paths.root)
print(Paths.raw)
print(Paths.processed)