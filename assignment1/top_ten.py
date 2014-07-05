import sys
import json

def main():
    tweet_file = open(sys.argv[1])

    hashtags = {} 
    for line in tweet_file:
      tweet = json.loads(line)
      if not "entities" in tweet.keys():
        continue
      entities = tweet["entities"]
      if not "hashtags" in entities.keys():
        continue
      for hashtag in entities["hashtags"]:
        httext = hashtag["text"]
        hashtags[httext] = hashtags.get(httext,0) + 1

    count = 0
    for tag in sorted(hashtags.items(), key=lambda x:x[1], reverse=True):
      print tag[0], tag[1]
      count = count + 1
      if count == 10:
        break

if __name__ == '__main__':
    main()
