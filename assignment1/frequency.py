import sys
import json

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])

    terms = {} 
    total = 0.0

    for line in tweet_file:
      tweet = json.loads(line)
      text = tweet.get(unicode("text"),"")
      words = text.split()
      for word in words: 
        total = total + 1
        terms[word] = terms.get(word, 0) + 1

    for term in terms.keys():
      print term, terms[term] / total

if __name__ == '__main__':
    main()
