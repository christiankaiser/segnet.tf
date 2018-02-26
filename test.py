import config
import model

# Print some configuration information
print('Model testing...')
print("Check point file: %s" % config.testing)
print("CamVid testing dir: %s" % config.test_dir)
print("Batch Size: %d" % config.batch_size)
print("Output directory: %s" % config.log_dir)

# Run the model
model.test()
