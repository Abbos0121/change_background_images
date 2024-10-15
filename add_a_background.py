from PIL import Image

try:
    # Пути к файлам
    transparent_image_path = "images\\delete_output.png"  # изображение с прозрачным фоном
    background_path = "images\\bb723d5d7de17a7e5952d79d57f26455.jpg"  # новый фон
    output_path = "images\\add_output.png"  # путь для сохранения результата

    # Открытие изображения с прозрачным фоном
    transparent_image = Image.open(transparent_image_path)

    # Открытие нового фона
    background_image = Image.open(background_path)

    # Приведение фона к размеру изображения с прозрачным фоном
    background_image = background_image.resize(transparent_image.size)

    # Наложение изображения с прозрачным фоном на новый фон
    background_image.paste(transparent_image, (0, 0), transparent_image)

    # Сохранение финального изображения
    background_image.save(output_path)

    # Успешный вывод
    print("The image with the new background is ready.")

except Exception as e:
    print(f"An error occurred: {e}")
