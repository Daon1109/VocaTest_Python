#VocaTest_PythonApplication
#PYTHON RULES!!!
eng = []
eng = ['no_input_eng']*100
kor = []
kor = ['no_input_kor']*100
a_answer = []
a_answer = ['idk_answer']*100
t_answer = []
t_answer = ['idk_answer']*100
w_cnt = 0
record_endless = 'Before'
input_key = True

#
#TO-DO: Adding Clear-Screen Mode & Writing User Guide(WEB/text)
#Additional Feature(need to code): clear-screen mode
'''
    #ClearScreen code - this should be programmed logically(flowchart first)
    import os
    os.system('cls')
'''

# LOOP: Main Code - It doesn't break if endless mode is enabled
while True:
    #Reset variable 'choose'
    choose = 'x'

    # LOOP: Word & Choice Input Sequence
    while True:

        #Choice = 'No' or 'Done': break & goto 'The TEST Algorithm'
        if choose == 'n' or choose == 'N':
            break
        elif choose == 'D':
            break

        #execute code by input_key
        if input_key:
            # LOOP: Change variable(choose) & Enter Words
            print("\nEnter the words you want to memorize.\nTo stop, type 'ESC'.")
            while True:

                #Change the variable(choose)'s value
                if choose == 'a' or choose == 'A':
                    choose = 'D'                   # D = Done
                elif choose == 'b' or choose == 'B':
                    choose = 'e'                   #After the Word input Sequence, directly go to Edit Sequence

                #Input: Words
                eng[w_cnt] = input('\nWord#' + str(w_cnt + 1) + '\n')
                if eng[w_cnt] == 'esc' or eng[w_cnt] == 'ESC':      #Break when esc entered
                    break
                kor[w_cnt] = input()
                if kor[w_cnt] == 'esc' or kor[w_cnt] == 'ESC':      #Break when esc entered
                    break
                w_cnt = w_cnt + 1


        #Enter Choice (Edit/Add/Both/Not)
        while True:

            #1st Conditional Statement: Check variable
            if choose == 'D':
                break
            elif choose == 'e':
                pass
            else:
                #Reset variable 'choose'
                choose = 'x'
                #Input: 'choose'
                print("\n'e' is edit, 'a' is add, 'b' is both of them, and 'n' is no.")
                choose = input('\nWould you like to change anything?\nEnter your choice(e/a/b/n)\n')

            #2nd Conditional Statement: execute by commend(e/a/b/n)
            #Edit Sequence
            if choose == 'e' or choose == 'E':
                while True:
                    for e in range(w_cnt):
                        print('Word#' + str(e+1) + ' : ' + eng[e] + ' - ' + kor[e])
                    edit_num = input('\nEnter edit number: ')
                    eng[int(edit_num) - 1] = input('\nWord#' + str(edit_num) + '\n')
                    kor[int(edit_num) - 1] = input()
                    choose_edit = input('Would you like to edit again? (y/n): ')
                    if choose_edit == 'y' or choose_edit == 'Y':
                        pass
                    elif choose_edit == 'n' or choose_edit == 'N':
                        choose = 'D'        #because it's conditional statement, it directly goes up to LOOP 'Enter Choice'
                        break
                    #Error Message
                    else:
                        print("Error: your input is wrong. Please enter 'y' or 'n' again.")
                input_key = False
            #the others
            elif choose == 'a' or choose == 'A':
                input_key = True
                break
            elif choose == 'b' or choose == 'B':
                input_key = True
                break
            elif choose == 'n' or choose == 'N':
                input_key = False
                break
            #Error Message
            else:
                print('Error: your input is wrong. Please enter again.')
    
    #The TEST Algorithm (Independent)
    while True:

        #Choose Mode
        print("\n'a' is open-answer mode, and 't' is real test mode")
        choose_test = input('\nEnter your choice(a/t)\n')

        #Reset Answer
        a_answer = ['idk_answer']*100
        t_answer = ['idk_answer']*100

        # A : Open-Answer Mode
        if choose_test == 'a' or choose_test == 'A':
            print('\nOpen-Answer Mode: Enter the right answer')
            #Ping-pong Algorithm: Input answer & Output variale 'kor[]'(Answer)
            for a in range(w_cnt):
                a_answer[a] = input('\n' + eng[a] + ' : ')
                if a_answer[a] == kor[a]:           #Correct Answer 
                    print('\nCorrect!\nAnswer: ' + kor[a])
                else:                               #Wrong Answer 
                    print('\nWrong!\nAnswer: ' + kor[a])
            input_key = False
            break

        # T : Real Test Mode
        elif choose_test == 't' or choose_test == 'T':
            print('\nReal Test Mode: Enter the right answer')
            #Reset Score
            score = 0
            wrong_cnt = 0
            #Input Answer Sequence
            for t in range(w_cnt):
                t_answer[t] = input('\n' + eng[t] + ' : ')
            #Check Answer
            for tCheck in range(w_cnt):
                if t_answer[tCheck] == kor[tCheck]:
                    score = score + 1
            #Output
            print('\n\nScore: ' + str(score) + '/' + str(w_cnt))
            if score == w_cnt:
                print('\nYou got a perfect score!\n')
            for wrongAns in range(w_cnt):
                if t_answer[wrongAns] != kor[wrongAns]:
                    wrong_cnt = wrong_cnt + 1
                    print('Wrong Answer#' + str(wrong_cnt) + ': ' + eng[wrongAns] + ' - ' + t_answer[wrongAns] + ' (Correct Answer: ' + kor[wrongAns] + ')')
            
            input_key = False
            break
        #Error Message
        else:
            print('Error: your input is wrong. Please enter again.')
    
    #Endless Mode
    if record_endless == 'Before':
        while True:
            choose_endless = input('Would you like to start Endless Mode?(y/n)\n')
            if choose_endless == 'n' or choose_endless == 'N':
                break
            elif choose_endless == 'y' or choose_endless == 'Y':
                input_key = False
                record_endless = 'After'
                break
            #Error Message
            else:
                print('Error: your input is wrong. Please enter again.')

    #Break Main Loop
    if choose_endless == 'n' or choose_endless == 'N':
        break

#Credit
print('''
    -VocaTest Program-
    Made by Suho
    GitHub Username: Daon1109
    Last Update: 10/22/2021
''')
