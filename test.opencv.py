import cv2
from uuid import uuid4

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    frame = cv2.resize(frame, (32, 32), interpolation=cv2.INTER_NEAREST)

    cv2.imshow("hola", frame)
    
    key = cv2.waitKey(1) & 0xFF

    if key != 255:
        print("Key: {}".format(key))

    if key == ord('q'):
        break

    name = str(uuid4())

    if key == ord('1'):
        print("Aprender 1 dedo: {}".format(name))
        cv2.imwrite("fingers/one/{}.png".format(name), frame)

    if key == ord('2'):
        print("Aprender 2 dedo")
        cv2.imwrite("fingers/two/{}.png".format(name), frame)
        
cv2.destroyAllWindows()