import re
import sys

if(len(sys.argv)>1):
  file = open(sys.argv[1], encoding = "ISO-8859-1")
else:
  file = open(sys.stdin.fileno(), encoding = "ISO-8859-1")

minlength = 8
maxlength = 20
specials = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
lowers = re.compile('[abcdefghijklmnopqrstuvwxyz]')
uppers = re.compile('[ABCDEFGHIJKLMNOPQRSTUVWXYZ]')
numeric = re.compile('[0123456789]')

while 1:
  words = file.readlines(100000)
  if not words:
    break

  for word in words:
    word=word.strip()
    if(len(word)<minlength):
      continue
    if(len(word)>maxlength):
      continue
    if(None==specials.search(word)):
      continue
    if(None==lowers.search(word)):
      continue
    if(None==uppers.search(word)):
      continue
    if(None==numeric.search(word)):
      continue
    print(word)
