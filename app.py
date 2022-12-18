import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage,PostbackEvent

from fsm import TocMachine
from utils import send_text_message

load_dotenv()


machine = TocMachine(
    states = [
        "user", 
        "menu",
        "input_key",
        "show_fsm_pic",
        "search_restaurant",
        "add_favorite",
        "show_favorite",
        "delete_favorite",
        "introduction"],
    transitions=[
        {"trigger": "advance" , "source": "user" , "dest": "menu" , "conditions": "is_going_to_menu",},
        {"trigger": "advance" , "source": "menu" , "dest": "menu" , "conditions": "is_going_to_menu",},
        {"trigger": "advance" , "source": "menu" , "dest": "show_fsm_pic" , "conditions": "is_going_to_show_fsm_pic",},
        {"trigger": "advance" , "source": "menu" , "dest": "input_key" , "conditions": "is_going_to_input_key",},
        {"trigger": "advance" , "source": "input_key" , "dest": "search_restaurant" , "conditions": "is_going_to_search_restaurant",},
        {"trigger": "advance" , "source": "menu" , "dest": "introduction" , "conditions": "is_going_to_introduction",},
        # 加入我的最愛
        {"trigger": "advance_postback" , "source": ["user" , "menu"] , "dest": "add_favorite" , "conditions": "is_going_to_add_favorite",},
        # 查看最愛
        {"trigger": "advance" , "source": ["user" , "menu"] , "dest" : "show_favorite" , "conditions": "is_going_to_show_favorite",},
        # 刪除我的最愛
        {"trigger": "advance_postback" , "source": ["user" , "menu"] , "dest": "delete_favorite" , "conditions": "is_going_to_delete_favorite",},
        {"trigger": "go_back", "source": ["show_fsm_pic" , "search_restaurant", "introduction","add_favorite" , "show_favorite" , "delete_favorite",], "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")

channel_secret = os.environ.get("LINE_CHANNEL_SECRET")
channel_access_token = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN")

if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)

@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        enter = False
        enter_postback = False
        if isinstance(event, MessageEvent):
            if isinstance(event.message, TextMessage) and isinstance(event.message.text, str):
                response = machine.advance(event)
                enter = response
        elif isinstance(event, PostbackEvent):
            if isinstance(event.postback.data, str):
                response = machine.advance_postback(event)
                enter_postback = response
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        if enter == False:
            if enter_postback == False:
                send_text_message(event.reply_token, "請依照指示與按鈕來操作!")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
