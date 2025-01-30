# Conversational AI Agents: Build a Chatbot with Python

This repository contains code related to the tutorial on [building a Python chatbot with ChatterBot](https://realpython.com/build-a-chatbot-python-chatterbot/).

Create and activate a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/), then install the necessary dependencies:

```sh
$ python -m venv venv
$ source venv/bin/activate
(venv) $ python -m pip install -r requirements.txt
```

Then you can navigate into the folder `source_code_final/` and train and start the interactive command-line interface chatbot by running `bot.py`:

```sh
(venv) $ cd source_code_final
(venv) $ python bot.py
```

After training, you'll see an interactive prompt that you can chat with:

```text
> Hi
🪴 Welcome, friend 🤗
> Thanks for the Green Welcome
🪴 Ah yes avocados 🥑!
> Avocados?
🪴 Yes, there are a couple of seedlings that wanted to live
> did you mean avocado seedlings
🪴 The leafs that she had are getting dryer and dryer. But she’s also growing plenty of new ones
> did you mean monstera?
🪴 Fingers crossed 🤞
> No crops in pots
🪴 Wait, weren’t we talking about avocados?
> cleae
🪴 What do you consider 'your plants'?
> Mangoes
🪴 Lol
> lets talk about mangoes
🪴 10/10 thrips don't like this simple trick 😅
> hi
🪴 Welcome, friend 🤗
> thanks for the green welcome
🪴 Welcome, friend 🤗
> thanks
🪴 Kudos go mostly to my dad
> your dad?    
🪴 so many of them came up that he had about two dining room tables full of basil plants, each in their own pots...
> sounds like the perect experiment
🪴 
> I like the term
🪴 Motivational speeches
> what about the speeches
🪴 The cream must be the best of the best
```

The bot will learn from the replies you give and improve its accuracy. You can quit the interactive prompt by typing any of the `exit_conditions` defined in `bot.py`.

You'll find the code for each step of the tutorial in a separate folder. The folders also include a SQLite database that contains the different phases of training at each step. Because of this, you can inspect the project at different stages and notice how it evolves when you add more data and interactions.
