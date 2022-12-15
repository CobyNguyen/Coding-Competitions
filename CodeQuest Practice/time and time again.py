#Problem 97: Time and Time Again

import sys
import math
import string
import re

cases = int(sys.stdin.readline().rstrip())
hours = re.compile(".*?([0-9]+)h.*")
minutes = re.compile(".*?([0-9]+)m.*")
seconds = re.compile(".*?([0-9]+)s.*")

for caseNum in range(cases):
   data = sys.stdin.readline().rstrip()
   hourMatch = hours.match(data)
   minMatch = minutes.match(data)
   secMatch = seconds.match(data)
   h = 0
   m = 0
   s = 0
   if hourMatch:
      h = int(hourMatch.group(1))
   if minMatch:
      m = int(minMatch.group(1))
   if secMatch:
      s = int(secMatch.group(1))
   if h < 10:
      h = "0" + str(h)
   if m < 10:
      m = "0" + str(m)
   if s < 10:
      s = "0" + str(s)
   print(str(h) + ":" + str(m) + ":" + str(s))