import cv2
import os

# Start Camera
cam = cv2.VideoCapture(0)

while True:

    ret, frame = cam.read()

    # Show Camera
    cv2.imshow("Live Petrol Pump Camera", frame)

    key = cv2.waitKey(1)

    # Press S to Scan
    if key == ord('s'):

        # Save Image
        cv2.imwrite("images/meter.jpg", frame)

        print("Image Saved Successfully")

        # Run OCR
        os.system("python ocr_reader.py")

    # Press ESC to Exit
    elif key == 27:
        break

cam.release()
cv2.destroyAllWindows()
