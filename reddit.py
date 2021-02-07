import praw
import os
import re

class RedditClient(object):

	def __init__(self):
		self.reddit = praw.Reddit(
			client_id=os.environ['REDDIT_CLIENT_ID'],
			client_secret=os.environ['REDDIT_CLIENT_SECRET'],
			user_agent=os.environ['REDDIT_USER_AGENT']
		)
		self.gig_subreddits = [
			'slavelabour',
			'forhire',
			'designjobs',
			'remotejs',
			'hireawriter',
			'jobs4bitcoin',
			'Jobopenings'
		]

	def get_gigs(self):
		gigs = []
		for sub_name in self.gig_subreddits:
			sub = self.reddit.subreddit(sub_name)
			for post in sub.new(limit=10):
				if (self.is_gig(post.title)):
					gigs.append({
						'title': post.title,
						'desc': post.selftext,
						'url': post.url,
						'time': post.created_utc,
						'sub_img': sub.icon_img,
						'sub_name': sub_name


					})
		return sorted(gigs, key=lambda post: post['time'], reverse=True)

	def is_gig(self, title):
		return re.search('\\[task\\]', title, re.IGNORECASE) or \
				re.search('\\[hiring\\]', title, re.IGNORECASE)

		