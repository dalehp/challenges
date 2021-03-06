from collections import namedtuple
import csv
import os
from typing import List

import tweepy

from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET

DEST_DIR = 'data'
EXT = 'csv'
NUM_TWEETS = 100

Tweet = namedtuple('Tweet', ['id_str', 'created_at', 'text'])


class UserTweets(object):
    def __init__(self, handle: str, max_id: int = None):
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        self._api = tweepy.API(auth)
        self._handle = handle
        self._max_id = max_id
        self.output_file = os.path.join(DEST_DIR, f"{self._handle}.{EXT}")
        self._tweets = list(self._get_tweets())
        self._save_tweets()

    def _get_tweets(self) -> List[Tweet]:
        return (
            Tweet(tweet.id_str, tweet.created_at, tweet.text)
            for tweet in self._api.user_timeline(id=self._handle, max_id=self._max_id)
        )

    def _save_tweets(self):
        with open(self.output_file, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(Tweet._fields)
            writer.writerows(self._tweets)

    def __len__(self):
        return len(self._tweets)

    def __getitem__(self, pos):
        return self._tweets[pos]


if __name__ == "__main__":

    for handle in ('pybites', '_juliansequeira', 'bbelderbos'):
        print('--- {} ---'.format(handle))
        user = UserTweets(handle)
        for tw in user[:5]:
            print(tw)
        print()
