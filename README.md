# HaikuGenerator

A Python script that generates haikus based on a JSON dataset

Just supply a file called `sentences.json` in the project root. Fill it with sentences. The more the better - mine has 74,229 sentences!

The JSON file should be formatted like this, each sentence has its own line:
```json
[
    "Sentence",
    "Sentence 2",
    "Sentence 3",
    "Sentence 4",
    ... etc
]
```

Then, install the requirements in `requirements.txt` and run `main.py`. 

You can change settings like enabling and disabling spell check in `config.json`