"""
Name: Adam Stafford
Date: 2/28/24
This program will accurately output the truth tables of six different combinations of AND, OR, and NOT gates, with the first three truth tables-
-being the basic AND, OR, and NOT and the latter three being combinations of those mentioned previously.
"""
###Classes and subroutines###
#parent class framework provided by Dr. Gourd
class Gate:
    def __init__(self, inputs):
        self._inputs = inputs
    
    #getter
    def get_inputs(self):
        
        return self._inputs
    
    #setter
    def set_inputs(self, inputs):
        
        self._inputs = inputs
    #allow us to use .inputs on instances of gate   
    inputs = property(get_inputs, set_inputs)
        
    def evaluate(self):
        return 0
    
#AND gate provided by Dr. Gourd
#basic logic class for AND gate truthtable(s).
class AND_Gate(Gate):
    #inputs assigned as a 2 variable list, remains true for remaining Gate classes as well. 
    def __init__(self, inputs=[0,0]):
        #inheriting from the Gate Class, remains true for remaining Gate classes as well.
        super().__init__(inputs)
        
    #evaluation logic: if program runs through the inputs from 0 to 1 and finds that they both equal 1, will return True, or 1. Expanded in subroutines.
    #Any other combination will return False, or 0.
    def evaluate(self):
        if (self._inputs[0] == 1 and self._inputs[1] == 1):
            return 1
        else:
            return 0
#basic logical class for OR gate truthtable(s).
class OR_Gate(Gate):
    def __init__(self, inputs=[0,0]):
        super().__init__(inputs)
    
    #evaluation logic: program will run through inputs from 0 to 1 and will return True/1 if there is at least one or more "1" in each column. Expanded in subroutines.
    #only combination that will return False/0 is the column containing two "0s".
    def evaluate(self):
        if (self._inputs[0] == 1 or self._inputs[1] == 1):
            return 1
        if (self._inputs[0] == 1 and self._inputs[1] == 1):
            return 1
        else:
            return 0
        
#basic logical class for NOT gate truthtable(s).       
class NOT_Gate(Gate):
    def __init__(self, inputs=[0,0]):
        super().__init__(inputs)
        
    #evaluation logic: program will invert inputs 0 and 1. 
    def evaluate(self):
        if self._inputs[0] == 1:
            return 0
        else:
            return 1
        
#AND truthtable provided by Dr. Gourd
def AND_Truth_Table():
    print("AND Gate")
    print("A B Out")
    gate = AND_Gate()
    for A in range(0,2):
        for B in range(0,2):
            #setter in Gate class allows for use of setter to set values of A and B as it goes through loop.
            gate.inputs = [A, B] 
            output = gate.evaluate()
            #simple .format function to print results to terminal. Same function used throughout subroutines
            print("{} {} {}".format(A, B, output))
            
#OR truthtable posseses same logic as the AND truthtable. the only difference being calling the OR Gate Class instead          
def OR_Truth_Table():
    print("OR Gate")
    print("A B Out")
    gate = OR_Gate()
    for A in range(0,2):
        for B in range(0,2):
            
            gate.inputs = [A, B] 
            output = gate.evaluate()
            
            print("{} {} {}".format(A, B, output))
            
#Mostly similar to AND and OR truth tables, with the only difference being only going through A and inverting the output to prove functionality.      
def NOT_Truth_Table():
    print("NOT Gate")
    print("A Out")
    gate = NOT_Gate()
    for A in range(0,2):
        
        gate.inputs = [A] 
        output = gate.evaluate()
        
        print("{} {}".format(A, output))
        
#NAND utilizes both the AND and NOT gate classes to output correct truthtable. Part of framework provided by Dr. Gourd.
def NAND_Truth_Table():
    print("NAND Gate")
    print("A B Out")
    and_gate = AND_Gate()
    not_gate = NOT_Gate()
    for A in range(0,2):
        for B in range(0,2):
            
            and_gate.inputs = [A, B] 
            and_output = and_gate.evaluate()
            #NOT gate evaluates the results of the AND gate evaluation and inverts the results
            not_gate.inputs = [and_output]
            output = not_gate.evaluate()
            
            print("{} {} {}".format(A, B, output))
            
#Circuit drawing one requires use of all three basic Gate classes to acquire correct truthtable
#z = (A*B) + (not C)
def Circuit_Drawing_One_Truth():
    print("Circuit Drawing 1")
    print("A B C Out")
    and_gate = AND_Gate()
    or_gate = OR_Gate()
    not_gate = NOT_Gate()
    #nested for loop requires a third variable, C, for correct evaluation
    for A in range(0,2):
        for B in range(0,2):
            for C in range(0,2):
                #and gate A B is evaluated from 0 to 1 and stored as output
                and_gate.inputs = [A,B]
                and_output = and_gate.evaluate()
                #NOT gate only has variable C to evaluate and stored as not_output
                not_gate.inputs = [C]
                not_output = not_gate.evaluate()
                #OR gate class takes both output results of AND and NOT gate variables A,B,C and evaluates then stores it as a final output to be printed.
                #CHATGPT assisted me by telling me to put a comma between the and_output and not_output instead of a "+" like i originally had.
                #this helped my logic in both this subroutine and the next.
                or_gate.inputs = [and_output, not_output]
                output = or_gate.evaluate()
                print("{} {} {} {}".format(A, B, C, output))
    
#Being the most complicated, circuit drawing two requires 3 AND gates, 2 NOT Gates, and 1 OR gate to procure accurate truthtable
# z = [not(P*Q) + (P * R)] * not R
def Circuit_Drawing_Two_Truth():
    print("Circuit Drawing 2")
    print("P Q R Out")
    and_gate1 = AND_Gate()
    and_gate2 = AND_Gate()
    and_gate3 = AND_Gate()
    or_gate = OR_Gate()
    not_gate1 = NOT_Gate()
    not_gate2= NOT_Gate()
    #Once again, for loop requires an additional nested variable
    for P in range(0,2):
        for Q in range(0,2):
            for R in range(0,2):
                #calls on and_gate class to note P and Q and P and R as [0,0] for correct evaluation.
                and_gate1.inputs = [P, Q]
                and_gate2.inputs = [P, R]
                #NOT gate 1 input used to invert and_gate1 results
                #NOT gate 2 inverts R
                not_gate1.inputs = [and_gate1.evaluate()]
                not_gate2.inputs = [R]
                #OR gate utilized to interpret and evaluate results of the invertion of and_gate1 and regular results of and_gate 2
                #CHATGPT assisted me in a small way by telling me to swap the not_gate1.evaluate() and or_gate.evaluate() to
                #the locations they are at now. A small but very big logical change that flew right over my head when writing originally.
                or_gate.inputs = [not_gate1.evaluate(), and_gate2.evaluate()]
                and_gate3.inputs = [or_gate.evaluate(), not_gate2.evaluate()]
                #AND gate 3 will take results of the or gate results and not gate result of R to get the final output
                output = and_gate3.evaluate()
                
                print("{} {} {} {}".format(P, Q, R, output))
                    
###MAIN PROGRAM###
AND_Truth_Table()

OR_Truth_Table()

NOT_Truth_Table()

NAND_Truth_Table()

Circuit_Drawing_One_Truth()

Circuit_Drawing_Two_Truth()