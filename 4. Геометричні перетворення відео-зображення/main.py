import cv2  # Імпорт OpenCV
import numpy as np  # Імпорт NumPy для матричних операцій

def main():
    img = cv2.imread('image.jpg')  # Зчитування зображення

    if img is None:
        print("Помилка: не вдалося зчитати зображення")
        return

    rows, cols = img.shape[:2]  # Отримання розмірів зображення

    # Матриця зсуву (перенесення на 50 пікселів вправо і вниз)
    M = np.float32([[1, 0, 50], [0, 1, 50]])
    shifted = cv2.warpAffine(img, M, (cols, rows))  # Застосування зсуву

    cv2.imshow("Оригінал", img)  # Показ оригіналу
    cv2.imshow("Перенесене", shifted)  # Показ зображення після зсуву

    cv2.waitKey(0)  # Очікування клавіші
    cv2.destroyAllWindows()  # Закриття вікон

if __name__ == "__main__":
    main()
