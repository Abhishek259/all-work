import datetime
from git_filter_repo import Commit

def commit_callback(commit: Commit, aux_info: dict):
    # Define the new date as a string
    new_date_str = datetime.datetime(2022, 1, 1, 0, 0, 0).strftime('%a %b %d %H:%M:%S %Y %z')
    # Set both author and committer dates
    commit.author_date = new_date_str
    commit.committer_date = new_date_str

