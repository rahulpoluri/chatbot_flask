import time
time.clock = time.process_time()
import chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from chatterbot.response_selection import get_most_frequent_response
from chatterbot.filters import get_recent_repeated_responses
from chatterbot.comparisons import LevenshteinDistance
import logging
logging.basicConfig(level=logging.INFO)
# bot creation
bot = ChatBot("Rahul",
              storage_adapter="chatterbot.storage.SQLStorageAdapter",
              database_uri="sqlite:///database.sqlite3",
              # logic_adapters=["chatterbot.logic.MathematicalEvaluation",
              #                 "chatterbot.logic.TimeLogicAdapter",
              #                 "chatterbot.logic.BestMatch"

                # {
                #     'import_path': 'my.logic.AdapterClass1',
                #     'statement_comparison_function': chatterbot.comparisons.LevenshteinDistance
                #     'response_selection_method': chatterbot.response_selection.get_first_response
                # },
              #                 ]
              filters=[get_recent_repeated_responses],
                statement_comparison_function=LevenshteinDistance
              )

# bot training
# trainer1 = ListTrainer(bot)
# trainer1.train([
#     'How are you?',
#     'I am good.',
#     'That is good to hear.',
#     'Thank you',
#     'You are welcome.',
# ])
trainer2 = ChatterBotCorpusTrainer(bot)
trainer2.train("chatterbot.corpus.english")

# bot running
print("Your Chat bot is ready to answer now")
while True:
    try:
        bot_input = bot.get_response(input())
        print(bot_input)
    except (KeyboardInterrupt, EOFError, SystemExit):
        break

