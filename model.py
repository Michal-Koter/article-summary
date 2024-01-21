from transformers import pipeline


class Model:
    def __init__(self, model_name):
        self.pipe = pipeline("summarization", model=model_name)

    def get_summary(self, text: str):
        return self.pipe(text)[0]['summary_text']
