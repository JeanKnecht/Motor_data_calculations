import os
import imageio

files = os.listdir("C:/Users/JeanK/OneDrive/Bureaublad/rocket/Rocket Data/Motor_data_calculations/Animated graph/Images")

images = []
img_path = [os.path.join('C:/Users/JeanK/OneDrive/Bureaublad/rocket/Rocket Data/Motor_data_calculations/Animated graph/Images', file) for file in files]
for img in img_path:
    images.append(imageio.imread(img))

imageio.mimwrite('C:/Users/JeanK/OneDrive/Bureaublad/rocket/Rocket Data/Motor_data_calculations/Animated graph/Gif/animated_graph.gif', images, fps = 20)