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
    new_terms = {}  
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
#            print(score)
            for word in tweet_word:
                if word.encode('utf-8') not in scores.keys():		#Look up each token which is not present in the scores dict
                    n_w_score = float(score)						#Define a variable that would contain the tweet score
                    if word.encode('utf-8') in new_terms.keys():		#Check whether the term is present in the new_terms dict
                        new_terms[word.encode('utf-8')] = new_terms[word.encode('utf-8')] + n_w_score		
                    else:
                        new_terms[word.encode('utf-8')] = n_w_score                  
    for w in new_terms:
        print w, new_terms[w]								#Print the new terms and their scores

if __name__ == '__main__':
    main()
