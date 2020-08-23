groclist = []
while True :
    # Ask what they want to do about the grocery list 
    action = input('What would you like to do concerning your grocery list?\n(ADD, REMOVE, PRINT, STOP)\n')
    # take action (add remove or print or stop)
    if action.upper() == 'ADD':
        item = input('What would you like to do add ?\n')
        groclist.append(item)
    elif action.upper() == 'REMOVE':
        item = input('What would you like to do remove?\n')
        groclist.remove(item)
    elif action.upper() == 'PRINT':
        print(groclist)
    elif action.upper() == 'STOP':
        print('Stopping the program.')
        break
    else:
        print('Incorrect input. Exiting.')
        break 
    # stop when stop add
