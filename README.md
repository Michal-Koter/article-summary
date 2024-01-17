# Streszczanie anglojęzycznych artykułów

Aplikacja pozwala na otrzymanie streszczenia artykułu w języku angielski.
Używając interfejsu webowego, otrzymuje się od razu trzy streszczenia z różnych modeli.

## Instalacja

Instalacja wymaganych modułów

```
pip install -r \requirements.txt
```

Może być też potrzebna instalacja kompilatora Rust'a


## Uruchamianie

Będąc w katalogu projektu wpisz komendę:

```
uvicorn main:app --reload   
```

Program uruchomi sięna porcie 8000.

Aby wejść na stronę domową użyj: `http://localhost:8000/static/index.html`

## Streszczanie z pliku CSV
Jest możliwość streszczania tekstu zawartego w CSV, gdzie każdy artykuł jest w oddzielnej linii.
Plik musi mieć nazwę `articles.csv`.
Najlepiej jak dane w pliku CSV nnie zawierają cudzysłowów.

Uruchamianie z linii komend
```
python -m summery_to_file.py
```
Jako wynik dostajemy plik `articles_summery.csv`

## Wykorzystane modele AI

Wszystkie modele pochodzą z HuggingFace

### sshleifer/distilbart-cnn-12-6
https://huggingface.co/sshleifer/distilbart-cnn-12-6

### Falconsai/text_summarization
https://huggingface.co/Falconsai/text_summarization

### slauw87/bart_summarisation
https://huggingface.co/slauw87/bart_summarisation

