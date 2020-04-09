- Setup

  You will need to install Tensorflow and Python on your Machine.
  To install tensorflow, hit the following in the terminal:

      pip install tensorflow
      pip install opencv-python

- Gathering Images

  You will need a lot of images of your(or the one for whom you are creating the Face ID) Faces, i.e., go ahead and take hundreds of
  thousands of selfies and fill all those in the Images folder of this repository.

- (Re)Training

  To train the model, hit the following:

      python retrain.py --output_graph=retrained_graph.pb --output_labels=retrained_labels.txt --architecture=MobileNet_1.0_224 --image_dir=images

- Using the Model

  To get the model Working, hit

      python detect.py
