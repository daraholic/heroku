#!/usr/bin/env python3
from flask import Flask
app=Flask(__name__) #__name__代表目前執行的模組
@app.route("/") #Decorator
def home():
    return "Hello Flask"
@app.route("/test") #Decorator
def test():
    return "Just Test" #處理網站路徑
if __name__=="__main__":
    app.run() #立刻啟動伺服器

