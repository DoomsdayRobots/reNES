
import tkinter as tk  # gives tk namespace
from tkinter import filedialog as fd 
import os, os.path
import os

def open_dir():
    """
    sets the working directory
    here is a small list of filedialogcommands
    fd.asksaveasfilename()
    fd.asksaveasfile()
    fd.askopenfilename()
    fd.askopenfile()
    fd.askdirectory()
    fd.askopenfilenames()
    fd.askopenfiles()
    """
    
    wd_dir = fd.askdirectory(title = 'Please select the directory to work in')
    if wd_dir != "":
        #print(wd_dir)
        return(wd_dir)

def clearTextInput():
    T.delete("1.0","end")
    
def get_nes_file_names():  
    
    f = open(tf, 'w')

    for filename in os.listdir(cwd):
        if os.path.isfile(os.path.join(cwd, filename)):
            result = filename.find(".nes")
            if result >= 0:
                newstring = filename + '\n'
                f.write(newstring)
    
def answer(Event):
    global reply_counter
    global search_string
    global replace_string
    
    reply = enter1.get()

    #replacement_string = ""
    
    #print("You answered: "+reply+". The reply counter is now set to: "+str(reply_counter))

    if reply_counter == 99:
        entryText.set("")
        reply = "y"
        reply_counter = 6
        
        
    if reply_counter == 0:
        if reply == "Y" or reply == "YES" or reply == "Yes" or reply == "y" or reply == "yes":
            #print("you typed "+reply) 
            wd = open_dir()
            clearTextInput()
            message = """OK, awesome! You've selected\n   """+wd+"""\nfor your working directory.\n\nWould you like to see the list of ".nes" files\n(Y\\N)?\n"""  
            T.insert("1.0", message)
            entryText.set("")
            reply_counter = 1
            return()
        
        if reply == "N" or reply == "NO" or reply == "No" or reply == "n" or reply == "no":
            clearTextInput()
            entryText.set("")
            reply_counter = 2
        
        
    if reply_counter == 1:
        if reply == "Y" or reply == "YES" or reply == "Yes" or reply == "y" or reply == "yes":
            #print("you typed "+reply)
            get_nes_file_names()
            f = open(tf,'r')
            filedata = f.read()
            clearTextInput()
            message = "Here it is...\nScroll down to see everything.\n\n"+filedata+"\n"
            T.insert("1.0", message)
            f.close()
            os.remove(tf)
            entryText.set("")
            reply_counter = 2
 
            
        if reply == "N" or reply == "NO" or reply == "No" or reply == "n" or reply == "no":
            clearTextInput()
            entryText.set("")
            reply_counter = 2

    if reply_counter == 2:
        message = "would you like to add, delete or replace something form the exsisting title?...\n(A\\D\\R)?\n"
        T.insert("end", message)
        entryText.set("")
        reply_counter = 3
        return()
        
    if reply_counter == 3:
        if reply == "A" or reply == "ADD" or reply == "Add" or reply == "a" or reply == "add":
            clearTextInput()
            message = "You chose to 'Add' something.\n The only option to add some thing is with numbers.\n Spicificaly that the numbers will preceed the file names.\n like in this example...\n   1000 Adventure Island.nes\n   1001 Adventure Island II (U).nes\n   1002 Dragon Warrior.nes\n\nWould you like to continue (Y\\N)?\n"
            T.insert("1.0", message)
            entryText.set("")
            reply_counter = 4
            return()
        
        if reply == "D" or reply == "DELETE" or reply == "Delete" or reply == "DEL" or reply == "Del" or reply == "del" or reply == "d" or reply == "delete":
            clearTextInput()
            message = "You chose to 'Delete' something.\n  What would you like to delete?\n\nHere are some common examples of what to enter\n  Take note of the extra space before the requested text to delete.\n  This is only in some of the folowing examples...\n     ' (U)'  ' (Unl)'  ' (J)' 'numbers'.\n"
            T.insert("1.0", message)
            entryText.set("")
            reply_counter = 5
            return()
        if reply == "R" or reply == "REPLACE" or reply == "Replace" or reply == "REL" or reply == "Rel" or reply == "rel" or reply == "r" or reply == "replace":
            clearTextInput()
            message = "You chose to 'Replace' something. What would you like to replace?\n  Take note, what ever you type in will be searched for here\n   and then replaced in the next step.\n  Here are some examples...\n    replacing II with 2   replacing IV with 7.\n"
            T.insert("1.0", message)
            entryText.set("")
            reply_counter = 10
            return()
            
        
    if reply_counter == 5:
        if reply == "Numbers" or reply == "numbers" or reply == "Num" or reply == "num" or reply == "N" or reply == "n":
            clearTextInput()
            message = "You chose numbers, is this correct (Y\\N)?\n"
            T.insert("1.0", message)
            reply_counter = 6
            entryText.set("")
            return()
        if reply != "Numbers" or reply != "numbers" or reply != "Num" or reply != "num" or reply != "N" or reply != "n":
            clearTextInput()
            search_string = reply
            replace_string = ""
            f = open(tf, 'w')
        
            for filename in os.listdir(cwd):
                if os.path.isfile(os.path.join(cwd, filename)):
                    result = filename.find(".nes")
                    if result >= 0:
                        result = filename.find(search_string)
                        if result >= 0:
                            newfilename = filename.replace(search_string,replace_string)
                            #print("replacing: "+filename+" with: "+newfilename)
                            os.rename(filename,newfilename)
                            newstring = newfilename + '\n'
                            f.write(newstring)
                
            f.close()
            os.remove(tf)
        
            message = """You have chosen to delete the phrase: """+reply+"""\n  from all of the ".nes" files in this directory.\n    Would you like To see the file list now? (Y\\N)?\n\n"""
            T.insert("1.0", message)
            entryText.set("")
            reply_counter = 8
            #return()
        
        
    if reply_counter == 6:
        if reply == "Y" or reply == "YES" or reply == "Yes" or reply == "y" or reply == "yes":
            clearTextInput()
            message = "You chose numbers.\n  Please select a range eg 1 to 1000\n"
            T.insert("1.0", message)
            entryText.set("")
            reply_counter = 7
            return()
        
        if reply == "N" or reply == "NO" or reply == "No" or reply == "n" or reply == "no":
            clearTextInput()
            message = "Oops!\n  Press any key to continue...\n\n"
            T.insert("1.0", message)
            reply_counter = 2
            entryText.set("")
            return()
        
    if reply_counter == 7:
        print(" ")
        clearTextInput()
        try:
            # Convert it into integer
            val = int(reply)
            #print("Your input was an integer = ", str(val))
            #clearTextInput()
            message = "Your input was an integer = "+str(val)+"\n\n"
            T.insert("1.0", message)
        except ValueError:
            try:
                # Convert it into float
                val = float(reply)
                #print("Your input was a float = ", str(val))
                #clearTextInput()
                message = "Your input was a float = "+str(val)+"\n\n"
                T.insert("1.0", message)
            except ValueError:
                #print("No!! Your input was not a number.\n\n  Please try again...\n\n   Press any key to continue...\n\n")
                clearTextInput()
                message = "No!! Your input was not a number.\n\n  Please try again...\n\n   Press any key to continue...\n\n"
                T.insert("1.0", message)
                entryText.set("")
                reply_counter = 99
                return()
            
        #do the file renaming here...
        replace_string = ""
        number_range = int(reply)
        length_of_input = 1+len(str(reply))
        printcounter = 0

        f = open(tf, 'w')
        
        for filename in os.listdir(cwd):
            if os.path.isfile(os.path.join(cwd, filename)):
                result = filename.find(".nes")
                if result >= 0:
                    #OK we know that we only have.nes files at this point.
                    flag = 0    
                    if flag == 0:
                        #print("Current file: "+filename)
                        #print("Resetting...........................")
                        #print("")
                        flag = 1
                        
                    x = 0
                    print_counter = 0
                    for x in range(0,int(number_range)+1):
                        current_num = str(x)
                        #number_in_filename = (filename[:length_of_input])
                        space_in_filename = filename.find(" ",0,length_of_input)
                        number_in_filename = (filename[:space_in_filename])    
   
                        if current_num == number_in_filename:
                            old = str(x)+" "
                            newfilename = filename.replace(old,"")
                            #print("Changing : "+filename+" to: "+newfilename)
                            os.rename(filename,newfilename)
                            newstring = newfilename + '\n'
                            f.write(newstring)
                        
        f.close()
        os.remove(tf)

        message = """The numbers 1 to """+reply+""" have now been deleted \n  from all of the ".nes" files in this directory.\n    Would you like To see the file list now? (Y\\N)?\n\n"""
        T.insert("end", message)
        entryText.set("")
        reply_counter = 8
        #return()

    if reply_counter == 8:
        if reply == "Y" or reply == "YES" or reply == "Yes" or reply == "y" or reply == "yes":
            get_nes_file_names()
            f = open(tf,'r')
            filedata = f.read()
            clearTextInput()
            message = "Here it is...\nScroll down to see everything.\n\n"+filedata+"\nAre you done using reNES (Y\\N)?\n"
            T.insert("1.0", message)
            f.close()
            os.remove(tf)
            entryText.set("")
            reply_counter = 9
            return()
        
        if reply == "N" or reply == "NO" or reply == "No" or reply == "n" or reply == "no":
            message = "Are you done using reNES (Y\\N)?\n"
            T.insert("end", message)
            entryText.set("")
            reply_counter = 9
            return()
        
    if reply_counter == 9:
        if reply == "Y" or reply == "YES" or reply == "Yes" or reply == "y" or reply == "yes":
            clearTextInput()
            message = "Thankyou for using reNes!"
            T.insert("1.0", message)
            entryText.set("")
            reply_counter = 9
            return()
        if reply == "N" or reply == "NO" or reply == "No" or reply == "n" or reply == "no":
            clearTextInput()
            message = "OK, Cool!\n\n  Hit any key to continue...\n\n"
            T.insert("1.0", message)
            entryText.set("")
            reply_counter = 2
            
    #------------------------------------------------------------------------------
            
    if reply_counter == 10:
        search_string  = reply
        clearTextInput()
        message = "You have chosen '"+search_string +"' as the thing to search for, is this correct (Y\\N)\n"
        T.insert("1.0", message)
        entryText.set("")
        reply_counter = 11
        return()
        
    if reply_counter == 11:
        if reply == "Y" or reply == "YES" or reply == "Yes" or reply == "y" or reply == "yes":
            clearTextInput()
            message = "OK! Now we will type in something to replace '"+search_string+"' with."
            T.insert("1.0", message)
            entryText.set("")
            reply_counter = 12
            return()
            
        if reply == "N" or reply == "NO" or reply == "No" or reply == "n" or reply == "no":
            clearTextInput()
            message = "Oops! Try again."
            search_string = ""
            T.insert("1.0", message)
            entryText.set("")
            reply_counter = 2
            return()
        
    if reply_counter == 12:
        replace_string = reply
        clearTextInput()
        message = "You have chosen '"+replace_string +"' as the thing to replace, is this correct (Y\\N)\n"
        T.insert("1.0", message)
        entryText.set("")
        reply_counter = 13
        return()
    
    if reply_counter == 13:
        if reply == "Y" or reply == "YES" or reply == "Yes" or reply == "y" or reply == "yes":
            clearTextInput()
            message = """OK! So, we replace '"""+search_string+"""' with '"""+replace_string+"""'\nWe will do this for all of the ".nes" files in this directory.\n    Would you like To see the file list now? (Y\\N)?\n\n"""
            T.insert("1.0", message)
            f = open(tf, 'w')
        
            for filename in os.listdir(cwd):
                if os.path.isfile(os.path.join(cwd, filename)):
                    result = filename.find(".nes")
                    if result >= 0:
                        result = filename.find(search_string)
                        if result >= 0:
                            newfilename = filename.replace(search_string,replace_string)
                            #print("replacing: "+filename+" with: "+newfilename)
                            os.rename(filename,newfilename)
                            newstring = newfilename + '\n'
                            f.write(newstring)
                
            f.close()
            os.remove(tf)
            
            entryText.set("")
            reply_counter = 8
            return()
        
        if reply == "N" or reply == "NO" or reply == "No" or reply == "n" or reply == "no":
            clearTextInput()
            message = "Oops! Try again."
            search_string = ""
            T.insert("1.0", message)
            entryText.set("")
            reply_counter = 2
            return()
        
    if reply_counter == 4:
        if reply == "Y" or reply == "YES" or reply == "Yes" or reply == "y" or reply == "yes":
            clearTextInput()
                                
            #filecount = get_nes_file_names()
            numcount = 0
                
            f = open(tf, 'w')
            for filename in os.listdir(cwd):
                if os.path.isfile(os.path.join(cwd, filename)):
                    result = filename.find(".nes")
                    if result >= 0:
                        numcount = numcount + 1
                        #prepend = str(numcount)
                        newfilename = str(numcount)+" "+filename
                        #print("replacing: "+filename+" with: "+newfilename)
                        os.rename(filename,newfilename)
                        newstring = newfilename + '\n'
                        f.write(newstring)
                
            f.close()
            os.remove(tf)

            message = """Awesome! The numbers have now been added \nto all of the ".nes" files in this directory.\n    Would you like To see the file list now? (Y\\N)?\n\n"""
            T.insert("1.0", message)
            entryText.set("")
            reply_counter = 8
            return()
        if reply == "N" or reply == "NO" or reply == "No" or reply == "n" or reply == "no":
            clearTextInput()
            message = "Oops! Thats OK, We will just try again."
            T.insert("1.0", message)
            entryText.set("")
            reply_counter = 2
            return()
        
    
        
        
            
    
# create the main window
label_width = 100
text_box_width = label_width - 10
text_box_height = 8
entry_width = label_width
right_blank_width = 2
bottom_blank_width = label_width
pad_val = 10
reply_counter = 0
tf = "temp.txt"
cwd = os.getcwd()

window = tk.Tk()
window.title("reNES")

# create a blank label to the right of the textbox
title = tk.Label(window, text='',width=right_blank_width)
title.grid(row=0, column=0, sticky=tk.W)

# create a blank label to the right of the textbox
title = tk.Label(window, text='',width=right_blank_width)
title.grid(row=0, column=3, sticky=tk.W)

# create a label above the textbox
title = tk.Label(window, text='reNES Terminal',width=label_width)
title.grid(row=0, column=1, sticky=tk.W)

# Create text widget and specify size.
T = tk.Text(window,height = text_box_height,width = text_box_width,padx = pad_val,pady = pad_val)
T.grid(row=1, column=1, sticky=tk.W)

message = """Welcome to reNES!
reNES is a ".nes" title editor.

Lets start by selecting a directory
that contains ".nes" files.

type (Y/N) into the box below."""

# fill message
T.insert("1.0", message)

# create a label above the first list box
entry_title = tk.Label(window, text='Your answers go here',width=label_width,justify='center')
entry_title.grid(row=2, column=1, sticky=tk.W)


# create an entry widget to display or edit text
entryText = tk.StringVar()
enter1 = tk.Entry(window, width=entry_width,textvariable=entryText )
entryText.set( 'Type your answere here' )
enter1.grid(row=3, column=1)

# pressing the return key will update edited line
enter1.bind('<Return>', answer)

# or double click left mouse button to update line
enter1.bind('<Double-1>', answer)

# create a blank label below the entry box
title = tk.Label(window, text='',width=right_blank_width)
title.grid(row=4, column=0, sticky=tk.W)

window.mainloop()
