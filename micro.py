### Conversion Service ###

while True:

    # Read filepath from 'algorithm.txt' file
    file = open('algorithm.txt', 'r')
    filepath = file.readline()
    file.close()

    # If valid text filepath
    if filepath.endswith('.txt'):

        # Read algorithm from filepath
        file = open(filepath, 'r')
        algorithm = file.readline()
        file.close()

        # Write algorithm to 'algorithm.txt' file
        file = open('algorithm.txt', 'w')
        file.write(str(algorithm))
        file.close()


