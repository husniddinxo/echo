from flask import Flask, request

echo_app = Flask(__name__)

@echo_app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'GET':
        return 'hi from Husniddin'
    elif request.method == 'POST':
        data = request.get_json(force=True)
        print(data)

        chat_id = data['message']['from']['id']
        text = data['message']['text']
        return 'hello'

#if __name__ == '__main__':
    echo_app.run()
    print(chat_id, text)
    return 'hello'





