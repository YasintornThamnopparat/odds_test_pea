import numpy as np
import random
import sys
import time

def sprint(str):
    """ print text slowly
    """
    for c in str + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3./90)

def potter_hat(n_iteration=50) :  
    """ choosing person to each houses(Griffindor, hufflepuff, ravenclaw, slytherin)
    then print result and summary
    
    Parameter
    _________
    n_iteration : int
        number of iterations that want to fill names.
        
    """
    count_dict = {
        'griffindor' : [0,0.25],
        'hufflepuff' : [0,0.25],
        'ravenclaw' : [0,0.25],
        'slytherin' : [0,0.25]
    }

    name_dict = {}
    surname_list = []
    i = 0
    while i < n_iteration :
        name = input('Please tell me your name : ')
        # check for same person
        if name in name_dict.keys() :
            print('You are already choosen by {}. No second chance!!'.format(name_dict[name]))
            print('----------------------------')
        else :
            sprint('Ah, right then.')
            print('.....')
            sprint('Hmm, right.')
            print('.....')
            house = random.choices([name for name in count_dict.keys()], 
                                   [prob[1] for prob in count_dict.values()])[0]

            #I want to random speech krub5555
            rand = np.random.randint(0,100)
            if rand >= 50 and count_dict[house][0] >=1 :
                sprint('Another one to ')
                print('.....')
                sprint(house + '!!!!')
                print('Hahaha')
            else :
                sprint('Okay, {}!'.format(house))
            # update people in house in count_dict
            for key in count_dict.keys() :
                if key == house :
                    count_dict[house][0] += 1
                    
            # fix probability in count_dict
            n_list = [np.exp(n[0]) for n in count_dict.values()]
            update_prob = (np.sum(n_list) - n_list) / np.sum(np.sum(n_list) - n_list)
            
            # update probability to count_dict
            count = 0
            for val in count_dict.values() :
                val[1] = update_prob[count]
                count +=1

            #add person to name_dict
            name_dict[name] = house
            if i < n_iteration-1 :
                print('\n')
            else :
                print('\n')
                print('----------------------------')
                print('Here is summary : ')
                print('----------------------------')
                for key in count_dict.keys() :
                    print(key + ' : ' + str(count_dict[key][0]))
                print('thank you for testing')
            i+=1

potter_hat()
