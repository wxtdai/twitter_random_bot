import json
from typing import List
from search_mentions import search_my_mentions
from exclude_replyed import exclude_replyed
from parse import parse
from my_random import my_random
from reply import reply
from add_header_text import add_header_text
from logging import getLogger, StreamHandler, DEBUG


def main():
    logger = getLogger(__name__)
    handler = StreamHandler()
    handler.setLevel(DEBUG)
    logger.setLevel(DEBUG)
    logger.addHandler(handler)
    logger.propagate = False

    my_mentions: List[dict] = search_my_mentions()
    logger.debug("my_mentions is below:")
    logger.debug(json.dumps(my_mentions, indent=4, sort_keys=True, ensure_ascii=False))

    non_replyed_mentions: List[dict] = exclude_replyed(my_mentions)
    logger.debug("non_replyed_mention is below:")
    logger.debug(json.dumps(non_replyed_mentions, indent=4, sort_keys=True, ensure_ascii=False))

    for tweet in non_replyed_mentions: #tweet: dict
        parsed_tweet_contents:List[str] = parse(tweet["text"])
        main_context:str = my_random(parsed_tweet_contents)
        reply_content:str = add_header_text(main_context)
        reply(tweet, reply_content)
        logger.debug(tweet)
        logger.debug(reply_content)


if __name__ == "__main__":
    main()

