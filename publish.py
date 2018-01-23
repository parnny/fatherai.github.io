import os
import argparse
import zipfile
import shutil


def find_all_articles(hexo_path):
    articles = []
    article_path = os.path.join(hexo_path, 'source', '_posts')
    for fn in os.listdir(article_path):
        fp = os.path.join(article_path, fn)
        ext = os.path.splitext(fp)[-1]
        if not os.path.isfile(fp) or ext is not '.md': continue
        articles.append(fp)
    return articles



def git_commit_and_push(git_path):
    os.system('cd {}'.format(git_path))
    os.system('git add ./')
    os.system('git add ./')



def publish(hexo_path, article_zip_path):
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
        shutil.rmtree(old_asset_path)
        shutil.rmtree(old_article_path)


    # copy new articles
    for i in range(len(names)):
        name = names[i]
        md_path = md_paths[i]
        asset_path = asset_paths[i]

        shutil.copy(md_path, os.path.join(article_path, os.path.basename(md_path)))
        shutil.copytree(asset_path, os.path.join(article_path, name), True)







if __name__ == '__main__':
    # parse args
    def str2bool(v): return v.lower() in ("yes", "true", "t", "1", True)
    parser = argparse.ArgumentParser(description="Run commands")
    parser.add_argument('command', choices=['publish', 'remove'], help='please choose action')
    parser.add_argument('--hexo', type=str, required=True, help='hexo project path')
    parser.add_argument('--article', type=str, required=True, help='new article file path for publish or a name for remove')
    args = parser.parse_args()

    csv_paths = [os.path.realpath(p) for p in args.csv]
    output_path = os.path.realpath(args.output_path)
