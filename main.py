import time

### USER INTERFACE ###

while True:

    # Prompt user
    print("Enter filepath:")
    filepath = input()

    # Write filepath to 'algorithm.txt' file
    file = open('algorithm.txt', 'w')
    file.write(str(filepath))
    file.close()

    time.sleep(0.75)

    # Read algorithm from 'algorithm.txt' file
    file = open('algorithm.txt', 'r')
    algorithm = file.readline()
    file.close()

    print(algorithm)