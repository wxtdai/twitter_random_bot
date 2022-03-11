from typing import List
import search_mentions,my_random,parse,reply,exclude_replyed

def main():
    my_mentions:List[dict] = search_mentions.search_my_mentions
    non_replyed_mentions:List[dict] = exclude_replyed(my_mentions)
    for tweet in non_replyed_mentions: #tweet: dict
        parsed_tweet_content:List[str] = parse(tweet["text"])
        reply_content = my_random(parsed_tweet_content)
        reply(tweet, reply_content)


if __name__ == "__main__":
    main()