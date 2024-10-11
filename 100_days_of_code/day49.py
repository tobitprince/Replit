f= open("savedFile.txt", "r" )
while True:
    contents = f.readline().strip() 
    if contents == "":
        break
    print(contents)
f.close()  
  