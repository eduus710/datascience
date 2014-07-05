import sys
import json

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {} # initialize an empty dictionary
    for line in sent_file:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
   
    states = {}

    for line in tweet_file:
      tweet = json.loads(line)
      if not "place" in tweet:
        continue
      if tweet["place"] is None:
        continue
      place = tweet["place"]
      if not "country_code" in place:
        continue
      if not place["country_code"] == "US":
        continue
      if not "place_type" in place:
        continue
      if not place["place_type"] == "city":
        continue
      if not "full_name" in place:
        continue
      city, state = place["full_name"].split(", ");

      text = tweet.get("text","")
      words = text.split()
      score = 0
      for word in words: 
        score = score + scores.get(word, 0)
      statescore = states.get(state, [0,0])
      statescore[0] = statescore[0] + 1.0
      statescore[1] = statescore[1] + score
      states[state] = statescore

    happiest = "NY";
 
    for state in states.keys():
      current = states[state][1]/states[state][0]
      best = states[happiest][1]/states[happiest][0]
      if current > best:
        happiest = state

    print happiest

if __name__ == '__main__':
    main()
