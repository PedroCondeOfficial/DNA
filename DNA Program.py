""" 
    *** Created by Pedro Conde, 2016 ***
    *** University of South Florida ***
"""

from Bio.Seq import Seq
    from Bio.Alphabet import IUPAC
    import re
    
while True:
    # Takes input from the user
    x = input("What is your DNA sequence?\n") 
    
    # Checks to see if the sequence is  is using appropriate format
    if not re.match(r"[A,a,C,c,G,g,T,t]", x):
        print("Input a proper DNA sequence!\n")
        continue
    
    # Checks to see if the length of the sequence is correct
    if not len(x)%3 == 0:
        print("Input a properly sized sequence!\n")
        continue
    
    # Creates a class with the various functions in it
    class OPS: 
        # Checks the sequence again
        def __init__(self):
            if not re.match(r"[A,a,C,c,G,g,T,t]", x):
                print("Input a proper DNA sequence!\n")
            if not len(x)%3 == 0:
                print("Input a properly sized sequence!\n")
        # Translates into protein nomenclature
        def translate(self):
            trans = Seq(x, IUPAC.unambiguous_dna)
            trans.translate()
            print(trans.translate())
        # Translates into RNA nomenclature
        def transcribe(self):
            transc = Seq(x, IUPAC.unambiguous_dna)
            transc.transcribe()
            print(transc.transcribe())
        # Performs reverse complementation for opposing strands
        def reversal(self):
            rev = Seq(x, IUPAC.unambiguous_dna)
            rev.reverse_complement()
            print(rev.reverse_complement())
    # Creates an instance of the OPS class
    g = OPS
    
    # Prompts the user for input as to which function they would like to call
    y = input("Which operation would you like to perform(translate, transcribe, or reverse complement)?\n")
    
    # Handles which operation to carry out based on the user's input
    if y.lower() == 'translate':
        print(g.translate(x))
    elif y.lower() == 'transcribe':
        print(g.transcribe(x))
    elif y.lower() == 'reverse complement':
        print(g.reversal(x))
    # Handles any errors involving incorrect commands
    else:
        print("Insert a valid response(translate, transcribe, or reverse complement)\n")
        
    # Prompts the user for an additional operation    
    eta = input("Would you like to start again with a new sequence or operation(Y/N)?\n")
    
    # Checks the user's response to either continue the loop or break out of it
    if eta.lower() == 'y':
        continue
    elif eta.lower() == 'n':
        break    
        
            
        
        
    
        
    
    

    
    

    
    

    
          
  


        
