# define function to cut down on repetition 
def produce_summary(filename):
    #open  file
    produce_day_summary = open(filename)
    #gather input from user on day of produce summary
    produce_summary_day = input("Day: ")
    #iterate through each line of the file and split indexes apart "|" characteer 0 | 1 | 2
    for line in produce_day_summary:
        line = line.rstrip()
        words = line.split('|')
    #change indexes so that they reflect what is in files um-deliveries melon | count | amount
        melon = words[0]
        count = words[1]
        amount = words[2]
    #print f-string with the indexes values taken from file... 
        print(f'On day {produce_summary_day} Delivered {count} {melon}s for total of ${amount}')
    produce_day_summary.close()

