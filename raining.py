def func1():
        while True:
            raining = input('Is it raining?: ')

            if raining == 'yes':
                A1 = input('Have an umbrella?: ')

                if A1 == 'no':
                    Q1 = 'yes'
                    while Q1 == 'yes':
                        print('Wait a while.')
                        Q1 = input('Is it raining? ')

                    if Q1 == 'no':
                        print('go outside')

                elif A1 == 'yes':
                    print('go outside...')

            elif raining == 'no':
                print('go outside...')
func1()
