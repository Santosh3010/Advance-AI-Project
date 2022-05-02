# Import libraries
import aima.utils
import aima.logic
# The main entry point for this module
import os
""" 
    The program takes all the rules from rules.txt, add some knowledge base and test whether if there is any wife relation inferred from the rules
"""
# PATH = 'datasets'


def main():
    # Create an array to hold clauses
    clauses = []

    # Reading all rules in
    with open(f'datasets/rules.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip(('\n'))
            # print(type(line))
            print(line)
            new_str = aima.utils.expr(line)
            clauses.append(new_str)

    # Create a first-order logic knowledge base (KB) with clauses

    KB = aima.logic.FolKB(clauses)
    # Add rules and facts with tell

    KB.tell(aima.utils.expr("Husband(John,Marry)"))
    KB.tell(aima.utils.expr("Husband(Joe,Many)"))
    KB.tell(aima.utils.expr("daughter(A,B)"))
    KB.tell(aima.utils.expr("daughter(B,C)"))
    KB.tell(aima.utils.expr("plays(John,Guitar)"))

    wife = aima.logic.fol_fc_ask(KB, aima.utils.expr('Wife(x,y)'))
    print('is there any wife relation?')
    print(list(wife))


# Tell python to run main method
if __name__ == "__main__":
    main()
