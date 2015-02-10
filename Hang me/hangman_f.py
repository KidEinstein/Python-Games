# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
from Tkinter import *
import tkFont
import ImageTk
root=Tk()
master=Frame(root)
master.grid(row=0, column=0)
import sys
import Image
hangImage=['Hangman\hangman1.png','Hangman\hangman2.png','Hangman\hangman3.png','Hangman\hangman4.png','Hangman\hangman5.png'\
           ,'Hangman\hangman6.png','Hangman\hangman7.png','Hangman\hangman8.png','Hangman\hangman9.png','Hangman\hangman10.png','Hangman\hangman11.png']
WORDLIST_FILENAME = "words.txt"
#root.wm_attributes('-alpha', 0.7)  
default_font = tkFont.nametofont("TkDefaultFont")
default_font.configure(size=15)
root.option_add("*Font", "stencil")
root.option_add("*Background", "white")
root.option_add("*Button.Background", "yellow")

root.resizable(width=FALSE, height=FALSE)

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    st=''
    for i in range(len(secretWord)):
        if(secretWord[i] in lettersGuessed):
            st=st+secretWord[i]
        else:
            st=st+'_'+' '
    return st



import string
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    abc=string.ascii_lowercase
    st=''
    for i in abc:
        if(i not in lettersGuessed):
            st=st+i
    return st
def appendGuess(letter,sw):

    global g
    global guessLabel
    global endLabel
    global label
    global wrongAns
    try:
        guessLabel.grid_forget()
    except:
        pass
    try:
        endLabel.grid_forget()
    except:
        pass
    try:
        label.grid_forget()
    except:
        pass
    try:
        canvas.grid_forget()
    except:
        pass
    
    if(letter not in lettersGuessed):
        lettersGuessed.append(letter)
        if letter in sw:
            
            guessLabel=Label(master, text=('Good guess: ' + getGuessedWord(sw, lettersGuessed)))
            guessLabel.grid(row=3,column=0,columnspan=26,pady=10)
            b[letter].config(state=DISABLED,disabledforeground="white")

            
        else:
            guessLabel=Label(master, text=('Oops! That letter is not in my word: ' + getGuessedWord(sw, lettersGuessed)))
            guessLabel.grid(row=3,column=0,columnspan=26,pady=10)
            g-=1
            wrongAns+=1
            b[letter].config(state=DISABLED,disabledforeground="white")
    canvas = Canvas(master,width=300,height=279)
    image=ImageTk.PhotoImage(file="Backgrounds\\bg2.jpg")
    photo = ImageTk.PhotoImage(file=hangImage[wrongAns])
    canvas.create_image(0,0, image=image)
    canvas.create_image(0,0, image=photo, anchor=NW)
    canvas.image=image
    canvas.image1=photo
    canvas.grid(row=6,column=0,columnspan=26)
    
    
    
##    
##    label=Label(master, image=photo)
##    label.image = photo
##    label.grid(row=5,column=0,columnspan=26)

            

    if(getGuessedWord(sw, lettersGuessed)==sw):
        guessLabel.pack_forget()
        endLabel=Label(master,text= 'Congratulations, you won!')
        endLabel.grid(row=8,column=0,columnspan=26,pady=10)
        close()
    elif(g==0):
        guessLabel.pack_forget()
        endLabel=Label(master, text=('Sorry, you ran out of guesses. The word was ' + sw + '.'))
        endLabel.grid(row=8,column=0,columnspan=26,pady=10)
        close()
    else:
        endLabel=Label(master, text=('You have ' +str(g) + ' guesses left.'))
        endLabel.grid(row=8,column=0,columnspan=26,pady=10)
    
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...

##    print 'Welcome to the game, Hangman!'
##    print 'I am thinking of a word that is ' +str(len(sw)) + ' letters long.'
##    print '-------------'
##    g=10
##    while g>0:
##        print 'You have ' +str(g) + ' guesses left.'
##        print 'Available letters: ', getAvailableLetters(lettersGuessed)
##        gl=raw_input("Please guess a letter: ")
##        gl=gl.lower()
##        if(gl not in lettersGuessed):
##            lettersGuessed.append(gl)   
##            if gl in sw:
##                print 'Good guess: ', getGuessedWord(sw, lettersGuessed)
##            else:
##                print 'Oops! That letter is not in my word: ', getGuessedWord(sw, lettersGuessed)
##                g-=1
##        else:
##            print 'Oops! You\'ve already guessed that letter: ', getGuessedWord(sw, lettersGuessed)
##        print '-------------'
##        if(getGuessedWord(sw, lettersGuessed)==sw):
##            print 'Congratulations, you won!'
##            return 
##    print 'Sorry, you ran out of guesses. The word was ', sw,'.'
    global label
    sw=secretWord
    welcomeLabel=Label(master, text="'Welcome to the game, Hangman!'")
    welcomeLabel.grid(row=0,column=0,columnspan=26,pady=10)
    numLabel=Label(master, text='I am thinking of a word that is ' +str(len(sw)) + ' letters long.')
    numLabel.grid(row=1,column=0,columnspan=26,pady=10)
##    dashLabel=Label(master)
##    dashLabel.grid(row=2,column=0,columnspan=26,pady=10)
    buttons(sw)
    canvas = Canvas(master,width=300,height=279)
    image=ImageTk.PhotoImage(file="Backgrounds\\bg2.jpg")
    photo = ImageTk.PhotoImage(file=hangImage[0])
    canvas.create_image(0,0, image=image)
    canvas.create_image(0,0, image=photo, anchor=NW)
    canvas.image=image
    canvas.image1=photo
    canvas.grid(row=6,column=0,columnspan=26)
##    label=Label(master,image=photo)
##    label.image = photo
##    label.grid(row=5,column=0,columnspan=26)

def buttons(sw):
    b['a']=Button(master, text='a', command=lambda: appendGuess('a',sw))
    b['b']=Button(master, text='b', command=lambda: appendGuess('b',sw))
    b['c']=Button(master, text='c', command=lambda: appendGuess('c',sw))
    b['d']=Button(master, text='d', command=lambda: appendGuess('d',sw))
    b['e']=Button(master, text='e', command=lambda: appendGuess('e',sw))
    b['f']=Button(master, text='f', command=lambda: appendGuess('f',sw))
    b['g']=Button(master, text='g', command=lambda: appendGuess('g',sw))
    b['h']=Button(master, text='h', command=lambda: appendGuess('h',sw))
    b['i']=Button(master, text='i', command=lambda: appendGuess('i',sw))
    b['j']=Button(master, text='j', command=lambda: appendGuess('j',sw))
    b['k']=Button(master, text='k', command=lambda: appendGuess('k',sw))
    b['l']=Button(master, text='l', command=lambda: appendGuess('l',sw))
    b['m']=Button(master, text='m', command=lambda: appendGuess('m',sw))
    b['n']=Button(master, text='n', command=lambda: appendGuess('n',sw))
    b['o']=Button(master, text='o', command=lambda: appendGuess('o',sw))
    b['p']=Button(master, text='p', command=lambda: appendGuess('p',sw))
    b['q']=Button(master, text='q', command=lambda: appendGuess('q',sw))
    b['r']=Button(master, text='r', command=lambda: appendGuess('r',sw))
    b['s']=Button(master, text='s', command=lambda: appendGuess('s',sw))
    b['t']=Button(master, text='t', command=lambda: appendGuess('t',sw))
    b['u']=Button(master, text='u', command=lambda: appendGuess('u',sw))
    b['v']=Button(master, text='v', command=lambda: appendGuess('v',sw))
    b['w']=Button(master, text='w', command=lambda: appendGuess('w',sw))
    b['x']=Button(master, text='x', command=lambda: appendGuess('x',sw))
    b['y']=Button(master, text='y', command=lambda: appendGuess('y',sw))
    b['z']=Button(master, text='z', command=lambda: appendGuess('z',sw))
    for i in string.ascii_lowercase[:13]:         
        b[i].grid(row=4, column=string.ascii_lowercase.find(i) ,padx=10,pady=10)
    for i in string.ascii_lowercase[13:]:        
        b[i].grid(row=5, column=string.ascii_lowercase.find(i)-13 ,padx=10,pady=10)
    
        

def close():
    for i in string.ascii_lowercase:         
        b[i].config(state=DISABLED)
    thankLabel=Label(master, text="Thank you for playing")
    thankLabel.grid(row=9,column=0,columnspan=26,pady=10)
    newGame=Button(master, text='Start New Game',command=NewGame)
    newGame.grid(row=10,column=0,columnspan=26,pady=10)

def NewGame():
    global master
    master.destroy()
    master=Frame()
    master.grid(row=0, column=0)
    secretWord = chooseWord(wordlist).lower()
    global b
    b={}
    global lettersGuessed
    lettersGuessed=[]
    global g
    g=10
    global wrongAns
    wrongAns=0
    global bgImage
    global bgLabel
    bgImage=ImageTk.PhotoImage(file='Backgrounds\\bg5.png')
    bgLabel=Label(master, image=bgImage)
    bgLabel.place(x=0,y=0)
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
    hangman("apple")
    
    

    

    
    
b={}
lettersGuessed=[]
g=10
wrongAns=0
guessLabel=Label(master)
endLabel=Label(master)
wrongAns=0
bgImage=ImageTk.PhotoImage(file='Backgrounds\\bg2.jpg')
bgLabel=Label(master, image=bgImage)
bgLabel.place(x=0,y=0)

NewGame()
mainloop()

    











