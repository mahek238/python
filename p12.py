with open("test.txt", "r") as src, open("copy.txt", "w") as dst:
 dst.write(src.read())