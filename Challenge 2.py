#Muhammad Hakeem Adli Bin Abdul Rahim (1817151)

def accepts(transitions,initial,final_state,s):
    state = initial
    for c in s:
        state = transitions[state][c]
    return state in final_state

DFA = {0:{'F':1,'T':5},
        1:{'F':2,'T':5},
        2:{'F':3,'T':5},
        3:{'F':5,'T':4},
        4:{'F':5,'T':4},
        5:{'F':5,'T':5}}

def TestDFA(s):
    return accepts(DFA,0,{4},s)

def main():

    s = input("Enter Input: ")

    if  TestDFA(s) == True:
        print("System Disarmed/ Accepted user access! ")
    else:
        print("System Access Blocked and Alarm activated! ")

main()