---
title: Handbook of Kingsoft Automatic Publisher
subtitle: "Version: v0.1"
date: 2018-01-22 14:03:17
categories: others
tags: others
cover: 	icon-handbook.jpeg
author:
	nick: Yi Gu
	link: https://tornadoyi.github.io
---
 
## How to Publish Your Article  
It was so essential and promising to publish your carefully written articles to a beautiful designed website. There are only **two** simple steps that can be uploaded to your articles before you respond.

### Step 1. Prepare the Articles and Assets
For easy editing and aesthetic presentation, we use the [markdown](https://en.wikipedia.org/wiki/Markdown) syntax to edit the content of the article. 
- Prepare the article file with **.md** suffix (example: article.md).
- Create a resource folder If the article contains image or other assets (example: article).
- Make sure that the article file is the same name as the resource folder and is in the same level directory.
- Compress all files into a zip file.
>The contents in zip file may be as below:
> article.zip
> |------article.md
> |------article


### Step 2. Upload for Publishing
As you can expect, uploading is always not a difficult task as long as you have been connected to the network.  We combine publishing and uploading into a single function that makes you feel so easy to publish your own article.
- Open the [publishing website](http://192.168.145.36:8080/job/Article-Publisher/build?).
- Select **Publish** in command option bar.
- Click the **Browse** button and select your zip file and click **Open**
- Click **Build** button to start publishing.


## How to Remove the Articles Published Before
A few steps to remove the article published before as follows:
- Open the [publishing website](http://192.168.145.36:8080/job/Article-Publisher/build?).
- Select **Remove** in command option bar.
- Fill out the **name of article file to be deleted** in the **Article File Name** text box
- Click **Build** button to delete.


## Header of Article
As a standard norm and easy to read, we always expect author to define a very detailed header of the file. This is not only for the convenience of reading, but also for the better presentation.

You could use a pair of three line to describe the header of article, just like as below.
>\---
> HEADER AREA
>\---

The header of the article will determine how the article will be displayed. Therefore fully filling the header of the article as much as possible will help to show it better.

- title: The title of article always show in everywhere.
- subtitle: The subtitle is going to show below the title as abstract.
- date: The contents of latest post side bar will be showed base on date.
- categories: As classification of article, categories is used to fast search. See the trick of multilevel categories for child level classification.
- tags: Only used to fast search.
- cover: Cover is a banner of article.
- author:  author contains 2 properties, one is nick which should be filled by author name, another is link which describe the email of author.

An example of header configuration and display is shown as below:
> \---
> title: Handbook of Kingsoft Automatic Publisher
> subtitle: "Version: v0.1"
> date: 2018-01-22 14:03:17
> categories: others
> tags: others
> cover: 	icon-handbook.jpeg
> author:
> 	nick: Yi Gu
> 	link: https://tornadoyi.github.io
> \---

![example](example.png)



## Attension and Tricks
1. Define array constructor with [yaml](http://yaml.org) format for categories keyword could help to implement multilevel categories.
2. Compressing multiple files together helps to achieve batch publishing.
3. Republishing an article whose name is the same as that of the previous article means that an **update** operation is executed.
4. Use "|" to separate file name filled in article name text box could help to operate batch remove.
5. Please visit the [publishing website](http://192.168.145.36:8080/job/Article-Publisher/build?) in the internal network of kingsoft.
