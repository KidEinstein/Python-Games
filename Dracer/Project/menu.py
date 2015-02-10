from Tkinter import *
master = Tk()

def race():
    import race
def hang():
    import hangman
def snake():
    import snake
    
    
b = Button(master, text="Racing Game", command=print 'Apple',padx=5,pady=5)
c = Button(master, text="Hangman", command=hang,padx=5,pady=5)
d = Button(master, text="Snake", command=snake,padx=5,pady=5)

b.grid(padx=10,pady=5)
c.grid(padx=10,pady=5)
d.grid(padx=10,pady=5)
mainloop()
