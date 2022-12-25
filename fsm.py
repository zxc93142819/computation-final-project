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

keyword = {}
search_imageurl = {}
search_star = {}
search_online = {}
search_website = {}
search_address = {}
search_name = {}
index = {}

favorite_imageurl = {}
favorite_star = {}
favorite_online = {}
favorite_website = {}
favorite_address = {}
favorite_name = {}
favorite_index = {}

def get_restaurant_now(user_id):
    id = 0
    key = keyword[user_id]
    response = requests.get("https://ifoodie.tw/explore/%E5%8F%B0%E5%8D%97%E5%B8%82/list/" + quote(key) + "?sortby=rating&opening=true")
    print("https://ifoodie.tw/explore/%E5%8F%B0%E5%8D%97%E5%B8%82/list/" + quote(key) + "?sortby=rating&opening=true")
    soup = BeautifulSoup(response.content, "html.parser")
    cards = soup.find_all('div', {'class': 'jsx-3292609844 restaurant-item track-impression-ga'}, limit=10)
    spe_search_imageurl = []
    spe_search_star = []
    spe_search_online = []
    spe_search_website = []
    spe_search_address = []
    spe_search_name = []
    for card in cards:
        title = card.find("a", {"class": "jsx-3292609844 title-text"}).getText()
        spe_search_name.append(title)
        spe_search_star.append(card.find("div" , {"class" : "jsx-1207467136 text"}).getText())
        spe_search_online.append(card.find("div", {"class": "jsx-3292609844 info"}).getText()[6:])
        spe_search_address.append(card.find("div", {"class": "jsx-3292609844 address-row"}).getText())
        temp_imageurl = card.find("img" , {"alt" : title}).get("data-src")
        if temp_imageurl == None :
            temp_imageurl = card.find("img" , {"alt" : title}).get("src")
        spe_search_imageurl.append(temp_imageurl)
        spe_search_website.append("https://ifoodie.tw" + card.find("a", {"class": "jsx-3292609844 click-tracker"}).get("href"))
        # print(search_name[index])
        # print(search_star[index])
        # print(search_online[index])
        # print(search_address[index])
        # print(search_imageurl[index])
        # print(search_website[index])
        id += 1
    search_imageurl.update( {user_id : spe_search_imageurl} )
    search_star.update({user_id : spe_search_star})
    search_online.update({user_id : spe_search_online})
    search_website.update({user_id : spe_search_website})
    search_address.update({user_id : spe_search_address})
    search_name.update({user_id : spe_search_name})
    index.update( {user_id : id} )

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_menu(self, event):
        text = event.message.text
        return text == "主選單"

    def is_going_to_show_fsm_pic(self, event):
        text = event.message.text
        return text.lower() == "fsm"

    def is_going_to_search_restaurant(self, event):
        user_id = event.source.user_id
        key = event.message.text
        global keyword
        keyword.update( { user_id : key } )

        #check is chinese
        for _char in key:
            if not '\u4e00' <= _char <= '\u9fa5' :
                return  False
        return True

    def on_enter_input_key(self, event):
        send_text_message(event.reply_token, '請輸入你現在想吃什麼(例如火鍋、牛肉、飲料等等)(限中文)')

    # back------------------------------------------------------
    def is_going_to_back_input_key(self , event):
        text = event.message.text
        return text == "返回重新輸入餐廳類別"

    def is_going_to_back_search_restaurant(self , event):
        text = event.message.text
        return text == "返回查詢結果"

    def is_going_to_back_show_favorite(self , event):
        text = event.message.text
        return text == "返回我的最愛清單"
    # ---------------------------------------------------------

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

    def on_enter_search_restaurant(self, event):
        reply_token = event.reply_token
        user_id = event.source.user_id
        get_restaurant_now(user_id)

        id = index[user_id]
        img_array = search_imageurl[user_id]
        name_array = search_name[user_id]
        star_array = search_star[user_id]
        online_array = search_online[user_id]
        website_array = search_website[user_id]
        address_array = search_address[user_id]

        if id != 0 :
            message = message_template.restaurant_list
            message["contents"].clear()
            first_message = copy.deepcopy(message_template.first_item)
            msg = "共查到" + str(id) + "間正在營業的餐廳(最多10間)"
            first_message["body"]["contents"][0]["text"] = msg
            message["contents"].append(first_message)
            for i in range (id):
                new_message = copy.deepcopy(message_template.restaurant_item)
                new_message["hero"]["url"] = img_array[i]
                new_message["body"]["contents"][0]["text"] = name_array[i]
                new_message["body"]["contents"][1]["contents"][0]["contents"][1]["text"] = star_array[i]
                new_message["body"]["contents"][1]["contents"][1]["contents"][1]["text"] = address_array[i]
                new_message["body"]["contents"][1]["contents"][2]["contents"][1]["text"] = online_array[i]
                new_message["footer"]["contents"][0]["action"]["uri"] = website_array[i]
                # record data
                new_message["footer"]["contents"][2]['action']["data"] = "加入最愛," + website_array[i]
                message["contents"].append(new_message)
            message_to_reply = FlexSendMessage("查詢店家資訊", message)
            line_bot_api = LineBotApi( channel_access_token )
            line_bot_api.reply_message(reply_token, message_to_reply)
        else :
            message_to_reply = FlexSendMessage("查詢店家資訊", message_template.no_result)
            line_bot_api = LineBotApi( channel_access_token )
            line_bot_api.reply_message(reply_token, message_to_reply)

    # 加入最愛-----------------------------------------------------------------------
    def is_going_to_add_favorite(self , event):
        text = event.postback.data
        add_or_delete = text.split(',')[0]
        return add_or_delete == '加入最愛'

    def on_enter_add_favorite(self, event):
        user_id = event.source.user_id
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
        index = 0
        msg = ""

        name_array = []
        img_array = []
        star_array = []
        address_array = []
        online_array = []
        web_array = []
        if favorite_index.__contains__(user_id):
            index = favorite_index[user_id]
            name_array = favorite_name[user_id]
            img_array = favorite_imageurl[user_id]
            star_array = favorite_star[user_id]
            address_array = favorite_address[user_id]
            online_array = favorite_online[user_id]
            web_array = favorite_website[user_id]

        for tmp_name in name_array :
            if tmp_name == name :
                msg = '已在我的最愛!'
                has_data = True
                break
        if has_data == False :
            if index < 10:
                img_array.append(img)
                name_array.append(name)
                star_array.append(star)
                address_array.append(address)
                online_array.append(online)
                web_array.append(website)
                index += 1
                msg = '成功加入我的最愛'
            else:
                msg = '我的最愛已滿(最多10個)'
    
        favorite_imageurl.update( {user_id : img_array} )
        favorite_star.update({user_id : star_array})
        favorite_online.update({user_id : online_array})
        favorite_website.update({user_id : web_array})
        favorite_address.update({user_id : address_array})
        favorite_name.update({user_id : name_array})
        favorite_index.update( {user_id : index} )

        message = message_template.add_reply
        message["body"]["contents"][0]["text"] = msg
        message_to_reply = FlexSendMessage("加入最愛", message)
        line_bot_api = LineBotApi( channel_access_token )
        line_bot_api.reply_message(reply_token, message_to_reply)
    # ----------------------------------------------------------------------------------------------------
    
    # 查詢最愛-----------------------------------------------------------------------
    def is_going_to_show_favorite(self , event):
        text = event.message.text
        return text == "查看我的最愛"

    def on_enter_show_favorite(self, event):
        user_id = event.source.user_id
        reply_token = event.reply_token
        global favorite_index

        index = 0
        name_array = []
        img_array = []
        star_array = []
        address_array = []
        online_array = []
        web_array = []
        if favorite_index.__contains__(user_id):
            index = favorite_index[user_id]
            name_array = favorite_name[user_id]
            img_array = favorite_imageurl[user_id]
            star_array = favorite_star[user_id]
            address_array = favorite_address[user_id]
            online_array = favorite_online[user_id]
            web_array = favorite_website[user_id]

        if index != 0 :
            message = message_template.restaurant_list
            message["contents"].clear()
            first_message = copy.deepcopy(message_template.first_favorite)
            msg = "共查到" + str(index) + "間您儲存的最愛餐廳(最多10間)"
            first_message["body"]["contents"][0]["text"] = msg
            message["contents"].append(first_message)
            for i in range (index):
                new_message = copy.deepcopy(message_template.favorite_item)
                new_message["hero"]["url"] = img_array[i]
                new_message["body"]["contents"][0]["text"] = name_array[i]
                new_message["body"]["contents"][1]["contents"][0]["contents"][1]["text"] = star_array[i]
                new_message["body"]["contents"][1]["contents"][1]["contents"][1]["text"] = address_array[i]
                new_message["body"]["contents"][1]["contents"][2]["contents"][1]["text"] = online_array[i]
                new_message["footer"]["contents"][0]["action"]["uri"] = web_array[i]
                # record data
                new_message["footer"]["contents"][2]['action']["data"] = "從我的最愛移除," + web_array[i]
                message["contents"].append(new_message)
            message_to_reply = FlexSendMessage("查詢我的最愛", message)
            line_bot_api = LineBotApi( channel_access_token )
            line_bot_api.reply_message(reply_token, message_to_reply)
        else :
            message_to_reply = FlexSendMessage("查詢我的最愛", message_template.no_favorite)
            line_bot_api = LineBotApi( channel_access_token )
            line_bot_api.reply_message(reply_token, message_to_reply)
    # ----------------------------------------------------------------------------------------------------

    # 刪除最愛-----------------------------------------------------------------------
    def is_going_to_delete_favorite(self , event):
        text = event.postback.data
        add_or_delete = text.split(',')[0]
        return add_or_delete == '從我的最愛移除'

    def on_enter_delete_favorite(self, event):
        user_id = event.source.user_id
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

        index = 0
        name_array = []
        img_array = []
        star_array = []
        address_array = []
        online_array = []
        web_array = []
        if favorite_index.__contains__(user_id):
            index = favorite_index[user_id]
            name_array = favorite_name[user_id]
            img_array = favorite_imageurl[user_id]
            star_array = favorite_star[user_id]
            address_array = favorite_address[user_id]
            online_array = favorite_online[user_id]
            web_array = favorite_website[user_id]

        for tmp_name in name_array :
            if tmp_name == name :
                has_data = True
                break
        if has_data == True :
            if index > 0:
                img_array.remove(img)
                name_array.remove(name)
                star_array.remove(star)
                address_array.remove(address)
                online_array.remove(online)
                web_array.remove(website)
                index -= 1
                msg = '成功從我的最愛中移除'
            else :
                msg = "我的最愛中無資料哦~"
        else :
            msg = "我的最愛中無此資料哦~"

        favorite_imageurl.update( {user_id : img_array} )
        favorite_star.update({user_id : star_array})
        favorite_online.update({user_id : online_array})
        favorite_website.update({user_id : web_array})
        favorite_address.update({user_id : address_array})
        favorite_name.update({user_id : name_array})
        favorite_index.update( {user_id : index} )

        message = message_template.delete_reply
        message["body"]["contents"][0]["text"] = msg
        message_to_reply = FlexSendMessage("加入最愛", message)
        line_bot_api = LineBotApi( channel_access_token )
        line_bot_api.reply_message(reply_token, message_to_reply)
    # ----------------------------------------------------------------------------------------------------
    
    def on_enter_introduction(self, event):
        reply_token = event.reply_token
        message = message_template.introduction_message
        message_to_reply = FlexSendMessage("功能介紹與使用說明", message)
        line_bot_api = LineBotApi( channel_access_token )
        line_bot_api.reply_message(reply_token, message_to_reply)

