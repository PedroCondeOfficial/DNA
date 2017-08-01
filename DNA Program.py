while True:
    from Bio.Seq import Seq
    from Bio.Alphabet import IUPAC
    import re
    
    x = input("What is your DNA sequence?\n")
    
    if not re.match(r"[A,a,C,c,G,g,T,t]", x):
        print("Input a proper DNA sequence!\n")
        continue
    
    if not len(x)%3 == 0:
        print("Input a properly sized sequence!\n")
        continue
    
    
    class OPS: 
        def __init__(self):
            if not re.match(r"[A,a,C,c,G,g,T,t]", x):
                print("Input a proper DNA sequence!\n")
            if not len(x)%3 == 0:
                print("Input a properly sized sequence!\n")
        def translate(self):
            trans = Seq(x, IUPAC.unambiguous_dna)
            trans.translate()
            print(trans.translate())
        
        def transcribe(self):
            transc = Seq(x, IUPAC.unambiguous_dna)
            transc.transcribe()
            print(transc.transcribe())
        
        def reversal(self):
            rev = Seq(x, IUPAC.unambiguous_dna)
            rev.reverse_complement()
            print(rev.reverse_complement())
            
    g = OPS
    
    y = input("Which operation would you like to perform(translate, transcribe, or reverse complement)?\n")
    
    if y.lower() == 'translate':
        print(g.translate(x))
    elif y.lower() == 'transcribe':
        print(g.transcribe(x))
    elif y.lower() == 'reverse complement':
        print(g.reversal(x))
    else:
        print("Insert a valid response(translate, transcribe, or reverse complement)\n")
        
        
    eta = input("Would you like to start again with a new sequence or operation(Y/N)?\n")
        
    if eta.lower() == 'y':
        continue
    elif eta.lower() == 'n':
        break    
        
            
        
        
    
        
    
    

    
    

    
    

    
          
  


        