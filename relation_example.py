# Import libraries
import aima.utils
import aima.logic
# The main entry point for this module


def main():
    # Create an array to hold clauses
    clauses = []
    # Add first-order logic clauses (rules and fact)

    # x is husband of
    clauses.append(aima.utils.expr(
        "(Husband(x,y)) ==> Wife(y,x)"
    ))
    # Create a first-order logic knowledge base (KB) with clauses
    KB = aima.logic.FolKB(clauses)
    # Add rules and facts with tell

    KB.tell(aima.utils.expr("Husband(John,Marry)"))

    wife = KB.ask(aima.utils.expr("Wife(x,y)"))
    # Print answers
    print('is there any wife relation?')
    print(wife)


# Tell python to run main method
if __name__ == "__main__":
    main()
