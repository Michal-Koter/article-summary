from os import listdir
from os.path import join

import numpy as np
import pandas as pd
from bert_score import BERTScorer
from rouge import Rouge

from service import Service


def get_rouge_scores(text1, text2):
    rouge = Rouge()
    return rouge.get_scores(text1, text2)


def get_bert_scores(text1, text2):
    score = BERTScorer(lang='en')
    return score.score(text1, text2)


if __name__ == '__main__':
    article_path = "data/news-articles"
    summary_path = "data/summaries"

    service = Service()
    ref, bart_sum, distilbart_sum, t5_sum = [], [], [], []

    for file_name in listdir(article_path):
        print(file_name)

        article = None
        reference = None
        with open(join(article_path, file_name), 'r') as file:
            article = file.read()

        with open(join(summary_path, file_name), 'r') as file:
            reference = file.read()

        if article is None or reference is None:
            continue

        ref.append(reference)

        try:
            bart_summary = service.get_summary_bart(article)
        except Exception as e:
            print("Bart:", e)
            bart_summary = 'none'

        try:
            distilbart_summary = service.get_summary_distilbart(article)
        except Exception as e:
            print("Distilbart:", e)
            distilbart_summary = 'none'

        try:
            t5_summary = service.get_summary_t5_small(article)
        except Exception as e:
            print("T5:", e)
            t5_summary = 'none'

        bart_sum.append(bart_summary)
        distilbart_sum.append(distilbart_summary)
        t5_sum.append(t5_summary)

    # calculate bart_score
    _, _, f1_bart = get_bert_scores(ref, bart_sum)
    _, _, f1_distilbart = get_bert_scores(ref, distilbart_sum)
    _, _, f1_t5 = get_bert_scores(ref, t5_sum)

    bart_scores_out = []

    row = {
        "Metric": "F1",
        "Summary bart": np.average(f1_bart.tolist()),
        "Summary distilbart": np.average(f1_distilbart.tolist()),
        "Summery T5": np.average(f1_t5.tolist())
    }
    bart_scores_out.append(row)
    bart_scores_out = pd.DataFrame(bart_scores_out).set_index("Metric")
    print(bart_scores_out)

    # calculate ROUGE
    eval_bart_rouge = get_rouge_scores(bart_sum, ref)
    eval_distilbart_rouge = get_rouge_scores(distilbart_sum, ref)
    eval_t5_rouge = get_rouge_scores(t5_sum, ref)

    rouge_scores_out = []
    for metric in ["rouge-1", "rouge-2", "rouge-l"]:
        for label in ["F-Score"]:
            eval_bart_score = eval_bart_rouge[0][metric][label[0].lower()]
            eval_distilbart_score = eval_distilbart_rouge[0][metric][label[0].lower()]
            eval_t5_score = eval_t5_rouge[0][metric][label[0].lower()]
            row = {
                "Metric": f"{metric} ({label})",
                "Summary bart": eval_bart_score,
                "Summary distilbart": eval_distilbart_score,
                "Summery T5": eval_t5_score
            }
            rouge_scores_out.append(row)

    rouge_scores_out = pd.DataFrame(rouge_scores_out).set_index("Metric")
    print(rouge_scores_out)
