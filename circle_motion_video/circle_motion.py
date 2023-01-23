import numpy as np
import cv2
import sys

sys.path.append("../image_generator")
import image_generator.draw_image_using_pillow

color = image_generator.draw_image_using_pillow.color
positions = image_generator.draw_image_using_pillow.positions


class CircleMotionVideo:
    def __init__(self, resolution_image=(512, 512, 3)):
        self.resolution_image = resolution_image

        # Create a black image
        self.img = np.zeros(self.resolution_image, np.uint8)

        # Circle parameters
        self.radius = 10
        self.color = color()  # BGR
        self.thickness = 2
        self.start_position = positions(self.resolution_image)

    def draw_circle(self):
        cv2.circle(self.img, self.start_position, self.radius, self.color, self.thickness)

        # Create a video writer
        self.fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # for mp4 format
        self.out = cv2.VideoWriter("circle_movement.mp4", self.fourcc, 5.0, (self.resolution_image[0], self.resolution_image[1]))

        # Write the frames to the video
        self.n = 0
        self.m = 0
        for i in range(250):
            self.img_copy = self.img.copy()
            if i <= 10:
                self.n += 1
            elif i <= 20:
                self.m += 1
            elif i <= 30:
                self.m += -1
            else:
                self.m += 1
            self.start_position = (self.start_position[0] + self.n, self.start_position[1] + self.m)
            cv2.circle(self.img_copy, self.start_position, self.radius, self.color, self.thickness)
            self.out.write(self.img_copy)

        # Release the resources
        self.out.release()
        cv2.destroyAllWindows()


# main function to run the model
if __name__ == "__main__":
    motion_video = CircleMotionVideo(resolution_image=(200, 200, 3))
    motion_video.draw_circle()