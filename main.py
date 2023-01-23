from generate_images import Generate_Images

# Initialize the object
geometrical_shape = Generate_Images(resolution_image=(100, 100), background_color=(0, 0, 0))
# Create a directory to save the images
geometrical_shape.create_directories(directory_name="geometrical_shapes_using_pillow")

# Generate images for Training
geometrical_shape.generate_images(num_images=800, include_circle=True, images_for="Training")
geometrical_shape.generate_images(num_images=800, include_circle=False, images_for="Training")

# Generate images for Validation
geometrical_shape.generate_images(num_images=200, include_circle=True, images_for="Validation")
geometrical_shape.generate_images(num_images=200, include_circle=False, images_for="Validation")

# Generate images for Test
geometrical_shape.generate_images(num_images=100, include_circle=True, images_for="Test")
geometrical_shape.generate_images(num_images=100, include_circle=False, images_for="Test")