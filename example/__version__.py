'''
A file to store the application version. Used by the /health endpoint.
Using git python, get the git hash of the repository from the HEAD.
'''
VERSION = (0, 0, 0)
try:
     __version__ = '.'.join(map(str, VERSION))
except:
    __version__ = 'application version unavailable'

try:
    import git
    repo = git.Repo(search_parent_directories=True)
    __git_hash__ = repo.head.object.hexsha
except:
    __git_hash__ = 'git hash unavailable'
