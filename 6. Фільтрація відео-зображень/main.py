import cv2  # Імпорт OpenCV
import numpy as np  # Імпорт NumPy

def main():
    img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)  # Зчитування зображення у відтінках сірого

    if img is None:
        print("Помилка: не вдалося зчитати зображення")
        return

    edges1 = cv2.Canny(img, 50, 150)   # Виявлення меж (нижчі параметри)
    edges2 = cv2.Canny(img, 100, 200)  # Виявлення меж (вищі параметри)

    cv2.imshow("Оригінал", img)
    cv2.imshow("Межі 50-150", edges1)
    cv2.imshow("Межі 100-200", edges2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
