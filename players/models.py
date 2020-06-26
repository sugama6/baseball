from django.db import models

class Team(models.Model):
    team_id = models.AutoField(primary_key=True, default=0)
    team_nm = models.CharField(max_length=30)
    league = models.CharField(max_length=1)
    stadium = models.CharField(max_length=30)
    address = models.CharField(max_length=50,null=True)
    league_v = models.IntegerField()
    japan_v = models.IntegerField()
    owner = models.CharField(max_length=30)
    img = models.TextField(null=True)
    address_url = models.TextField(null=True)
    
    def __str__(self):
        return str(self.team_nm) + ',' +\
            str(self.league) + '・リーグ,' +\
            '本拠地: ' + str(self.stadium) + ',' +\
            'リーグ優勝回数: ' + str(self.league_v) + '回,' +\
            '日本一回数: ' + str(self.japan_v) + '回' +\
            '球団代表: ' + str(self.owner)

class Player(models.Model):
    player_id = models.AutoField(primary_key=True, default=0)
    team_id = models.IntegerField()
    number = models.IntegerField()
    player_nm = models.CharField(max_length=100)
    player_kana = models.CharField(max_length=100)
    position = models.CharField(max_length=10)
    birthday = models.DateField()
    age = models.IntegerField()
    blood = models.CharField(max_length=10)
    height = models.FloatField(max_length=3)
    weight = models.FloatField(max_length=3)
    hit_throw = models.CharField(max_length=2)
    draft_year = models.IntegerField()
    draft_rank =  models.CharField(max_length=30)
    join_year = models.IntegerField()
    career = models.CharField(max_length=200)
    award = models.CharField(max_length=200)
    video = models.URLField(null=True)
    img = models.TextField(null=True)
    
    def __str__(self):
        return str(self.player_id)
# Create your models here.
