"""
Four suspects; one of them is a thief. In interrogation
    John said: I am not the thief.
    Paul said: George is the thief.
    George said: It must be Ringo.
    Ringo said: George is lying.

Among them, three were telling the truth while one was lying.
Could you find out who is the thief?

"""

Suspects = ['John', 'Paul', 'George', 'Ringo']
for thief in Suspects:
    sum = (thief != 'John') + (thief == 'George') + (thief == 'Ringo') + (thief != 'Ringo')
    if sum == 3:
        print("The thief is {}.".format(thief))

    #john - cannot be thief or else paul and george would be lying
    #paul - paul and george would lie
    #george - GEORGE
    #ringo - paul and ringo are lying
