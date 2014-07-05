import sys
import json

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {} # initialize an empty dictionary
    for line in sent_file:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
   
    for line in tweet_file:
      tweet = json.loads(line)
      text = tweet.get(unicode("text"),"")
      words = text.split()
      score = 0
      for word in words: 
        score = score + scores.get(word, 0)
      print score

if __name__ == '__main__':
    main()
