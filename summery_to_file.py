import pandas as pd

from service import Service

if __name__ == '__main__':
    try:
        data = open('data/articles.csv', "r")
    except FileNotFoundError:
        print("File not found")
        exit(1)

    service = Service()

    d = {"article": [], "sshleifer/distilbart-cnn-12-6": [], "Falconsai/text_summarization": [], "slauw87/bart_summarisation": []}
    df = pd.DataFrame(data=d)

    for idx, line in enumerate(data):
        print(line)
        summery_destilbart = service.get_summery_destilbert(line)
        summery_t5 = service.get_summery_t5_small(line)
        summery_bert = service.get_summery_bart(line)
        df.loc[idx] = [line, summery_destilbart, summery_t5, summery_bert]

    print(df.shape)
    df.to_csv('data/articles_summery.csv', index=False, sep='@')
