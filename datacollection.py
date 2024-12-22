import cv2

positionList = []
width = 100
height = 50

def mouseclick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        positionList.append((x,y))
while True:
    image = cv2.imread("car1.png")
    image = cv2.resize(image, (900, 500))
    for pos in positionList:
        #to create rectangle where it detects
        cv2.rectangle(image , pos, (pos[0]+ width, pos[1]+height), (255,0,255), 2 )
    cv2.imshow("Image", image)
    cv2.setMouseCallback("Image", mouseclick)
    k = cv2.waitKey(0)
    if k == ord('q'):
        break