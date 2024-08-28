print("Fill in the blank lyrics")
print()
print("Type in the blank lyrics and see if you are as cool as me")
print()
print ("Never going to ____ you up.")
print()

print("")
count = 1
while True:
  
  lyric= input("What is the missing word?: ")
  if lyric == "give":
    
    break
  else:
    print("Nope, Try again")
    count += 1
if count == 1:
  print(f"Woww! It only took you {count} attempt.")
else:
  print(f"Well done! It only took you {count} attempts.")
