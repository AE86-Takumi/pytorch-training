# 画像のリサイズと正規化
import matplotlib.pyplot as plt
from PIL import Image
from torchvision import transforms

if __name__ == "__main__":
    image_path = "./exercise_data/dog_img.png"
    image = Image.open(image_path)

    transform = trasnforms.Compose([
        transforms.Resize((224,224))
    ])
    # 変換を適応
    transformed_image = transform(image)
    print("変換前のサイズ")
    print(image.size)
    print("変換後のサイズ")
    print(transformed_image.size)
    plt.imshow(image)
    plt.show()
    plt.imshow(transformed_image)
    plt.show()