song = """
Humpty Dumpty sat on a wall,
Humpty Dumpty had a great fall
All the king's horses and all the king's men
Couldn't put Humpty together again.Humpty Dumpty sat on a wall,
Humpty Dumpty had a great fall
All the king's horses and all the king's men
Couldn't put Humpty together again.They tried to push him up
They tried to pull him up
They tried to patch him up
Couldn't put him back together again.
"""

print(len(set(song.lower().replace("\"", "").split())))

word_dict = {}

