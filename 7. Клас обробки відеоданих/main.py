import cv2
import numpy as np

class VideoProcessor:
    def __init__(self, source=0):
        self.cap = cv2.VideoCapture(source)

    def convert_to_lab(self, frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)

    def shift_image(self, frame, dx=50, dy=50):
        rows, cols = frame.shape[:2]
        M = np.float32([[1, 0, dx], [0, 1, dy]])
        return cv2.warpAffine(frame, M, (cols, rows))

    def blur_image(self, frame, ksize=(5, 5)):
        return cv2.GaussianBlur(frame, ksize, 0)

    def edge_detection(self, frame, t1=100, t2=200):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return cv2.Canny(gray, t1, t2)

    def run(self):
        if not self.cap.isOpened():
            print("Помилка: не вдалося відкрити відео")
            return

        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            lab = self.convert_to_lab(frame)
            shifted = self.shift_image(frame)
            blurred = self.blur_image(frame)
            edges = self.edge_detection(frame)

            cv2.imshow("Оригінал", frame)
            cv2.imshow("LAB", lab)
            cv2.imshow("Зсув", shifted)
            cv2.imshow("Розмивання", blurred)
            cv2.imshow("Межі", edges)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    processor = VideoProcessor()
    processor.run()
