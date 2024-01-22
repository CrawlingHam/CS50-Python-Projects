                # ABOUT PROGRAM
'''In a file called extensions.py, implement a program that prompts the user for the 
name of a file and then outputs that file’s media type if the file’s name ends, 
case-insensitively, in any of these suffixes:

.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip '''


filename = input("Enter filename: " )
filename_edited = filename.rstrip().lower()

if filename_edited.endswith(".jpg"): print("image/jpeg")
elif filename_edited.endswith(".jpeg"): print("image/jpeg")
elif filename_edited.endswith(".png"): print("image/png")
elif filename_edited.endswith(".pdf"): print("application/pdf")
elif filename_edited.endswith(".txt"): print("text/plain")
elif filename_edited.endswith(".zip"): print("application/zip")
elif filename_edited.endswith(".gif"): print("image/gif")
else: print("application/octet-stream")