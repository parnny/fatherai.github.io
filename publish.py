import os
import argparse
import zipfile
import shutil
from git import Repo


def find_all_articles(hexo_path):
    articles = []
    article_path = os.path.join(hexo_path, 'source', '_posts')
    for fn in os.listdir(article_path):
        fp = os.path.join(article_path, fn)
        ext = os.path.splitext(fp)[-1]
        if not os.path.isfile(fp) or ext is not '.md': continue
        articles.append(fp)
    return articles



def git_commit_and_push(git_path, log):
    repo = Repo(git_path)
    index = repo.index
    remote = repo.remote()

    # add untracked_files
    index.add(repo.untracked_files)

    # commit
    repo.git.commit('-a', '-m', '\"{}\"'.format(log))

    # push
    remote.push()




def publish(hexo_path, article_zip_path, log):
    # check
    if not os.path.isfile(article_zip_path):
        raise Exception('Can not found zip file {}'.format(article_zip_path))

    article_path = os.path.join(hexo_path, 'source', '_posts')

    # extract files
    zip_file = zipfile.ZipFile(article_zip_path)
    extract_path = os.path.splitext(article_zip_path)[0] + '.extract'
    zip_file.extractall(extract_path)
    zip_file.close()

    # find all md and assets
    names = []
    md_paths = []
    asset_paths = []
    for root, dirs, files in os.walk(extract_path):
        for filename in files:
            # check
            name, ext = os.path.splitext(filename)
            if ext != '.md': continue

            # find article
            names.append(name)

            # find md
            md_paths.append(os.path.join(root, filename))

            # find asset of md
            asset_path = os.path.join(root, name)
            if not os.path.isdir(asset_path): asset_path = None
            asset_paths.append(asset_path)


    # clean old articles
    for name in names:
        old_asset_path = os.path.join(article_path, name)
        old_article_path = old_asset_path + '.md'
        if os.path.isdir(old_asset_path): shutil.rmtree(old_asset_path)
        if os.path.isfile(old_asset_path): os.remove(old_article_path)


    # copy new articles
    for i in range(len(names)):
        name = names[i]
        md_path = md_paths[i]
        asset_path = asset_paths[i]

        shutil.copy(md_path, os.path.join(article_path, os.path.basename(md_path)))
        if asset_path is not None: shutil.copytree(asset_path, os.path.join(article_path, name), True)


    # commit
    git_commit_and_push(hexo_path, log)




def remove(hexo_path, article_name, log, separator):
    article_path = os.path.join(hexo_path, 'source', '_posts')

    # split article names
    article_names = article_name.split(separator)

    # trim article names
    for i in range(len(article_names)):
        name = article_names[i]
        name = os.path.splitext(name)[0]
        article_names[i] = name.rstrip().lstrip()


    # remove all article
    for name in article_names:
        asset_path = os.path.join(article_path, name)
        md_path = asset_path + '.md'
        if os.path.isdir(asset_path): shutil.rmtree(asset_path)
        if os.path.isfile(md_path): os.remove(md_path)


    # commit
    git_commit_and_push(hexo_path, log)



if __name__ == '__main__':
    # parse args
    def str2bool(v): return v.lower() in ("yes", "true", "t", "1", True)
    parser = argparse.ArgumentParser(description="Run commands")
    parser.add_argument('command', choices=['publish', 'remove'], help='please choose action')
    parser.add_argument('--hexo', type=str, required=True, help='hexo project path')
    parser.add_argument('--article', type=str, required=True, help='new article file path for publish or a name for remove')
    parser.add_argument('--log', type=str, default='automatic commit by publish', help='a log for commit')
    parser.add_argument('--separator', type=str, default='|', help='a separator for process array string')
    args = parser.parse_args()

    if args.command.lower() == 'publish':
        publish(args.hexo, args.article, args.log)

    elif args.command.lower() == 'remove':
        remove(args.hexo, args.article, args.log, args.separator)

    else:
        raise Exception('invalid command {}'.format(args.command))
