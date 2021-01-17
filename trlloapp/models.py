from django.db import models

# Create your models here.
class Team_Type(models.Model):
    team_type_name=models.CharField(max_length=200)
    def __str__(self):
        return self.team_type_name
class Team(models.Model):
    team_name=models.CharField(max_length=200,unique=True,primary_key=True)
    team_type=models.ForeignKey(Team_Type,on_delete=models.CASCADE)
    team_description=models.TextField()

    def __str__(self):
        return self.team_name

class Board(models.Model):
    TEAM_VISIBLE=(('private','Private'),('public','Public'))
    board_title=models.CharField(max_length=200)
    team=models.ForeignKey(Team,to_field='team_name', on_delete=models.CASCADE)
    team_visible=models.CharField(max_length=20,choices=TEAM_VISIBLE)
    def __str__(self):
        return self.board_title