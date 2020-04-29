# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

#print(email_one)

key_word = 'she'
def one_key_word(censor,email):
    lst = ''
    for i in range(len(censor)):
        if censor[i] == ' ':
            lst += ' '
        elif censor[i].islower():
            lst += 'X'
        elif censor[i].isupper():
            lst += 'X'
    return email.replace(censor,lst)
#print(one_key_word(key_word,email_two))

proprietary_terms = ["she","Helena", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

def list_key_words(list,email):
    for word in list:
        lst = ''
        if word in email:
            for i in range(len(word)):
                if word[i] == ' ':
                    lst += ' '
                else:
                    lst += 'X'
        email = email.replace(word,lst)
    return email
#print(list_key_words(proprietary_terms,email_two))

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "Horribly", "questionable"]
punctuation = [",", "!", "?", ".", "%", "/", "(", ")"]

list = proprietary_terms + negative_words


#Any fouling language that occur only once
def censoring(swear,censor,email):
    for word in swear:
        lst = ''
        #just once
        if word in email:
            for i in range(len(word)):
                if word[i] == ' ':
                    lst += ' '
                else:
                    lst += 'X'
        email_edited = email.replace(word,lst)    
    email_finish=list_key_words(censor,email_edited)
    return email_finish
#print(censoring(negative_words,proprietary_terms,email_three))


#Any fouling language that occur more than two times 
def censoring_2_times(swear,censor,email):
    for word in swear:
        lst = ''
        if word in email:
            for i in range(len(word)):
                if word[i] == ' ':
                    lst += ' '
                else:
                    lst += 'X'
        email_edited = email.replace(word,lst)    
    count = 0
    for word in censor:
        if word in email_edited:
            count+=1
        if count >2:
            email_finish=list_key_words(censor,email_edited)
    return email_finish
#print(censoring_2_times(negative_words,proprietary_terms,email_three))

#Any fouling language that occur more than two times  + initial & we
def full_censoring(email,censored_list,negative_words):
    input_text_words = []
    for x in email.split(" "):
        x1 = x.split("\n")
        for word in x1:
            input_text_words.append(word)
    for i in range(0,len(input_text_words)):
        if (input_text_words[i] in censored_list) == True: 
            word_clean = input_text_words[i]
            censored_word = " "
            for i in range(0,len(word_clean)):
                if censored_word == " ":
                    censored_word += " "
                else:
                    censored_word = censored_word + "X"
            input_text_words[i] = input_text_words[i].replace(word_clean,censored_word)
        count = 0
        if (input_text_words[i] in negative_words) == True:
            count += 1
            if count > 2:
                word_clean = input_text_words[i]
                censored_word = " "
                for j in range(0,len(word_clean)):
                    if censored_word == " ":
                        censored_word +=  " "
                else:
                    censored_word = censored_word + "X"
                input_text_words[i].input_text_words[i].replace(word_clean,censored_word)
    return ' '.join(input_text_words)

#full_censoring(email_three,proprietary_terms,negative_words)
#print(full_censoring(email_three,proprietary_terms,negative_words))



#Any fouling language + any word before and after taking into account any punctuation
def basta(email,censored_list):
    input_text_words = []
    for x in email.split(" "):
        x1 = x.split("\n")
        for word in x1:
            input_text_words.append(word)
    for i in range(0,len(input_text_words)):
        check_word =input_text_words[i].lower()
        for x in punctuation:
            check_word = check_word.strip(x) 
        if check_word in censored_list:
        
        #finding the keyword
            word_clean = input_text_words[i]
            censored_word = " "
            for j in range(0,len(word_clean)):
                if censored_word == " ":
                    censored_word += " "
                else:
                    censored_word += "X"
            input_text_words[i] = input_text_words[i].replace(word_clean,censored_word)

        #finding the word before keyword 
            word_clean_before = input_text_words[i-1]
            censored_word_before = ""
            for j in range(0,len(word_clean)):
                if censored_word_before == " ":
                    censored_word_before+= " "
                else:
                    censored_word_before += "X"
            input_text_words[i-1] = input_text_words[i-1].replace(word_clean_before,censored_word_before)
        
        #finding the word after keyword 
            word_clean_after = input_text_words[i+1]
            censored_word_after = " "
            for j in range(0,len(word_clean)):
                if censored_word_after == " ":
                    censored_word_after += " "
                else:
                    censored_word_after += "X"
            input_text_words[i+1] = input_text_words[i+1].replace(word_clean_after,censored_word_after)
    return ' '.join(input_text_words)
basta(email_four,list)
print('basta rhymes    ' + basta(email_four,list))

