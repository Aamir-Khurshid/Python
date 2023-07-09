import os
files = os.listdir("Images")
i=0
for file in files:
    if file.endswith(".png"):

      i=i+1
      os.rename(f"Images/{file}",f"Images/{i}.png")
      print(file)