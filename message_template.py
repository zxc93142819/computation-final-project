
main_menu = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/4HFOPeR.png",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "1.25:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "功能介紹與使用說明",
              "text": "功能介紹與使用說明"
            },
            "height": "md",
            "color": "#ff9900",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_kags6idO74w3nBXNf_wjgbG5HJtwFB9hNQ&usqp=CAU",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "1.25:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "查詢店家資訊",
              "text": "查詢店家資訊"
            },
            "height": "md",
            "color": "#ff6666",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqDZwJPxo5y6aAzVyQuCCX8heLEf7RzOoENg&usqp=CAU",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "1.25:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "我的最愛",
              "text": "查看我的最愛"
            },
            "height": "md",
            "color": "#ff66b3",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    },
  ]
}

show_pic = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "giga",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/6w5d9ih.png",
        "aspectMode": "fit",
        "size": "full",
        "aspectRatio": "2:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "前往網頁看圖片",
              "uri": "https://i.imgur.com/6w5d9ih.png"
            },
            "height": "md",
            "color": "#5cd65c",
            "style": "primary"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "返回主選單",
              "text": "主選單"
            },
            "height": "md",
            "color": "#00cc66",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    }
  ]
}

no_result = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "查無相關店家",
        "weight": "bold",
        "size": "xl",
        "margin": "lg",
        "align": "center"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "message",
          "label": "返回主選單",
          "text": "主選單"
        }
      }
    ]
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}

recommend_message = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "推薦程度",
        "weight": "bold",
        "size": "xl",
        "margin": "md"
      },
      {
        "type": "text",
        "text": "(台幣換成日幣)"
      },
      {
        "type": "separator",
        "margin": "xxl"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "xxl",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "最近三個月前五點",
                "size": "md",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": "否",
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "最近兩週前三低點",
                "size": "md",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "否",
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "separator",
            "margin": "xxl"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "推薦程度",
                "size": "md",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "低",
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "message",
          "label": "返回主選單",
          "text": "主選單"
        }
      }
    ]
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}

introduction_message = {
  "type": "bubble",
  "size": "giga",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "功能介紹",
        "weight": "bold",
        "size": "lg",
        "margin": "lg",
        "align": "center"
      },
      {
        "type": "text",
        "text": "1. 依據你輸入的關鍵字(想吃什麼)，查詢台南現在正營業的店家資訊(會查給你十間餐廳)",
        "wrap": True
      },
      {
        "type": "text",
        "text": "2. 可將自己去過的店家加入最愛(最多儲存10個)",
        "wrap": True
      },
      {
        "type": "text",
        "text": "3. 輸入「fsm」查看fsm結構圖",
        "wrap": True
      },
      {
        "type": "text",
        "text": "使用說明",
        "weight": "bold",
        "size": "lg",
        "margin": "lg",
        "align": "center"
      },
      {
        "type": "text",
        "text": "◎　輸入「主選單」來開始所有操作(或是按下方menu以呼叫主選單",
        "wrap": True
      },
      {
        "type": "text",
        "text": "◎　也可利用下方按鈕進行操作",
        "wrap": True
      },
      {
        "type": "text",
        "text": "◎　操作時請拖曳橫向(左右)滑動以查看更多呦~",
        "wrap": True
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "message",
          "label": "返回主選單",
          "text": "主選單"
        }
      }
    ]
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}

restaurant_item = {
    "type": "bubble",
    "hero": {
      "type": "image",
      "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
      "size": "full",
      "aspectRatio": "20:13",
      "aspectMode": "cover",
      "action": {
        "type": "uri",
        "uri": "http://linecorp.com/"
      }
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": "Brown Cafe",
          "weight": "bold",
          "size": "xl",
          "flex":1
        },
        {#["body"]["contents"][1]
          "type": "box",
          "layout": "vertical",
          "margin": "lg",
          "spacing": "sm",
          "contents": [
            {#["body"]["contents"][1]["contents"][0]
              "type": "box",
              "layout": "baseline",
              "contents": [
                {
                  "type": "text",
                  "text": "店家評價",
                  "size": "sm",
                  "color": "#999999",
                  "flex": 2
                },
                {
                  "type": "text",
                  "text": "4.0",
                  "size": "sm",
                  "color": "#999999",
                  "flex": 5
                }
              ]
            },
            {
              "type": "box",
              "layout": "baseline",
              "spacing": "sm",
              "contents": [
                {
                  "type": "text",
                  "text": "店家地址",
                  "color": "#aaaaaa",
                  "size": "sm",
                  "flex": 2
                },
                {
                  "type": "text",
                  "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
                  "wrap": True,
                  "color": "#666666",
                  "size": "sm",
                  "flex": 5
                }
              ]
            },
            {
              "type": "box",
              "layout": "baseline",
              "spacing": "sm",
              "contents": [
                {
                  "type": "text",
                  "text": "營業時間",
                  "color": "#aaaaaa",
                  "size": "sm",
                  "flex": 2
                },
                {
                  "type": "text",
                  "text": " ",
                  "wrap": True,
                  "color": "#666666",
                  "size": "sm",
                  "flex": 5
                }
              ]
            }
          ]
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "vertical",
      "spacing": "sm",
      "contents": [
        {
          "type": "button",
          "style": "link",
          "height": "sm",
          "action": {
            "type": "uri",
            "label": "查看店家",
            "uri": "https://linecorp.com"
          }
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [],
          "margin": "sm"
        },
        {
          "type": "button",
          "style": "link",
          "height": "sm",
          "action": {
            "type": "postback",
            "label": "加入最愛",
            "data": "hello",
          }
        }
      ],
      "flex": 0
    },
}

restaurant_list = {
  "type": "carousel",
  "contents": [
    {
    "type": "bubble",
    "hero": {
      "type": "image",
      "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
      "size": "full",
      "aspectRatio": "20:13",
      "aspectMode": "cover",
      "action": {
        "type": "uri",
        "uri": "http://linecorp.com/"
      }
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": "Brown Cafe",
          "weight": "bold",
          "size": "xl"
        },
        {#["body"]["contents"][1]
          "type": "box",
          "layout": "vertical",
          "margin": "lg",
          "spacing": "sm",
          "contents": [
            {#["body"]["contents"][1]["contents"][0]
              "type": "box",
              "layout": "baseline",
              "contents": [
                {
                  "type": "text",
                  "text": "店家評價",
                  "size": "sm",
                  "color": "#999999",
                  "flex": 2
                },
                {
                  "type": "text",
                  "text": "4.0",
                  "size": "sm",
                  "color": "#999999",
                  "flex": 5
                }
              ]
            },
            {
              "type": "box",
              "layout": "baseline",
              "spacing": "sm",
              "contents": [
                {
                  "type": "text",
                  "text": "店家地址",
                  "color": "#aaaaaa",
                  "size": "sm",
                  "flex": 2
                },
                {
                  "type": "text",
                  "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
                  "wrap": True,
                  "color": "#666666",
                  "size": "sm",
                  "flex": 5
                }
              ]
            },
            {
              "type": "box",
              "layout": "baseline",
              "spacing": "sm",
              "contents": [
                {
                  "type": "text",
                  "text": "營業時間",
                  "color": "#aaaaaa",
                  "size": "sm",
                  "flex": 2
                },
                {
                  "type": "text",
                  "text": "10:00 - 23:00",
                  "wrap": True,
                  "color": "#666666",
                  "size": "sm",
                  "flex": 5
                }
              ]
            }
          ]
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "vertical",
      "spacing": "sm",
      "contents": [
        {
          "type": "button",
          "style": "link",
          "height": "sm",
          "action": {
            "type": "uri",
            "label": "查看店家",
            "uri": "https://linecorp.com"
          }
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [],
          "margin": "sm"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "加入最愛",
            "uri": "http://linecorp.com/"
          },
          "style": "link",
          "height": "sm"
        }
      ],
      "flex": 0
    },
}
  
  ]
}

no_favorite = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "沒有最愛店家哦~~",
        "weight": "bold",
        "size": "xl",
        "margin": "lg",
        "align": "center"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "message",
          "label": "返回主選單",
          "text": "主選單"
        }
      }
    ]
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}

favorite_item = {
    "type": "bubble",
    "hero": {
      "type": "image",
      "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
      "size": "full",
      "aspectRatio": "20:13",
      "aspectMode": "cover",
      "action": {
        "type": "uri",
        "uri": "http://linecorp.com/"
      }
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": "Brown Cafe",
          "weight": "bold",
          "size": "xl"
        },
        {#["body"]["contents"][1]
          "type": "box",
          "layout": "vertical",
          "margin": "lg",
          "spacing": "sm",
          "contents": [
            {#["body"]["contents"][1]["contents"][0]
              "type": "box",
              "layout": "baseline",
              "contents": [
                {
                  "type": "text",
                  "text": "店家評價",
                  "size": "sm",
                  "color": "#999999",
                  "flex": 2
                },
                {
                  "type": "text",
                  "text": "4.0",
                  "size": "sm",
                  "color": "#999999",
                  "flex": 5
                }
              ]
            },
            {
              "type": "box",
              "layout": "baseline",
              "spacing": "sm",
              "contents": [
                {
                  "type": "text",
                  "text": "店家地址",
                  "color": "#aaaaaa",
                  "size": "sm",
                  "flex": 2
                },
                {
                  "type": "text",
                  "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
                  "wrap": True,
                  "color": "#666666",
                  "size": "sm",
                  "flex": 5
                }
              ]
            },
            {
              "type": "box",
              "layout": "baseline",
              "spacing": "sm",
              "contents": [
                {
                  "type": "text",
                  "text": "營業時間",
                  "color": "#aaaaaa",
                  "size": "sm",
                  "flex": 2
                },
                {
                  "type": "text",
                  "text": "10:00 - 23:00",
                  "wrap": True,
                  "color": "#666666",
                  "size": "sm",
                  "flex": 5
                }
              ]
            }
          ]
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "vertical",
      "spacing": "sm",
      "contents": [
        {
          "type": "button",
          "style": "link",
          "height": "sm",
          "action": {
            "type": "uri",
            "label": "查看店家",
            "uri": "https://linecorp.com"
          }
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [],
          "margin": "sm"
        },
        {
          "type": "button",
          "style": "link",
          "height": "sm",
          "action": {
            "type": "postback",
            "label": "從我的最愛移除",
            "data": "hello",
          }
        }
      ],
      "flex": 0
    },
}

add_reply = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "查無相關店家",
        "weight": "bold",
        "size": "xl",
        "margin": "lg",
        "align": "center"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "message",
          "label": "返回查詢結果",
          "text": "返回查詢結果"
        }
      },
      {
        "type" : "separator"
      },
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "message",
          "label": "返回主選單",
          "text": "主選單"
        }
      },
    ]
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}

delete_reply = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "查無相關店家",
        "weight": "bold",
        "size": "xl",
        "margin": "lg",
        "align": "center"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "message",
          "label": "返回我的最愛清單",
          "text": "返回我的最愛清單"
        }
      },
      {
        "type" : "separator"
      },
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "message",
          "label": "返回主選單",
          "text": "主選單"
        }
      },
    ]
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}

first_favorite = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "Brown Cafe",
        "weight": "bold",
        "size": "xl",
        "wrap":True,
        "flex":1
      },
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "box",
        "layout": "baseline",
        "margin": "md",
        "contents": [
          {
            "type": "text",
            "text": " ",
            "size": "sm",
            "color": "#999999",
            "margin": "md",
            "flex": 0
          }
        ]
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "返回主選單",
          "text": "主選單"
        },
        "height": "md",
        "color": "#00cc66",
        "style": "primary"
      }
    ],
    "flex": 0
  }
}

first_item = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "Brown Cafe",
        "weight": "bold",
        "size": "xl",
        "wrap":True,
        "flex":1
      },
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "box",
        "layout": "baseline",
        "margin": "md",
        "contents": [
          {
            "type": "text",
            "text": " ",
            "size": "sm",
            "color": "#999999",
            "margin": "md",
            "flex": 0
          }
        ]
      },
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "message",
          "label": "返回重新輸入餐廳類別",
          "text": "返回重新輸入餐廳類別"
        }
      },
      {
        "type" : "separator"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "返回主選單",
          "text": "主選單"
        },
        "height": "md",
        "color": "#00cc66",
        "style": "primary"
      }
    ],
    "flex": 0
  }
}
