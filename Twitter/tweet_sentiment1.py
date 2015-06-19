import sys,json

#def hw():
    #print 'Hello, world!'

#def lines(fp):
   # print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
#    hw()
#    lines(sent_file)
#    lines(tweet_file)
    #afinnfile = open("AFINN-111.txt")
    afinnfile=sent_file
    data = []                                   #Define an empty dict to store the tweets
    for line in tweet_file:
        data.append(json.loads(line))
    
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    #print scores.items() # Print every (term, score) pair in the dictionary
    for i in range(len(data)):
        tweet=data[i]
        if len(tweet)>1:
            tweet_word = data[i]["text"].split()    
            score = 0
            for word in tweet_word:
                if word.encode('utf-8') in scores.keys():       #Look up each token in the scores dict  
                    score = score + float(scores[word])         #If the term matches, assign the term score and calculate the total score of each tweet 
                else:
                    score = score
            print(score)
		

if __name__ == '__main__':
    main()
