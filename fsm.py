import copy
from transitions.extensions import GraphMachine

import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FlexSendMessage

from utils import send_text_message

load_dotenv()

channel_secret = os.environ.get("LINE_CHANNEL_SECRET")
channel_access_token = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN")

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pyimgur
import message_template
from urllib.parse import quote

keyword = ""
search_imageurl = []
search_star = []
search_online = []
search_website = []
search_address = []
search_name = []
index = 0
favorite_imageurl = []
favorite_star = []
favorite_online = []
favorite_website = []
favorite_address = []
favorite_name = []
favorite_index = 0

def get_restaurant_now():
    search_name.clear()
    search_imageurl.clear()
    search_star.clear()
    search_online.clear()
    search_website.clear()
    search_address.clear()
    global index
    index = 0
    response = requests.get("https://ifoodie.tw/explore/%E5%8F%B0%E5%8D%97%E5%B8%82/list/" + quote(keyword) + "?sortby=rating&opening=true")
    print("https://ifoodie.tw/explore/%E5%8F%B0%E5%8D%97%E5%B8%82/list/" + quote(keyword) + "?sortby=rating&opening=true")
    soup = BeautifulSoup(response.content, "html.parser")
    cards = soup.find_all('div', {'class': 'jsx-3292609844 restaurant-item track-impression-ga'}, limit=10)
    for card in cards:
        search_name.append(card.find("a", {"class": "jsx-3292609844 title-text"}).getText())
        search_star.append(card.find("div" , {"class" : "jsx-1207467136 text"}).getText())
        search_online.append(card.find("div", {"class": "jsx-3292609844 info"}).getText()[6:])
        search_address.append(card.find("div", {"class": "jsx-3292609844 address-row"}).getText())
        temp_imageurl = card.find("img" , {"alt" : search_name[index]}).get("data-src")
        if temp_imageurl == None :
            temp_imageurl = card.find("img" , {"alt" : search_name[index]}).get("src")
        search_imageurl.append(temp_imageurl)
        search_website.append("https://ifoodie.tw" + card.find("a", {"class": "jsx-3292609844 click-tracker"}).get("href"))
        # print(search_name[index])
        # print(search_star[index])
        # print(search_online[index])
        # print(search_address[index])
        # print(search_imageurl[index])
        # print(search_website[index])
        index += 1

def get_url_3month():
    return "三個月資訊"

def get_url_2week():
    return "兩周資訊"

def get_recommend():
    return "建議你"

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_menu(self, event):
        text = event.message.text
        return text == "主選單"

    def is_going_to_show_fsm_pic(self, event):
        text = event.message.text
        return text == "fsm"

    def is_going_to_search_restaurant(self, event):
        global keyword
        keyword = event.message.text

        #check is chinese
        for _char in keyword:
            if not '\u4e00' <= _char <= '\u9fa5' :
                return  False
        return True

    def on_enter_input_key(self, event):
        send_text_message(event.reply_token, '請輸入你現在想吃什麼(例如火鍋、牛肉、飲料等等)(限中文)')

    def is_going_to_input_key(self , event):
        text = event.message.text
        return text == "查詢店家資訊"

    def is_going_to_introduction(self, event):
        text = event.message.text
        return text == "功能介紹與使用說明"

    def on_enter_menu(self, event):
        reply_token = event.reply_token
        message = message_template.main_menu
        message_to_reply = FlexSendMessage("開啟主選單", message)
        line_bot_api = LineBotApi( channel_access_token )
        line_bot_api.reply_message(reply_token, message_to_reply)
    
    def on_enter_show_fsm_pic(self, event):
        reply_token = event.reply_token
        message = message_template.show_pic
        message_to_reply = FlexSendMessage("查看fsm結構圖", message)
        line_bot_api = LineBotApi( channel_access_token )
        line_bot_api.reply_message(reply_token, message_to_reply)
        self.go_back()

    def on_enter_search_restaurant(self, event):
        reply_token = event.reply_token
        get_restaurant_now()
        global index
        if index != 0 :
            message = message_template.restaurant_list
            message["contents"].clear()
            for i in range (index):
                new_message = copy.deepcopy(message_template.restaurant_item)
                new_message["hero"]["url"] = search_imageurl[i]
                new_message["body"]["contents"][0]["text"] = search_name[i]
                new_message["body"]["contents"][1]["contents"][0]["contents"][1]["text"] = search_star[i]
                new_message["body"]["contents"][1]["contents"][1]["contents"][1]["text"] = search_address[i]
                new_message["body"]["contents"][1]["contents"][2]["contents"][1]["text"] = search_online[i]
                new_message["footer"]["contents"][0]["action"]["uri"] = search_website[i]
                # record data
                new_message["footer"]["contents"][2]['action']["data"] = "加入最愛," + search_website[i]
                message["contents"].append(new_message)
            message_to_reply = FlexSendMessage("查詢店家資訊", message)
            line_bot_api = LineBotApi( channel_access_token )
            line_bot_api.reply_message(reply_token, message_to_reply)
        else :
            message_to_reply = FlexSendMessage("查詢店家資訊", message_template.no_result)
            line_bot_api = LineBotApi( channel_access_token )
            line_bot_api.reply_message(reply_token, message_to_reply)
        self.go_back()

    # 加入最愛-----------------------------------------------------------------------
    def is_going_to_add_favorite(self , event):
        text = event.postback.data
        add_or_delete = text.split(',')[0]
        return add_or_delete == '加入最愛'

    def on_enter_add_favorite(self, event):
        reply_token = event.reply_token
        get_website = event.postback.data.split(',')[1]
        response = requests.get(get_website)
        soup = BeautifulSoup(response.content, "html.parser")
        name = soup.find('img', {'itemprop': 'image'}).get("alt")
        img = soup.find('img', {'itemprop': 'image'}).get("src")
        star = soup.find('div', {'class': 'jsx-1207467136 text'}).getText()
        address = soup.find('span', {'class': 'jsx-1969054371 detail'}).getText()
        online = soup.find('div', {'class': 'jsx-1969054371 open-text'}).getText()
        website = get_website
        has_data = False
        global favorite_index
        msg = ""
        # if url[0] == 'movie':
        for tmp_name in favorite_name :
            if tmp_name == name :
                msg = '已在我的最愛!'
                has_data = True
                break
        if has_data == False :
            if favorite_index < 10:
                favorite_imageurl.append(img)
                favorite_name.append(name)
                favorite_star.append(star)
                favorite_address.append(address)
                favorite_online.append(online)
                favorite_website.append(website)
                favorite_index += 1
                msg = '成功加入我的最愛'
            else:
                msg = '我的最愛已滿(最多10個)'
        send_text_message(reply_token , msg)
        self.go_back()
    # ----------------------------------------------------------------------------------------------------
    
    # 查詢最愛-----------------------------------------------------------------------
    def is_going_to_show_favorite(self , event):
        text = event.message.text
        return text == "查看我的最愛"

    def on_enter_show_favorite(self, event):
        reply_token = event.reply_token
        global favorite_index
        if favorite_index != 0 :
            message = message_template.restaurant_list
            message["contents"].clear()
            for i in range (favorite_index):
                new_message = copy.deepcopy(message_template.favorite_item)
                new_message["hero"]["url"] = favorite_imageurl[i]
                new_message["body"]["contents"][0]["text"] = favorite_name[i]
                new_message["body"]["contents"][1]["contents"][0]["contents"][1]["text"] = favorite_star[i]
                new_message["body"]["contents"][1]["contents"][1]["contents"][1]["text"] = favorite_address[i]
                new_message["body"]["contents"][1]["contents"][2]["contents"][1]["text"] = favorite_online[i]
                new_message["footer"]["contents"][0]["action"]["uri"] = favorite_website[i]
                # record data
                new_message["footer"]["contents"][2]['action']["data"] = "從我的最愛移除," + favorite_website[i]
                message["contents"].append(new_message)
            message_to_reply = FlexSendMessage("查詢我的最愛", message)
            line_bot_api = LineBotApi( channel_access_token )
            line_bot_api.reply_message(reply_token, message_to_reply)
        else :
            message_to_reply = FlexSendMessage("查詢我的最愛", message_template.no_result)
            line_bot_api = LineBotApi( channel_access_token )
            line_bot_api.reply_message(reply_token, message_to_reply)
        self.go_back()
    # ----------------------------------------------------------------------------------------------------

    # 刪除最愛-----------------------------------------------------------------------
    def is_going_to_delete_favorite(self , event):
        text = event.postback.data
        add_or_delete = text.split(',')[0]
        return add_or_delete == '從我的最愛移除'

    def on_enter_delete_favorite(self, event):
        reply_token = event.reply_token
        get_website = event.postback.data.split(',')[1]
        response = requests.get(get_website)
        soup = BeautifulSoup(response.content, "html.parser")
        name = soup.find('img', {'itemprop': 'image'}).get("alt")
        img = soup.find('img', {'itemprop': 'image'}).get("src")
        star = soup.find('div', {'class': 'jsx-1207467136 text'}).getText()
        address = soup.find('span', {'class': 'jsx-1969054371 detail'}).getText()
        online = soup.find('div', {'class': 'jsx-1969054371 open-text'}).getText()
        website = get_website
        has_data = False
        global favorite_index
        msg = ""
        # if url[0] == 'movie':
        for tmp_name in favorite_name :
            if tmp_name == name :
                has_data = True
                break
        if has_data == True :
            if favorite_index > 0:
                favorite_imageurl.remove(img)
                favorite_name.remove(name)
                favorite_star.remove(star)
                favorite_address.remove(address)
                favorite_online.remove(online)
                favorite_website.remove(website)
                favorite_index -= 1
                msg = '成功從我的最愛中移除'
            else :
                msg = "我的最愛中無資料哦~"
        else :
            msg = "我的最愛中無此資料哦~"
        send_text_message(reply_token , msg)
        self.go_back()
    # ----------------------------------------------------------------------------------------------------
    
    def on_enter_introduction(self, event):
        reply_token = event.reply_token
        message = message_template.introduction_message
        message_to_reply = FlexSendMessage("功能介紹與使用說明", message)
        line_bot_api = LineBotApi( channel_access_token )
        line_bot_api.reply_message(reply_token, message_to_reply)
        self.go_back()

