import cv2
import os

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kameradan görüntü gelmiyor...")

img_counter = 0

resimler = 'cekilen_resimler'
os.makedirs(resimler, exist_ok=True)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Webcam", frame)

    k = cv2.waitKey(1)

    if k%256 == 27:
        print("Esc tuşuna basıldı.. Kapatılıyor..")
        break
    elif k % 256 == ord('s'):
        img_name = os.path.join(resimler, "opencv_frame_{}.png".format(img_counter))
        cv2.imwrite(img_name, frame)
        print("{} oluşturuldu!".format(img_name))
        img_counter += 1

cap.release()
cv2.destroyAllWindows()

