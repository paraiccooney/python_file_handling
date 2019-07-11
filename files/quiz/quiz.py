def show_menu():
    print("1. Ask question")
    print("2. Add a questions")
    print("3. Exit Game")
    
    option = input("Enter option: ")
    return option

def add_question():
    print("")
    question = input("Enter a question\n> ")
    
    print("")
    print("OK then, tell me the answer")
    answer= input("{0}\n> ".format(question))
    
    file= open("questions.txt", "a")
    file.write(question + "\n")
    file.write(answer + "\n")
    file.close()

def ask_questions():
    questions=[]
    answers = []
    
    #the with block is similar to opening a file with the open method but it takes care of a number of things for us including closing the file at the end
    with open("questions.txt", "r") as file:
        lines= file.read().splitlines()
    
    # the enumerate function turns each of these lists in a tuple with a line number for each line (which we represent with i). We represent the text with 'text'
    for i, text in enumerate(lines):
        # when we put these to questions or answers below we're not writing them to a file but storing them in memory
        if i%2 == 0:
            questions.append(text)
        else:
            answers.append(text)
    
    number_of_questions = len(questions)
    # the zip function adds the two together in memory. The result is [("question...", "answer...")] for each
    questions_and_answers = zip(questions, answers)
    
    score = 0
    
   
    for question, answer in questions_and_answers:
        guess = input(question + "> ")
        if guess == answer:
            score += 1
            print("right!")
            print(score)
        else:
            print("wrong!")
    
    print("You got {0} correct out of {1}".format(score, number_of_questions))

def game_loop():
    while True:
        option = show_menu()
        if option == "1":
            ask_questions()
        elif option == "2":
            add_question()
        elif option == '3':
            break
        else:
            print("Invalid option")
        print("")
        
game_loop()
