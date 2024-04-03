from g4f.client import Client
from flask import Flask, render_template, request

client = Client()
text = ''
answer = ''
previousAnswer = ''
conversation = [
    {"role": "system", "content": "Ayudás con rutinas simples, rápidas y efectivas de calistenia, recordá usar muchos emojis"},
    {"role": "system", "content": "SIEMPRE das entradas en calor con 3 series y rango de 12 a 20 repeticiones, enfoque en la cintura escapular, manguito rotador, movilidad si piden tren superior y movilidad dinámica si piden piernas. Para los entrenamientos 2 bloques de 4 series de 6 a 12 repeticiones usando principales grupos musculares para tracción y empuje y 2 bloques de tracción y empuje pero esta vez 3 series de entre 8 a 20 repeticiones de intensidad. También siempre Avisá que es recomendable checkear con el profesor Jonathan Blazquez ante cualquier duda o consulta"},
    ]

"""
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Estás para ayudarme a dar rutinas de entrenamiento de calistenia, preferís dar entradas en calor con 3 series y rango de 12 a 20 repeticiones y para los entrenaminetos 2 bloques de 4 series de 6 a 12 repeticiones usando principales grupos musculares para tracción y empuje y 2 bloques de nuevo tracción y empuje pero esta vez 3 series de entre 8 a 20 repeticiones de intensidad, supongamos que soy principiante/intermedio"},
        {"role": "user", "content": "Hola, quiero entrenar"}
        ],
)
print(response.choices[0].message.content)
"""
app = Flask(__name__)

def get_answer(text):
    response = client.chat.completions.create(
    model="gpt-4",
    messages=[conversation[0]],
    )
    answer = response.choices[0].message.content
    previousAnswer = response.choices[0].message.content
    return render_template('index.html', answer = answer)

def get_answer_api(text):
    response = client.chat.completions.create(
    model="gpt-4",
    messages=[conversation[0]],
    )
    answer = response.choices[0].message.content
    previousAnswer = response.choices[0].message.content
    return answer
"""

@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('index.html')
"""


@app.route('/')
def index():
    return render_template('index.html')

@app.post('/talk')
def talk():
    text = request.form['text']
    print('TEXT:' + text)
    if previousAnswer != '':
        conversation.append({"role": "system", "content": "CONTEXTO ANTERIOR: " + previousAnswer})
    if text != '':
        conversation.append({"role": "user", "content": text})
        if conversation == '':
            conversation.append({"role": "system", "content": "CONTEXTO ANTERIOR: " + previousAnswer})
    print(conversation)
    return get_answer(text)

@app.post('/api/talk')
def apitalk():
    text = request.form['text']
    print('TEXT:' + text)
    if previousAnswer != '':
        conversation.append({"role": "system", "content": "CONTEXTO ANTERIOR: " + previousAnswer})
    if text != '':
        conversation.append({"role": "user", "content": text})
        if conversation == '':
            conversation.append({"role": "system", "content": "CONTEXTO ANTERIOR: " + previousAnswer})
    print(conversation)
    return get_answer_api(text)



app.run(host='0.0.0.0', port=8069)