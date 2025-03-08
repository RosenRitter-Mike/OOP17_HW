from skimage import io
import matplotlib.pyplot as plt


class EmojiImage:
    def __init__(self, file_name: str):
        self.file_name = file_name


class Emoji:
    def __init__(self, name: str, size: int, file_name: str):
        self.name = name
        self.size = size
        self.image = EmojiFactory.get_emoji(file_name)

    def draw(self):
        imoji = io.imread(self.image.file_name)
        plt.figure(figsize=(self.size, self.size))
        plt.title(self.name)
        print(plt.imshow(imoji))


class EmojiFactory:
    _emojis = {}

    @classmethod
    def get_emoji(cls, file_name):
        key = file_name

        if key not in cls._emojis:
            cls._emojis[key] = EmojiImage(file_name)
            print(f"Created new emoji: {cls._emojis[key]}")
        else:
            print(f"Reusing emoji: {cls._emojis[key]}")

        return cls._emojis[key]


def main():
    emojis = []
    emojis.append(Emoji("Imp", 100, "Smiling Devil Emoji.png"))
    emojis.append(Emoji("Lord", 150, "10064238.jpg"))
    emojis.append(Emoji("Angry", 100, "Very Angry Emoji.png"))
    emojis.append(Emoji("Yum", 120, "Hungry Face Emoji.png"))
    emojis.append(Emoji("Thinking", 120, "Thinking Emoji.png"))
    emojis.append(Emoji("Imp", 100, "Smiling Devil Emoji.png"))
    emojis.append(Emoji("Lord", 130, "10064238.jpg"))
    emojis.append(Emoji("Angry", 120, "Very Angry Emoji.png"))
    emojis.append(Emoji("Yum", 125, "Hungry Face Emoji.png"))
    emojis.append(Emoji("Money", 128, "Money Face Emoji.png"))
    emojis.append(Emoji("Money", 100, "Money Face Emoji.png"))
    emojis.append(Emoji("Lord", 150, "10064238.jpg"))
    emojis.append(Emoji("Nerd", 100, "Nerd Emoji With Glasses.png"))
    emojis.append(Emoji("Yum", 120, "Hungry Face Emoji.png"))
    emojis.append(Emoji("Nerd", 120, "Nerd Emoji With Glasses.png"))
    emojis.append(Emoji("Imp", 100, "Smiling Devil Emoji.png"))
    emojis.append(Emoji("Lord", 130, "10064238.jpg"))
    emojis.append(Emoji("Angry", 120, "Very Angry Emoji.png"))
    emojis.append(Emoji("Yum", 125, "Hungry Face Emoji.png"))
    emojis.append(Emoji("Thinking", 128, "Thinking Emoji.png"))

    for image in emojis:
        image.draw()

    print(f"\nNumber of Emoji objects: {len(emojis)}")
    print(f"Number of emoji objects: {len(EmojiFactory._emojis)}")
    print(f"Memory saving: {len(emojis) - len(EmojiFactory._emojis)} emoji objects")


if __name__ == "__main__":
    main()
