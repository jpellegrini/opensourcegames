"""
Converts the source releases of D-Fend Reloaded to a Git.
"""

import sys
import datetime
import re
from utils.utils import *


def subprocess_run(cmd):
    """

    """
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode:
        print("error {} in call {}".format(result.returncode, cmd))
        print(result.stderr.decode('ascii'))
        sys.exit(-1)
    else:
        print('  output: {}'.format(result.stdout.decode('ascii')))

def single_release(zip):
    """

    """

    # get version
    matches = version_regex.findall(zip)
    version = matches[0]
    print(' version {}'.format(version))
    ftp_link = 'https://sourceforge.net/projects/dfendreloaded/files/D-Fend%20Reloaded/D-Fend%20Reloaded%20{}/'.format(version)

    # clear git path without deleting '.git'
    for item in os.listdir(git_path):
        # ignore '.git
        if item == '.git':
            continue
        item = os.path.join(git_path, item)
        if os.path.isdir(item):
            shutil.rmtree(item)
        else:
            os.remove(item)

    # unpack zip to git path
    # with zipfile.ZipFile(os.path.join(source_releases_path, zip), 'r') as zipf:
    #    zipf.extractall(git_path)
    unzip(os.path.join(source_releases_path, zip), git_path)

    # get date from the files (latest of last modified)
    latest_last_modified = 0
    for dirpath, dirnames, filenames in os.walk(git_path):
        if dirpath.startswith(os.path.join(git_path, '.git')):
            # not in '.git'
            continue
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            lastmodified = os.path.getmtime(filepath)
            if lastmodified > latest_last_modified:
                latest_last_modified = lastmodified
                # print('{}, {}'.format(filepath, datetime.datetime.fromtimestamp(latest_last_modified).strftime('%Y-%m-%d')))

    original_date = datetime.datetime.fromtimestamp(latest_last_modified).strftime('%Y-%m-%d')
    print(' last modified: {}'.format(original_date))

    # update the git index (add unstaged, remove deleted, ...)
    print('git add')
    os.chdir(git_path)
    subprocess_run(['git', 'add', '--all'])

    # perform the commit
    print('git commit')
    os.chdir(git_path)
    message = 'version {} from {} ({})'.format(version, original_date, ftp_link)
    print('  message "{}"'.format(message))
    subprocess_run(['git', 'commit', '--message={}'.format(message), '--author={}'.format(author), '--date={}'.format(original_date)])


if __name__ == "__main__":

    # general properties
    author = 'alexanderherzog <alexanderherzog@users.sourceforge.net>'
    version_regex = re.compile(r"Reloaded-(.*)-", re.MULTILINE)

    # get paths
    source_releases_path = sys.argv[1]
    git_path = os.path.join(source_releases_path, 'git')

    # recreate git path
    recreate_directory(git_path)
    os.chdir(git_path)
    subprocess_run('git init')

    # get all files in the source releases path and sort them
    zips = os.listdir(source_releases_path)
    zips = [file for file in zips if os.path.isfile(os.path.join(source_releases_path, file))]
    print('found {} source releases'.format(len(zips)))
    zips.sort()

    # iterate over them and do revisions
    for counter, zip in enumerate(zips):
        print('{}/{}'.format(counter, len(zips)))
        single_release(zip)