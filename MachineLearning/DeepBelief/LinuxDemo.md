Linux Demo for DeepBelef
===

There're many types of platform that **DeepBelef** supports, however, different platfrom has different format, some use
Java, some use C++ or C. And the application as well as the build or make rules are quite different in various platform,
so this seris of document gives a very detailed instructions about how to use in different platform. This file only contains the
content under **Linux**.

##How to begin

There is a demo about Linux classification about an Image, first we need to install the libjpcnn.so in the system, so that
our system can link them when using make or build.

In the folder `LinuxLibrary`, execute the script `install.sh`, it will mv the head file and libs in the system path

Then, in the `exampls/SimpleLInux` folder, this is the source about how to use the API, it will use a pre-trained model jpcnn
to predict the probability of the image `lena.jpg` to one of their classes. When we digging the source of the repo, we will
find that it's quite simple, for classification task, it will do these following steps:

* load the pretrained model, using `jpcnn_create_network`, with the file name of the model
* load the to-be-classified image in the buffer for next step's classifying
* classify the image using `jpcnn_classify_image`, it will save the probability of each class in a fixed arrays
* for the array, predict each item that representing the probability of each class
* free the resources of network in memeory

All of the above steps are the simple process when using their libraries


##My Review

After reviewing, I get a rough idea about how it works in Linux, acutually they give the interface in the `jpcnn.h` file,
we can use some more complex function to do other image processing.

However, the model is not ours, the function only contains the interface and libaries that are unseen to us, we **CANNOT**
do any modification of the model or libaries.

What if we want to train our own model? (Since we may have a task in specific area like Food or X-ray image?)

What if we want to know how they classify and add our own processing like pre-processing, enhancement, or other feature
extractions steps? We should still figure out the code behind the `jpcnn.so`, so that we can build more powerfull functions
under their support.

However, it seems that currently they don't have plan to open source all of them, we need to figure out how.

Even though they support CCV models, that doesn't mean they used their libraries, it means that they've trained the model
like CCV's definition, and form a **NEW** model file in DeepBelief, so that they can use this model to predict like CCV
does. CCV's model still cannot work well in this repo, they need to be adjusted in this context
