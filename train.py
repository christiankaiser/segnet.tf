import config
import model

# Print some configuration information
print('Model training...')
print("Max training Iteration: %d" % config.max_steps)
print("Initial learning rate: %f" % config.learning_rate)
print("CamVid training images directory: %s" % config.image_dir)
print("CamVid validation images directory: %s" % config.val_dir)
print("Batch Size: %d" % config.batch_size)
print("Output directory: %s" % config.log_dir)

# Run the model
model.training(is_finetune=False)
