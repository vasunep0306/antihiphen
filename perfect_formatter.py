from tkinter import *
import re


root = Tk()
root.minsize(800, 600)
text = Text(root, width=800//10, height=600//20)

#re.sub('[ES]', 'a', s)
def writeOut():
    global text
    words = text.get("1.0","end-1c")
    new_words = []
    hyphenated_words = re.findall(r"\w+(?:- \S+\w+)+", words)
    for x in hyphenated_words:
        nx = x.replace("- ", "")
        words = words.replace(x, nx)
    print(words)

##    print(type(hyphenated_words))
##    print(re.search(r"\w+(?:- \S+\w+)+", words).group(0))
    #print(re.sub(r"\w+(?:- \S+\w+)+", "\b", words))
    f = open("output.txt", "w")
    f.write(text.get("1.0","end-1c"))
    f.close()




B = Button(root, text="Format And Writeout", command=writeOut)
B.place(x = 800//2, y = 600//3)
text.pack()
B.pack()
root.mainloop()
