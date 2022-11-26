from wtforms import RadioField, SubmitField
from wtforms.form import Form

class UserInformation(Form):
    gender = RadioField('性別は？', choices=[('male', '男性'), ('female', '女性')])
    population = RadioField('住んでいる町の人口は？', choices=[('many', '人口200万人以上'), ('less', '人口1万人以下'), ('middle', 'その他')])
    age = RadioField('今の年齢は？', choices=[('young', '30歳未満'), ('30s', '30-39歳'), ('40s', '40-49歳'), ('5060s', '50-69歳'), ('elder', '70歳以上')])
    background = RadioField('最終学歴は？', choices=[('university', '大学'), ('graduate', '大学院'), ('other', 'その他')])
    income = RadioField('年収は？', choices=[('normal', '700万以下'), ('high', '700万以上')])
    family1 = RadioField('死亡しているいないにかかわらず祖父母のうち1人でも85歳以上まで生きている？', choices=[('yes', 'はい'), ('no', 'いいえ')])
    family2 = RadioField('死亡しているいないにかかわらず祖父母が4人とも80歳以上まで生きている？', choices=[('yes', 'はい'), ('no', 'いいえ')])
    family3 = RadioField('両親のどちらかが50歳未満で心臓病か脳卒中で亡くなっている？', choices=[('yes', 'はい'), ('no', 'いいえ')])
    housemate = RadioField('誰かと同居している？', choices=[('yes', 'はい'), ('no', 'いいえ')])
    alone = RadioField('一人暮らしの期間は？', choices=[('short', '10年未満'), ('over10', '10年以上20年未満'), ('over20', '20年以上30年未満'), ('long', '30年以上')])
    exercise = RadioField('1日30分以上の運動頻度は？', choices=[('less', '週1以下'), ('normal', '週2-4'), ('many', '週5以上')])
    work = RadioField('仕事内容は？', choices=[('exercise', '体を動かす'), ('desk', 'デスクワーク'), ('house', '主婦/夫'), ('other', 'その他')])
    sleep = RadioField('1日の睡眠時間は？', choices=[('normal', '10時間未満'), ('long', '10時間以上')])
    personality = RadioField('性格は？', choices=[('calm', 'のんびり'), ('angry', '怒りっぽい'), ('other', 'その他')])
    cigarettes = RadioField('煙草は？', choices=[('no', '吸わない'), ('less1', '1日1箱未満'), ('less2', '1日1箱以上2箱未満'), ('many', '1日2箱以上')])
    weight = RadioField('体重-標準体重の絶対値は？※標準体重 = (身長[cm] - 100 * 0.9)', choices=[('1', '25kg以上'), ('2', '15kg以上25kg未満'), ('3', '5kg以上15kg未満'), ('4', '5kg未満')])
    submit = SubmitField('Submit')