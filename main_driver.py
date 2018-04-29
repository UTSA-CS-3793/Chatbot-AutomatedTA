import sys
import os
from find_context import get_context


options = '''
python main_driver.py [option]
options:
    qs-to-json
        generates a json that jons lstm will take from a text file of questions
    get-topics
        assumes json exists, inputs that into jons lstm
        produces file that's  q,t named "intermediate/questions_and_topics.csv"
    get-context
        assumes topics already generated, scrapes stackoverflow with topic as tag
        gets rid of all code in stackoverflow reponse
        produces q,c in file "intermediate/questions_and_context.csv"
    squadify
        assumes context file exists, puts into squad format with dummy paragraphs and
        dummy answers. makes id's
    get-answers
        assumes the squadified file exists, get's answers from that
        outputs in q, a format
    q-to-a
        basically just does all the above commands in order
'''

def main():
    if len(sys.argv) == 1:
        print("no option entered")
        print(options)
        return
    option = sys.argv[1]
    if option == 'qs-to-json':
        pass
    elif option == 'get-topics':
        pass
    elif option == 'get-context':
        get_context() # doesnt work yet
    elif option == 'squadify':
        pass
    elif option == 'get-answers':
        pass
    elif option == 'q-to-a':
        pass
    else:
        print("invalid option")
        print(options)


if __name__ == "__main__":
    main()
