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
## Graph Transform Tool Experiment

Recently, we've done an experiment about how to using graph transform tool on frozen tensorflow-model. Looking back to the past time, lots of complicated errors have occurred during our test time.Fortunately, we managed to solve them at the end. So we wish our experience may help you.

If you have any question about how to using tensorflow on IOS, you can click here [Using-TensorFlow-On-IOS](https://kingsoft-ai.github.io/2018/01/26/Using-tensorflow-On-IOS/). By the way, you could grasp everything about **Graph Transform tool** here [Git](https://github.com/tensorflow/tensorflow/tree/r1.3/tensorflow/tools/graph_transforms#quantize_nodes)

#### Compared tensorflow-r1.4 with tensorflow-r1.5 version

At the very beginning, we consider whether or not the tensorflow version were affecting the speed of transformed models on ios. Aiming at verifying this improbability，we build this two versions on our Mac-mini.
Then, we took a series of experiments. **Note that when you build your own deep-learning project on ios, you must ensure that your python-environment tensorflow version is the same as your built-on ios tensorflow version**.

#### Experiment results

After browsing all the transform references, we have selected some important parameters	for testing. Since we need to enhance the cpu processing speed on portable devices, the step of optimizing is indispensable. According to the official document, **This recipe removes all of the nodes that aren't called during inference, shrinks expressions that are always constant into single nodes, and optimizes away some multiply operations used during batch normalization by pre-multiplying the weights for convolutions**. When added these parameters for optimizing, your mobile cpu can run as fast as possible. At last, the official document introduces some parameters for shrinking the model size. Concretely, after our test, the model size can compressed to almost 70% smaller than the original model.

Bachmarks are as follow:

|      parameters      |  test1  |  test2  |  test3  |
|:--------------------:|:-------:|:-------:|:-------:|
|        frozen        |   Yes   |   Yes   |   Yes   |
|add_default_attributes|         |   Yes   |   Yes   |
|   fold_batch_norms   |         |   Yes   |   Yes   |
|    fold_constants    |         |   Yes   |   Yes   |
| fold_old_batch_norms |         |   Yes   |   Yes   |
|   quantize_weights   |         |         |   Yes   |
|  strip_unused_nodes  |         |   Yes   |   Yes   |
|     remove_nodes     |         |   Yes   |         |
| tensorflow-r1.4(fps) |    9    |   11    |    11   |
| tensorflow-r1.5(fps) |    9    |  10~11  |  10~11  |