while True:
    try:
        x = int(input('Enter a number: '))
        break
    except:
        print('That\'s not a valid number!')
    finally:
        print('\n Attempted input\n')