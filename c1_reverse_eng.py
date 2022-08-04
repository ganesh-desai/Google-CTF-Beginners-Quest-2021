arr = [52037,
52077,
52077,
52066,
52046,
52063,
52081,
52081,
52085,
52077,
52080,
52066]

# subtract cafe from each array and convert to ascii

for v in arr:
  print(chr(v - 0xcafe), end="")

# GoodPassword
# CTF{IJustHopeThisIsNotOnShodan}
