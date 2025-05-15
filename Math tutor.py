def math_tutor():   
    import random
    while True:
        numofq = input('How many questions do you want to answer? ')
        if numofq.isdigit():
            numofq = int(numofq)
            if numofq > 0:
                break
            else: 
                print('Number of questions must be greater than zero.')
        else:
            print('Invalid input. Please enter a number.')
    while True:
        max_val = input('How high should the numbers go? ')
        if max_val.isdigit():
            max_val = int(max_val)
            break
        else:
            print('Invalid input. Please enter a number.')
    score = 0
    question_list = []
    for _ in range(numofq):
        a = random.randrange(1,max_val+1)
        b = random.randrange(1,max_val+1)
        try:
            answer = int(input(f'{a} x {b} = '))
        except ValueError:
             print ('Invalid input. Please enter a number for your answer.')
             if _ < numofq - 1: 
                 print('Continuing to the next question.')
             continue
        correct_answer = a * b
        question_list.append(f'{a} x {b} = {correct_answer}')
        if answer == correct_answer:
            score += 1
    percentscore = round((score / numofq) * 100)
    question_list = ', '.join(question_list)

    return (f'Thank you for playing. You have got {score} out of {numofq} questions correct. Your score is {percentscore}%. Here are all the questions with the correct answer: {question_list}')

print(math_tutor())
