import cv2
from cvzone.HandTrackingModule import HandDetector as hd

def identify_ges(fingers):
    if fingers == [0, 1, 0, 0, 0]:
        return "POINTING"
    elif fingers == [0, 0, 1, 0, 0]:
        return "F***!"
    elif fingers == [0, 1, 1, 0, 0]:
        return "PEACE"
    elif fingers == [0, 1, 1, 1, 0]:
        return "THREE"
    elif fingers == [0, 1, 1, 1, 1]:
        return "FOUR"
    elif fingers == [1, 1, 1, 1, 1]:
        return "OPEN PALM"
    elif fingers == [0, 0, 0, 0, 0]:
        return "FIST"
    elif fingers == [0, 0, 0, 0, 1]:
        return "PINKY UP"
    elif fingers in [[0, 1, 0, 0, 1], [1, 1, 0, 0, 1]]:
        return "ROCK ON"
    else:
        return "UNKNOWN"
    
cam = cv2.VideoCapture(0)
detector = hd(detectionCon=0.8, maxHands=1)

while True:
    success, img = cam.read()
    if not success:
        break

    hands, img = detector.findHands(img,draw=True,flipType=False)

    ges = "NO HAND DETECTED"
    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        print("Finger states:", fingers)
        ges = identify_ges(fingers)
       
    cv2.putText(img, ges, (30, 50), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    
    cv2.imshow("GestureLens", img)
    if cv2.waitKey(10) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
