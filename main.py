from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    # Return json format.
    # {
    #     "attachments": [
    #         {
    #             "color": "#36a64f",
    #             "title": "Sukh Raj Limbu",
    #             "title_link": "https://www.codechef.com/users/sorablaze_11",
    #             "image_url": "https://picsum.photos/id/1005/200/300"
    #         }
    #     ]
    # }
    response = {}
    response['attachments'] = []
    payload = request.form.get('text').split()
    if len(payload) == 2:
        response['attachments'].append({
            "color": "#36a64f",
            "title": "Sukh Raj Limbu",
            "title_link": "https://www.codechef.com/users/sorablaze_11",
            "image_url": "https://picsum.photos/id/1005/200/300"
        })
    else:
        response['attachments'].append({
            'title': "Error"
        })
    return response


if __name__ == '__main__':
    app.run(debug=True)
