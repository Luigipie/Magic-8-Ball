import random
magicball2_random = ['it certainly is ' , "So that's it" , 'without any doubt' , 'Yes, for sure', 'you can imagine it',\
                   'from what I see it is so', 'almost surely', 'seems be a good things' , 'yes' , 'The signs point to yes', \
                   'unclear answer, please try again' , 'repeat the question' , 'I better not tell you' , "I can't predict it now" \
                   , 'focus and ask again' , "don't count on it" , 'My answer is No' , 'My source say no',\
                   "the foresight don't look good" , 'very doubtful'] #These are the random answers for the 8 magic ball

print ('any question?')
answer = input ()
if answer == "yes":
    magicball = True
while magicball == True:          #With this will start the loop
    print ('what is the question?')
    answer = input()
    print  (random.choice (magicball2_random))         #With this we can go to choose a random answer of the list
    print ('Do you want continue?')
    answer2 =input ()
    if answer2 == 'no':
        print ("GoodBye and thank you!")
        exit()
