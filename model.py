from transformers import pipeline


class Destilbert:
    pipe = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

    def get_summary(self, text: str):
        return self.pipe(text)[0]['summary_text']


class T5Small:
    pipe = pipeline("summarization", model="Falconsai/text_summarization")

    def get_summary(self, text: str):
        return self.pipe(text)[0]['summary_text']


class Bert:
    pipe = pipeline("summarization", model="slauw87/bart_summarisation")

    def get_summary(self, text: str):
        return self.pipe(text)[0]['summary_text']