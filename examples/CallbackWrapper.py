from flask import Flask, request
import json

app = Flask(__name__)

"""
    Пример запроса
{
    "type":"translated",
    "object":
        {
            "id":"54385",
            "peer_id":"116945277",
            "point":1000,
            "datetime":1558204677
        },
    "user_id":"402190246"
}
"""

### Пример принятие Callback ###

@app.route('/', methods=['POST'])
def processing():
    request_data = json.loads(request.data)
    """
        При получение платежа будет запущен данный метод, он может называтся как угодно

        :param request_data['object']['peer_id']: ID отправителя платежа
        :param request_data['object']['point']: Количество полученных VK Point
        :param request_data['object']['datetime']: Unix время
        
    """
    user_id = request_data['object']['peer_id']
    amount = request_data['object']['point']

    print('Получен платёж на сумму {amount} от {user_id}'.format(amount = amount, user_id = user_id))
    return 'ok'


if __name__ == "__main__":
    app.run()