# SegNet with Tensorflow

SegNet implementation for Tensorflow with instructions to run the model on Floydhub. This implementation is based on [github.com/tkuanlun350/Tensorflow-SegNet](https://github.com/tkuanlun350/Tensorflow-SegNet).

The implementation is a slightly modified [SegNet](http://arxiv.org/abs/1511.00561) in Tensorflow trained on the CamVid dataset (see section Dataset for the details).

In this implementation the original upsampling method is replaced simply by a deconv (or conv-transpose) layer (without pooling indices), because indice unravelling is not yet unavailable in Tensorflow (see corresponding [issue](https://github.com/tensorflow/tensorflow/issues/2169)).


## Dataset

We use here the Alex Kendall's CamVid dataset originally available from the [SegNet Tutorial](https://github.com/alexgkendall/SegNet-Tutorial) and available on Floydhub ffrom [humpelandi/datasets/camvid/1](https://www.floydhub.com/humpelandi/datasets/camvid).


## Run it on Floydhub

Create the project on Floydhub:

```
floyd init segnet
```


Training the network:

```
floyd run --gpu --env tensorflow-1.3 --data humpelandi/datasets/camvid/1:/CamVid 'python train.py'
```


It is possible to finetune an existing model:

```
# Not yet implemented
```


Testing is done with:

```
floyd run \
      --gpu \
      --env tensorflow-1.3 \
      --data humpelandi/datasets/camvid/1:/CamVid \
      --data humpelandi/projects/segnet/1/output:/model \
      'python test.py'
```

