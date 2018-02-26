"""
Model configuration

We make two configurations here, one for testing locally,
and one for running the model on Floydhub. Only the paths to
input and output are different between the two configurations.

We can switch between the two models by setting the
environement variable `LOCAL=1` to pick up the local config.

By default, we will pick up the Floydhub config.
"""

import os
LOCAL_CONFIG = (os.environ.get('LOCAL', False) == '1')

# Paths definition

if LOCAL_CONFIG:
  print('Picking up local configuration')
  testing = 'output/model.ckpt-19999'           # checkpoint file
  finetune = 'output/model.ckpt-19000'          # finetune checkpoint file
  log_dir = "output"                            # dir to store ckpt
  image_dir = "../datasets/CamVid/train.txt"    # path to CamVid image
  test_dir = "../datasets/CamVid/test.txt"      # path to CamVid test image
  val_dir = "../datasets/CamVid/val.txt"        # path to CamVid val image
else:
  print('Picking up remote configuration')
  testing = '/model/model.ckpt-19999'          # checkpoint file
  finetune = '/model/model.ckpt-19000'         # finetune checkpoint file
  log_dir = "/output"                           # dir to store ckpt
  image_dir = "/CamVid/train.txt"               # path to CamVid image
  test_dir = "/CamVid/test.txt"                 # path to CamVid test image
  val_dir = "/CamVid/val.txt"                   # path to CamVid val image


# Values for both configurations

batch_size = 5                        # batch_size
learning_rate = 1e-3                  # initial lr

max_steps = 20000                     # max_steps
image_h = 360                         # image height
image_w = 480                         # image width
image_c = 3                           # image channel (RGB)
num_class = 11                        # total class number

save_image = True                     # whether to save predicted image

