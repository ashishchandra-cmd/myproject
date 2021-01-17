from django.shortcuts import render,redirect
from trlloapp.forms import RegisterForm
from django.contrib.auth.models import User
from trlloapp.models import Team,Team_Type,Board


def index_view(request):
    return render(request,'index.html')
def user_home(request):
    team_data=Team.objects.all()
    board_data=Board.objects.all()
    return render(request,'user_home.html',{'team_data':team_data,'board_data':board_data})

def user_login(request):
    urn=request.POST.get("uname")
    pwd=request.POST.get("upassword")
    try:
        user=User.objects.get(username=urn,password=pwd)
        return redirect('user_home')
    except:
        return render(request,'user_login.html')

def user_signup(request):
    form=RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('user_login')
    return render(request,'user_signup.html',{'form':form})

def team_create(request):
    team_type_data=Team_Type.objects.all()
    if request.method=='POST':
        t_name=request.POST['team_name']
        t_type=request.POST['team_type']
        t_des=request.POST['team_description']
        t_tpye_d=Team_Type.objects.filter(team_type_name=t_type).first()
        Team.objects.create(team_name=t_name,team_type=t_tpye_d,team_description=t_des)
        return redirect('user_home')
    return render(request,'team.html',{'team_type_data':team_type_data})

def board_create(request):
    team_name_data=Team.objects.all()
    board_choice_data=Board.objects.all().values('team_visible')
    if request.method=='POST':
        b_title=request.POST['board_name']
        b_team=request.POST['board_team']
        t_vis=request.POST['team_vesible']
        b_teams_t=Team.objects.filter(team_name=b_team).first()
        Board.objects.create(board_title=b_title,team=b_teams_t,team_visible=t_vis)
        return redirect('user_home')
    return render(request,'board.html',{'team_name_data':team_name_data,'board_choice_data':board_choice_data})
