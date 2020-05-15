neg_offset = -1 #only exists to make the code look more difficult then it is
plus_one = 1 #read above^
different_letters = []#list of all different letters found
num_letters = []#list of how many times each letter occurs
c = False #to make verification below work


while c == False:#check if any non alphabet character exist in it(verification)
    a = input("enter wurdz")#user input
    b = a.replace(" ", "")#removing spaces
    c = b.isalpha()#is it only characters? T or F


def letter_counting(b, neg_offset, plus_one, different_letters, num_letters):#counting and adding letters to lists


    for finding_letters in range(len(b)):#loop for cycling though letters
        current_letter = b[finding_letters]#setting letter to be searched for in the list of letters
        print(current_letter) #just for testing purposes
        
        new_letter = True#putting this here was my main logic error(pretty much only error)

        for search in range(len(different_letters)):#searching list of letters to see if letter occurs
            current_compare = different_letters[search]#setting the letter to be compared to to each one in the list of alrady found letters
            index_apnd_t = different_letters.index(current_compare) #sets index to append to as the pos of current compare letter in already found letters

            if current_letter == current_compare:#if the letter is found in the list then do below
                num_letters[index_apnd_t] = num_letters[index_apnd_t] + plus_one#over complicated counter

                new_letter = False#sets this to well... false

        if new_letter == True:#adds new letter to list of letters found and adds 1 to its total times occuring 
            different_letters.append(current_letter)#adds new f
            num_letters.append(plus_one)

letter_counting(b, neg_offset, plus_one, different_letters, num_letters)

for print_loop in range(len(different_letters)):
    print(different_letters[print_loop],": ", num_letters[print_loop], "\n")





string2 = "afgasdasd"
counter = 0

for i in range(len(string2)):
    ltr = string2[i]
    if ltr == "a":
        counter = counter + 1

print (counter)