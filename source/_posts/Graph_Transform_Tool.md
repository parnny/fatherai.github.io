---
title: Graph Transform Tool Experiment
subtitle: Evaluate graph transform tool performance
date: 2018-02-01 15:23:53
categories:
  - machine learning
  - tensorflow
tags:
  - tensorflow
  - machine learning
  - ios
author:
  nick: Tongyao Bai
  link: https://github.com/C-ID
---
##Graph Transform Tool Experiment

Recently, we've done an experiment about how to using graph transform tool on frozen tensorflow-model. Looking back to the past time, there are a lot of misunderstanding errors occurred during our test time.Fortunately, we solved it at the end. So we wish our experience may helping your for your job.

If you have any question about how to using tensorflow on IOS, you can click here [Using-TensorFlow-On-IOS](https://kingsoft-ai.github.io/2018/01/26/Using-tensorflow-On-IOS/). By the way, you could grasp everything about **Graph Transform tool** here [Git](https://github.com/tensorflow/tensorflow/tree/r1.3/tensorflow/tools/graph_transforms#quantize_nodes)

####Compared tensorflow-r1.4 with tensorflow-r1.5 version

At the very beginning, we consider whether the tensorflow version affecting the speed of transformed model on ios or not. Aim at verifying this improbability，we build this two versions on our Mac-mini.
Then, a series of experiments began to work. **Note that when you start up your own deep-learning project on ios, you must keep your python environment installed tensorflow version and your built on ios tensorflow version of the same**.

####Experiment results about Part of those transform reference 

After browsing both of these transform reference, we selected some important parameters	for test. Since we need to enhance mobel cpu processing speed, the step of optimizing is indispensable.	According to the official document, **This recipe removes all of the nodes that aren't called during inference, shrinks expressions that are always constant into single nodes, and optimizes away some multiply operations used during batch normalization by pre-multiplying the weights for convolutions**. When added these parameters for optimizing, your mobel cpu can run as fast as possible. At last, the official document introduce some parameters for shrinking the model size. Concretely, after our test, the model size can compressed which almost 70% smaller than the original model.

bachmark are as follow:


|frozen|add_default_attributes|fold_batch_norms|fold_constants|fold_old_batch_norms|quantize_weights|sort_by_execution_order|strip_unused_nodes|remove_nodes|tensorflow-r1.4(fps)|tensorflow-r1.5(fps)|
|:----:|:--------------------:|:--------------:|:------------:|:------------------:|:--------------:|:---------------------:|:----------------:|:----------:|:------------------:|:------------------:|
|  Yes |                      |                |              |                    |                |                       |                  |            |          9         |         9          |
|  Yes |          Yes         |      Yes       |      Yes     |         Yes        |                |                       |       Yes        |     Yes    |          11        |         10~11      |
|  Yes |          Yes         |      Yes       |      Yes     |         Yes        |       Yes      |                       |       Yes        |            |          11        |         10~11      |
