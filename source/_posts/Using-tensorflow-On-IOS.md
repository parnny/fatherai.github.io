
---
title: Using TensorFlow On IOS
subtitle: "Version: v0.1"
date: 2018-01-26 15:43:36
categories: others
tags: tensorflow-for-ios
author:
nick: tongyao Bai
link: https://C-ID.github.io
---

## Using TensorFlow On IOS

Welcome to KingSoft AILab! In this article,we'll walk through getting TensorFlow, Google's machine learning library, set up to perform inference directly on an iOS device.

#### Installing TensorFlow 1.3 on IOS

The binary distribution of TensorFlow for macOS does not include the IOS static library or some of the scripts we'll need, so we'll have to build both ourselves in a later section. Since it helps if the version of the iOS library is the same as the version of TensorFlow installed on our system, we'll re-install the latest version of TensorFlow from source (even if it's already installed). This can save us some headaches down the road.

DownLoad TensorFlow here: [TensorFlow](https://github.com/tensorflow/tensorflow)

If you have installed [Git](https://git-scm.com),you can simply run:
```bash
  $ git clone https://github.com/tensorflow/tensorflow.git
```

#### Building Tensorflow on IOS
Note that tensorflow is built using a tool called bazel, and bazel requires some packages. if you have not installed, there is a easy way using Homebrew:
```bash
$ brew install bazel
$ brew install automake
$ brew install libtool
$ brew install autoconf
```
From our directory of TensorFlow 1.3 sources, we can simply run:
  Make sure that your tensorflow version is 1.3 , we can simply run the following command in your terminal in tensorflow's directory:
```bash
  $ git branch -a
```
  if your tensorflow version is not 1.3,then run the following command to checkout:
```bash
  $ git checkout r1.3
```
Before building tensorflow on IOS，you will need to download all dependencies as well. It provided a script that does so, to be run (as with all commands) **at the root of your tensorflow**:

```bash
$ tensorflow/contrib/makefile/download_dependencies.sh
```

For more information you can click here [Readme](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/makefile)


To get the libraries compiled,you must install xcode(version >7.3),you can install xcode from App Store.
Then,you can run this from the root of your TensorFlow source folder:

```bash
$ tensorflow/contrib/makefile/build_all_ios.sh
```

Running build_all_ios.sh will generate a TensorFlow static library in the tensorflow/contrib/makefile/gen/lib subdirectory. This library is compiled for ARMv7, ARM64, and x86 architectures, so you can use it in both the iOS simulator and on iOS hardware.

#### Setting up xcode project

Create a new xcode test project,then,we have to tell the iOS target about the TensorFlow static library we built for IOS (and the protocol buffer library is relies on). To do this, copy the following static library to your xcode test project .We can run the command to copy:

```bash
$ cp YOUR_TENSORFLOW_SOURCE_DIR/tensorflow/tensorflow/contrib/makefile/gen/lib/libtensorflow-core.a YOUR_XCODE_PROJECT_DIR/
$ cp YOUR_TENSORFLOW_SOURCE_DIR/tensorflow/tensorflow/contrib/makefile/gen/protobuf_ios/lib/libprotobuf-lite.a YOUR_XCODE_PROJECT_DIR/
$ cp YOUR_TENSORFLOW_SOURCE_DIR/tensorflow/tensorflow/contrib/makefile/gen/protobuf_ios/lib/libprotobuf.a YOUR_XCODE_PROJECT_DIR/
```

After that,we should add the tensorflow static library to xcode project.Open your xcode project you have created,right-click the project name,select >"Add Files to YOUR_PROJECT_NAME",you will see libtensorflow-core.a,libprobuf-lite.a,libprotobuf.a in your pages,then add them. You can checkout whether or not you have add the static library sucessfully by selecting xcode menu:'Building Phases -> Link Binary with Libraries'. Finally, add the "Accelerate.framework" static library to ensure your tensorflow-program running fine.


Then add select xcode "Building Setting" menu,add **$(PROJECT_DIR)/YOUR_PROJECT_NAME** to Library Search Paths.Here replace *YOUR_PROJECT_NAME* to your project name. We'll also add the following flags to Other Linker Flags:

**-force_load**
**$(PROJECT_DIR)/YOUR_PROJECT_NAME/libtensorflow-core.a**
**$(PROJECT_DIR)/YOUR_PROJECT_NAME/libprotobuf-lite.a**
**$(PROJECT_DIR)/YOUR_PROJECT_NAME/libprotobuf.a**

Next, we add the following to Header Search Paths.

**YOUR_TENSORFLOW_SOURCE_FOLDER/tensorflow**
**YOUR_TENSORFLOW_SOURCE_FOLDER/tensorflow/contrib/makefile/gen/proto**
**YOUR_TENSORFLOW_SOURCE_FOLDER/tensorflow/contrib/makefile/downloads**
**YOUR_TENSORFLOW_SOURCE_FOLDER/tensorflow/contrib/makefile/downloads/protobuf/src**
**YOUR_TENSORFLOW_SOURCE_FOLDER/tensorflow/contrib/makefile/downloads/eigen**

Now that the xcode project is set up, we'll load up our model and perform inference on the test datesets.
