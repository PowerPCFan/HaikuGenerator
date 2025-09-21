# HaikuGenerator

A Python script that generates haikus based on a JSON dataset

Just supply a file called `sentences.json` in the project root. Fill it with sentences. The more the better - mine has 73,843 sentences! But you only need a few hundred to get started.

The JSON file should be formatted like this:
```json
[
    "Sentence 1",
    "Sentence 2",
    "Sentence 3",
    "Sentence 4",
    // ...etc
]
```

Then, install the requirements in `requirements.txt` and run `main.py`. 

You can change settings like enabling and disabling spell check in `config.json`.

Here's an overview of all the settings:
- `max_generation_attempts`: `int`: How many attempts the program should make to create a proper line before giving up. Increase this if you find that lines are often not being generated. You will probably need to increase this if you increase the `state_size`.
- `advanced_spell_check`: `bool`: Whether to enable the more advanced (and very slow) spell check using TextBlob.
- `syllables`: `list`: The syllable count for each line. Each syllable you add corresponds to a line, so you can also use this key to change the amount of lines in the haiku.
- `state_size`: `int`: The state size for the Markov model. Higher values make the generated text more coherent, but also more similar to the sentences provided in your sentences.json file. Higher state size may also make generation slightly slower due to more attempts for sentences with the proper syllable count being necessary. You also need a much larger dataset to get good results with higher state sizes. The default is `2`, which is a good balance for most use cases. I would not recommend going above `4` unless you have an extremely large dataset with hundreds of thousands of sentences.
