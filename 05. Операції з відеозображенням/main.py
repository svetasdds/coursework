import cv2  # Імпорт бібліотеки OpenCV

def main():
    img = cv2.imread('image.jpg')  # Зчитування зображення з файлу

    if img is None:
        print("Помилка: не вдалося зчитати зображення")
        return

    blur1 = cv2.GaussianBlur(img, (5, 5), 0)   # Гаусове розмивання
    blur2 = cv2.medianBlur(img, 5)             # Медіанне розмивання
    blur3 = cv2.GaussianBlur(img, (15, 15), 0) # Розмивання з більшим ядром

    cv2.imshow("Оригінал", img)
    cv2.imshow("Гаусове 5x5", blur1)
    cv2.imshow("Медіанне 5", blur2)
    cv2.imshow("Гаусове 15x15", blur3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
