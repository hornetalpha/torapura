from django import forms
from .models import Plan

class PlanSearchForm(forms.Form):
    place = forms.ChoiceField(
        choices=[('', '都道府県を選択してください')] + [
        ('北海道', '北海道'),
        ('青森県', '青森県'),
        ('岩手県', '岩手県'),
        ('秋田県', '秋田県'),
        ('宮城県', '宮城県'),
        ('山形県', '山形県'),
        ('栃木県', '栃木県'),
        ('和歌山県', '和歌山県'),
        ('島根県', '島根県'),
        ('高知県', '高知県'),
        ('愛媛県', '愛媛県'),
        ('長崎県', '長崎県'),
        ('大分県', '大分県'),
        ('熊本県', '熊本県'),
        ('鹿児島県', '鹿児島県'),
    ],
    initial='')

    done = forms.ChoiceField(
        choices=[('', 'ジャンルを選択してください')] + [
        ('activity', 'スポーツ'),
        ('sightseeing', '観光'),
    ],
    initial='')

    person = forms.ChoiceField(
        choices=[('', '旅行人数を選択してください')] + [
        ('1～2人', '1～2人'),
        ('3人以上', '3人以上'),
    ],
    initial='')

    day = forms.ChoiceField(
        choices=[('', '旅行日数を選択してください')] + [
        ('日帰り', '日帰り'),
        ('1泊2日', '1泊2日'),
        ('2泊3日', '2泊3日'),
        ('3泊4日', '3泊4日'),
    ],
    initial='')

    keyword = forms.CharField(
        required=False,
        label='キーワード',
        widget=forms.TextInput(attrs={'placeholder': 'キーワードを入力'}))
