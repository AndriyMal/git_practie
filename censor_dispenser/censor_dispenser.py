# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

#print(email_one)


def censor_all_instances(email):
    var1 = 'learning'
    var2 = 'algorithms'
    var3 = var1 +" "+ var2  
    txt = email.find(var3)
    if txt !=-1:
        return True
    else:
        return False
  
print(censor_all_instances(email_three))

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
def censor_all_phrases(email):
  for i in range(len(proprietary_terms)):
    txt = email.find(proprietary_terms[i])
    if txt !=-1:
        return True
    else:
        return False
print(censor_all_phrases(email_three))