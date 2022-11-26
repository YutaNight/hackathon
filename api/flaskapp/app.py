from flask import Flask, request, render_template, url_for, redirect, session, jsonify
from static import config
import fitbit
from ast import literal_eval
import pandas as pd
import json
import datetime
import traceback
import logging
from models.form import UserInformation

# from models.form import UserInformation
from models.fitbitinfo import FitbitInfo

# 1.Flaskサーバーを立ち上げる
app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

answer_dict = config.answer_dict

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
streamHandler = logging.StreamHandler()
logger.addHandler(streamHandler)
formatter = logging.Formatter('***** %(asctime)s %(levelname)s: %(message)s *****')
streamHandler.setFormatter(formatter)

#3. 初期値のURL('/')からどこかの画面へ移る
@app.route('/api/home')
def home():
    return '<h2>Hello Flask+uWSGI+Nginx</h2>'

@app.route('/api/form', methods=['GET', 'POST'])
def get_user_data():
    form = UserInformation(request.form)
    if request.method == 'POST':
        logger.debug(request.form)
        logger.debug('DATA IS POSTED FROM {}'.format(request.remote_addr))
        session['gender'] = form.gender.data
        session['population'] = form.population.data
        session['age'] = form.age.data
        session['background'] = form.background.data
        session['income'] = form.income.data
        session['family1'] = form.family1.data
        session['family2'] = form.family2.data
        session['family3'] = form.family3.data
        session['housemate'] = form.housemate.data
        session['alone'] = form.alone.data
        session['exercise'] = form.exercise.data
        session['work'] = form.work.data
        session['sleep'] = form.sleep.data
        session['personality'] = form.personality.data
        session['cigarettes'] = form.cigarettes.data
        session['weight'] = form.weight.data
        logger.debug('REDIRECT TO RESULT')
        return redirect(url_for('result'))
    logger.debug('ACCESSED FROM {}'.format(request.remote_addr))
    return render_template('home.html', form=form)

@app.route('/result')
def result():
    logger.debug('START CALCULATION LIFE SPAN!')
    life_span = 79 if session['gender'] == 'male' else 86
    for label in answer_dict.keys():
        life_span += answer_dict[label][session[label]]
    logger.debug('END OF CALCULATION!')
    return render_template('result.html', life_span=life_span)

@app.route('/api/calculate')
def show_result():
    try:
        # 1週間の定義
        end_time = datetime.date.today()
        start_time = end_time - datetime.timedelta(days=6)
        # インスタンス化
        my_info = FitbitInfo(str(start_time), str(end_time))
        # fitbitから取得した値のセット
        my_info.sleep_time = my_info.get_sleep_data()
        my_info.exercise_count = my_info.get_activity_data()
        my_info.about_me = my_info.get_user_data()
        user_info = {
            "exercise_count": my_info.exercise_count,
            "average_sleep_time": my_info.sleep_time,
            "about_me": my_info.about_me
        }
        calculate_result = calculate_life(user_info)
        res = {
            'status': 'OK',
            'data': {
                'lifeSpan': calculate_result,
                'info': user_info
            }
        }
        
        return jsonify(res)
    
    except Exception as e:
        return traceback.format_exc()
        # return 'NG'

def calculate_life(data):
    try:
        exclusion_list = ['age', 'city', 'city_kind', 'gender', 'normal_weight', 'weight']
        life_span = 79 if data['about_me']['gender'] == 'MALE' else 86
        for k, v in data['about_me'].items():
            if k not in exclusion_list:
                life_span += answer_dict[k][v]
            elif k == 'city_kind':
                life_span = life_span - 2 if v > 0 else life_span
            else:
                pass
        tmp = abs(data['about_me']['weight'] - data['about_me']['normal_weight'])
        if tmp >= 25:
            life_span -= 8
        elif tmp >= 15:
            life_span -= 4
        elif tmp >= 5:
            life_span -= 2
        else:
            pass
        
        return life_span
    
    except Exception as e:
        print('error', e)
        return 'NG'

@app.route('/api/test')
def test():
    return '<h1>デプロイ自動化テスト</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    # app.run(debug=True)