from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot(
    'করোনা বট',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'আমি দুঃখিত, কিন্তু আমি বুঝতে পারছিনা। আমি এখনো শিখছি।',
            'maximum_similarity_threshold': 0.70
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)


trainer = ListTrainer(chatbot)

training_data_quesans = open('ques_ans.txt').read().splitlines()
training_data_personal = open('personal_ques.txt').read().splitlines()

training_data = training_data_quesans + training_data_personal

trainer.train(training_data)

