
eng = []
eng = ['idk_e']*40
kor = []
kor = ['idk_k']*40
w_cnt = 0

#단어 입력 & 수정 등
#시험 알고리즘은 짜야됨

while True:
    choose = 'x'
    # Word & Choice Input Sequence
    while True:

        #Choice = 'No' or 'Done': break & goto 'The TEST Code'
        if choose == 'n' or choose == 'N':
            break
        if choose == 'D':
            break

        #Enter Words
        while True:
            #Change the variable(choose)'s value
            if choose == 'a' or choose == 'A':
                choose = 'D'                   # D = Done
            if choose == 'b' or choose == 'B':
                choose = 'e'

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
            if choose == 'D':
                break
            elif choose == 'e':
                pass
            else:
                #Reset variable 'choose'
                choose = 'x'
                #Input: 'choose'
                print("\n'e' is edit, 'a' is add, 'b' is both of them, and 'n' is no.")
                choose = input('\nWould you like to change anything?\nPlease enter your choice(e/a/b/n)\n')

            #If choice is Edit
            if choose == 'e' or choose == 'E':
                while True:
                    for i in range(w_cnt):
                        print('Word#' + str(i+1) + ' : ' + eng[i] + ' - ' + kor[i])
                    edit_num = input('\nEnter edit number: ')
                    eng[int(edit_num) - 1] = input('\nWord#' + str(edit_num) + '\n')
                    kor[int(edit_num) - 1] = input()
                    choose_edit = input('Would you like to edit again? (y/n): ')
                    if choose_edit == 'y' or choose_edit == 'Y':
                        pass
                    elif choose_edit == 'n' or choose_edit == 'N':
                        choose = 'D'
                        break
                    #Error Message
                    else:
                        print("Error: your input is wrong. Please enter 'y' or 'n' again.")
            

            elif choose == 'a' or choose == 'A':
                break
            elif choose == 'b' or choose == 'B':
                break
            elif choose == 'n' or choose == 'N':
                break
            #Error Message
            else:
                print('Error: your input is wrong. Please enter again.')
    
    #The TEST Code
    print('type code here')
    
    #testcode
    for j in range(w_cnt):
        print(str(j+1) + eng[j] + ' : ' + kor[j] + '\n')