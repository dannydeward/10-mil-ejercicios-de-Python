pip install chatterbot
pip install chatterbot_corpus


Crea un script de Python y utiliza el siguiente código como punto de partida:
python
Copy code
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Crea un chatbot
chatbot = ChatBot('MiBot')

# Crea un nuevo entrenador para el chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Entrenar al chatbot con el conjunto de datos en inglés
trainer.train('chatterbot.corpus.english')

# Puedes agregar entrenamiento personalizado también
# trainer.train([
#     'Hola',
#     '¡Hola! ¿Cómo puedo ayudarte hoy?',
#     '¿Cuál es tu nombre?',
#     'Soy un bot. Puedes llamarme ChatBot.'
# ])

# Inicia el bucle de conversación
print("¡Hola! Soy un chatbot. Puedes preguntarme lo que quieras. Escribe 'salir' para finalizar.")

while True:
    user_input = input('Tú: ')
    
    if user_input.lower() == 'salir':
        print('Adiós. ¡Hasta luego!')
        break
    
    response = chatbot.get_response(user_input)
    print('Bot:', response)
