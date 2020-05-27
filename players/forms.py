from django import forms
from .models import Team, Player

class FindForm(forms.Form):
    data = [
            ('one', '絞り込み'),
            ('two', '名前'),
            ('three', 'カナ'),
            ('four', '背番号'),
            ('five', '年齢'),
            ('six', 'ドラフト年'),
            ('seven', 'ドラフト順位'),
            ('eight', 'タイトル')
        ]
    choice = forms.ChoiceField(label='絞り込み', choices=data)
    find = forms.CharField(required=False)
    
