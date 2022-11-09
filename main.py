import cv2
import numpy as np
import mcschematic


def generate_frame_schem(colors):
    schem = mcschematic.MCSchematic()
    for x in range(colors.shape[1]):
        for y in range(colors.shape[0]):
            schem.setBlock((x, 0, -y), "minecraft:white_concrete" if colors[y, x] == 1 else "minecraft:black_concrete")
    schem.save("data/schems", "bad_apple_frame_" + str(curFr), mcschematic.Version.JE_1_18_2)


def generate_frame_txt(colors):
    f = open("data/txt/frame" + str(curFr) + ".txt", "w")
    for x in range(colors.shape[1]):
        for y in range(colors.shape[0]):
            f.write(str(int(colors[y, x])) + " ")
        f.write("\n")
    f.close()


vid = cv2.VideoCapture("D:\Documents\JetBrainsProjects\BadAppleMinecraft\data/mainVid.mp4")
curFr = 0
_, frame = vid.read()
height, width = frame.shape[:2]

widthFin = width // 5
heightFin = height // 5

while vid.isOpened():
    _, frame = vid.read()
    frame = cv2.resize(frame, (widthFin, heightFin))
    cv2.imshow("Output", frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame //= 128

    colors = np.empty((widthFin, heightFin))
    for y in range(frame.shape[1]):
        for x in range(frame.shape[0]):
            colors[y][x] = frame[x][y]

    generate_frame_schem(colors)
    generate_frame_txt(colors)

    curFr += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
