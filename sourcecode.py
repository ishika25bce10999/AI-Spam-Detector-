import math
import json
import os
import string
from collections import defaultdict


class DataProcessor:

    def __init__(self):
        self.spam_words = defaultdict(int)
        self.ham_words = defaultdict(int)
        self.spam_count = 0
        self.ham_count = 0
        self.total_spam_words = 0
        self.total_ham_words = 0

    def clean_text(self, text):
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        words = text.split()
        return words

    def load_dataset(self, filepath):
        dataset = []

        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                for line in file:
                    if ',' in line:
                        label, message = line.strip().split(',', 1)
                        dataset.append((label, message))

            return dataset

        except Exception as e:
            print("Error loading dataset:", e)
            return []

    def train(self, dataset):

        for label, message in dataset:

            words = self.clean_text(message)

            if label == "spam":
                self.spam_count += 1
                for word in words:
                    self.spam_words[word] += 1
                    self.total_spam_words += 1

            else:
                self.ham_count += 1
                for word in words:
                    self.ham_words[word] += 1
                    self.total_ham_words += 1


class SpamClassifier:

    def __init__(self, processor):
        self.processor = processor

    def predict(self, message):

        words = self.processor.clean_text(message)

        spam_score = 0
        ham_score = 0

        total_messages = self.processor.spam_count + self.processor.ham_count

        spam_prob = self.processor.spam_count / total_messages
        ham_prob = self.processor.ham_count / total_messages

        spam_score = math.log(spam_prob)
        ham_score = math.log(ham_prob)

        for word in words:

            spam_word_freq = self.processor.spam_words[word] + 1
            ham_word_freq = self.processor.ham_words[word] + 1

            spam_score += math.log(
                spam_word_freq / (self.processor.total_spam_words + 1)
            )

            ham_score += math.log(
                ham_word_freq / (self.processor.total_ham_words + 1)
            )

        if spam_score > ham_score:
            return "Spam"
        else:
            return "Not Spam"


class ReportGenerator:

    def __init__(self):
        self.total = 0
        self.correct = 0

    def update(self, prediction, actual):

        self.total += 1

        if prediction.lower() == actual.lower():
            self.correct += 1

    def show_report(self):

        if self.total == 0:
            print("No data available")
            return

        accuracy = (self.correct / self.total) * 100

        print("\nModel Performance")
        print("Total Tested:", self.total)
        print("Correct Predictions:", self.correct)
        print("Accuracy:", round(accuracy, 2), "%")


class FileManager:

    def save_model(self, processor, filename="spam_model.json"):

        data = {
            "spam_words": dict(processor.spam_words),
            "ham_words": dict(processor.ham_words),
            "spam_count": processor.spam_count,
            "ham_count": processor.ham_count,
            "total_spam_words": processor.total_spam_words,
            "total_ham_words": processor.total_ham_words
        }

        with open(filename, "w") as file:
            json.dump(data, file)

    def load_model(self, processor, filename="spam_model.json"):

        if not os.path.exists(filename):
            return False

        with open(filename, "r") as file:
            data = json.load(file)

        processor.spam_words = defaultdict(int, data["spam_words"])
        processor.ham_words = defaultdict(int, data["ham_words"])
        processor.spam_count = data["spam_count"]
        processor.ham_count = data["ham_count"]
        processor.total_spam_words = data["total_spam_words"]
        processor.total_ham_words = data["total_ham_words"]

        return True


class SpamMailDetector:

    def __init__(self):
        self.processor = DataProcessor()
        self.classifier = SpamClassifier(self.processor)
        self.report = ReportGenerator()
        self.file_manager = FileManager()

    def train_model(self):

        filepath = input("Enter dataset file path: ")

        dataset = self.processor.load_dataset(filepath)

        if not dataset:
            print("Dataset not loaded")
            return

        self.processor.train(dataset)

        self.file_manager.save_model(self.processor)

        print("Model trained and saved successfully!")

    def detect_spam(self):

        loaded = self.file_manager.load_model(self.processor)

        if not loaded:
            print("Train model first")
            return

        while True:

            print("\nEnter Email (or type exit):")
            message = input()

            if message.lower() == "exit":
                break

            prediction = self.classifier.predict(message)

            print("Prediction:", prediction)

    def test_model(self):

        loaded = self.file_manager.load_model(self.processor)

        if not loaded:
            print("Train model first")
            return

        filepath = input("Enter test dataset path: ")

        dataset = self.processor.load_dataset(filepath)

        for label, message in dataset:

            prediction = self.classifier.predict(message)

            actual = "Spam" if label == "spam" else "Not Spam"

            self.report.update(prediction, actual)

        self.report.show_report()


if __name__ == "__main__":

    detector = SpamMailDetector()

    while True:

        print("\nAI Spam Mail Detector")
        print("1. Train Model")
        print("2. Detect Spam")
        print("3. Test Model")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            detector.train_model()

        elif choice == "2":
            detector.detect_spam()

        elif choice == "3":
            detector.test_model()

        elif choice == "4":
            break

        else:
            print("Invalid choice")
