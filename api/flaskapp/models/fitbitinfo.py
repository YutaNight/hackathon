import json
import fitbit
import datetime
from statistics import mean
from ast import literal_eval
from models.resasinfo import ResasInfo
import traceback

class FitbitInfo:
    # 定数定義
    CLIENT_ID = "238JFN"
    CLIENT_SECRET = "453110fd88880307fb7f25a41060f9ec"
    USER_ID = "B4657W"
    TOKEN_FILE = 'token.txt'
    
    def __init__(self, date_s, date_e):
        """Initialize the FitbitInfo

        Args:
            date_s (String): start date
            date_e (String): end date
        """
        tokens = open(self.TOKEN_FILE).read()
        token_dict = literal_eval(tokens)
        self.access_token = token_dict['access_token']
        self.refresh_token = token_dict['refresh_token']
        self.date_s = datetime.datetime.strptime(date_s, '%Y-%m-%d')
        self.date_e = datetime.datetime.strptime(date_e, '%Y-%m-%d')        
    
    def update_token(self, token):
        print(token)
        with open(self.TOKEN_FILE, 'w') as f:
            print(str(token))
            f.write(str(token))
    
    def get_sleep_data(self):
        try:
            # トークンの有効期限が切れていた場合はupdate_tokenにて更新
            client = fitbit.Fitbit(
                        self.CLIENT_ID,
                        self.CLIENT_SECRET,
                        access_token=self.access_token,
                        refresh_token=self.refresh_token,
                        refresh_cb=self.update_token
                        )
            res = client.time_series("sleep", base_date=self.date_s, end_date=self.date_e)
            target_list = []
            print(res)
                
            for data in res['sleep']:
                if 'isMainSleep' in data and data['isMainSleep'] == True:
                    target_list.append(data['timeInBed'])
            avrg_sleep = mean(target_list)
            return avrg_sleep
        except Exception as e:
            with open('./log', 'a') as f:
                f.write(traceback.format_exc())
            return 'NG'
    
    def get_activity_data(self):
        client = fitbit.Fitbit(
            self.CLIENT_ID,
            self.CLIENT_SECRET,
            access_token=self.access_token,
            refresh_token=self.refresh_token,
            refresh_cb=self.update_token
            )
        res = client.time_series("activities/heart", base_date=self.date_s, end_date=self.date_e)
        print(res)
        target_count = 0
        for daily_data in res['activities-heart']:
            target_data = [data for data in daily_data['value']['heartRateZones'] if data['name'] in ['Fat Burn', 'Cardio', 'Peak']]
            total_time = 0
            for data in target_data:
                total_time += data['minutes']
            if total_time > 30:
                target_count += 1
        return target_count
    
    def get_user_data(self):
        client = fitbit.Fitbit(
            self.CLIENT_ID,
            self.CLIENT_SECRET,
            access_token=self.access_token,
            refresh_token=self.refresh_token,
            refresh_cb=self.update_token
            )
        res = client.user_profile_get()
        age = res['user']['age']
        # 'MALE' or 'FEMALE'
        gender = res['user']['gender']
        # convert from inch to cm
        height = res['user']['height'] * 2.54
        # convert from pound to kg
        weight = res['user']['weight'] / 2.2046
        normal_weight = (height - 100) * 0.9
        about_me = json.loads(res['user']['aboutMe'])
        about_me['age'] = age
        about_me['gender'] = gender
        about_me['weight'] = weight
        about_me['normal_weight'] = normal_weight
        # print(json.dumps(about_me, indent=4))
        city = about_me['city']
        city_info = ResasInfo(13)
        about_me['city_kind'] = int(city_info.get_cities_data(city))
        return about_me