
import cv2
import mediapipe as mp

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    altura, largura, _ = img.shape
    dedos = 0

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lmList = []
            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x * largura), int(lm.y * altura)
                lmList.append((id, cx, cy))
                cv2.putText(img, str(id), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 1)

            tips = [8, 12, 16, 20]
            for tip in tips:
                if lmList[tip][2] < lmList[tip - 2][2]:
                    dedos += 1

            if abs(lmList[4][1] - lmList[3][1]) > 30:
                dedos += 1

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.putText(img, f'Dedos: {dedos}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)
    cv2.imshow("Contagem de Dedos", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
