import random
import json


class StateTracker:
    def __init__(self, salt):
        self.salt = salt
        self.get_answer = lambda x: get_answer(self.salt, x)
        self.questions = get_questions(self.salt)
        self.used_questions = []
        self._qa_clf = dummy_clf

    def get_question(self):
        if not self.questions:
            self.questions = self.used_questions
            self.used_questions = []
        index = random.randrange(0, len(self.questions))
        question = self.questions.pop(index)
        self.used_questions.append(question)
        return question[0]

    def get_reply(self, utterance):
        is_question = self._qa_clf(utterance)
        if is_question:
            return self.get_answer(utterance)
        else:
            return self.get_question()


class StoriesHandler:
    def __init__(self, filename="data/train-v1.1.json"):
        with open(filename) as f:
            dataset = json.load(f)
        self.stories = [par["context"] for text in dataset["data"] for par in text]

    def get_one(self):
        return random.choice(self.stories)


def get_answer(paragraph, question):
    return "STUB"


def get_questions(paragraph):
    return []


def dummy_clf(string):
    clean = string.strip().lower()
    is_question = False
    if clean[-1] == "?":
        is_question = True
    if clean.split()[0] in ["what", "where", "who", "whom", "when", "how"]:
        is_question = True

    return is_question