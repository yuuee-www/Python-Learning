from PIL import Image
import matplotlib.pyplot as plt

show_height = 25
show_width = 60
#We need to adjust these two values

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
#ascii list to store characters
char_len = len(ascii_char)

pic = plt.imread("1233.jpg")
# read the image
# matplotlib  R G B
# opencv的cv2 B G R

pic_height ,pic_width,_ = pic.shape
# obtain height & width
gray = 0.2126 * pic[:,:,0] + 0.7152 * pic[:,:,1] + 0.0722 * pic[:,:,2]
# gray = 0.2126 * r + 0.7152 * g + 0.0722 * b

# find corresbonding ascii_char
for i in range(show_height):
    # print the image
    y = int(i * pic_height / show_height )
    text = ""
    for j in range(show_width):
        x = int(j * pic_width / show_width)
        text += ascii_char[int(gray[y][x] / 256 * char_len)]
    print(text)
n = input()


