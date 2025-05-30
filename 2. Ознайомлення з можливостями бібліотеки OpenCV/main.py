import cv2  # Імпорт OpenCV

def main():
    cap = cv2.VideoCapture(0)  # Відкриття камери

    if not cap.isOpened():
        print("Помилка: камеру не знайдено")
        return

    while True:
        ret, frame = cap.read()  # Зчитування кадру
        if not ret:
            break

        cv2.imshow("Камера", frame)  # Показ кадру

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Вихід при 'q'
            break

    cap.release()  # Звільнення камери
    cv2.destroyAllWindows()  # Закриття вікон

if __name__ == "__main__":
    main()
