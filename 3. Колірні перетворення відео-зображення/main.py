import cv2  # Імпорт бібліотеки OpenCV

def main():
    img = cv2.imread('image.jpg')  # Зчитування зображення з файлу

    if img is None:
        print("Помилка: не вдалося зчитати зображення")
        return

    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)  # Перетворення в LAB-простір

    cv2.imshow("Оригінал", img)  # Показ оригінального зображення
    cv2.imshow("LAB", lab)  # Показ LAB-зображення

    cv2.waitKey(0)  # Очікування натискання клавіші
    cv2.destroyAllWindows()  # Закриття всіх вікон

if __name__ == "__main__":
    main()
