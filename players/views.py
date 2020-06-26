from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Team, Player
from django.db.models import Q
from .forms import FindForm
from django.views import generic


#home.html 画面
#class TeamList(ListView):
#    print("-- class TeamList(ListView): --")
#    template_name = 'home.html'
#    model = Team
#    def get_queryset(self):
#        return Team.objects.order_by('pk')

#start.html
def start(request):
    return render(request, 'start.html')

class TeamList(ListView, generic.edit.FormMixin):
    print("-- class TeamList(ListView): --")
    template_name = 'home.html'
    model = Team
    form_class = FindForm

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_queryset(self):
        return Team.objects.order_by('pk')


#team.html 画面
class TeamDetail(DetailView, generic.edit.FormMixin):
    print("-- class TeamDetail(DetailView): --")
    template_name = 'team.html'
    model = Team
    form_class = FindForm
    
    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        self.object_list = self.get_queryset()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'more_context': Player.objects.filter(team_id=self.kwargs['pk']).order_by('number')
        })
        team_list = Team.objects.all().order_by('pk')[:]
        return context
    def get_queryset(self):
        return Team.objects.order_by('pk')

#profile.html 画面
def profile_list(request, pk):
    print("-- profile_list(request, pk): --")
    object = Player.objects.get(pk=pk)
    params = {
        'form': FindForm(),
        'object':object
    }
    return render(request, 'profile.html', params)

#検索画面
class SelectForm(TemplateView): 
    def __init__(self):
        print("-- __init__(self) --")
        self.params = {
            'form': FindForm(),     
        }
    def get(self, request):
        print("-- def get(self, request) --")
        self.params = {
            'form': FindForm(),        
        }
        return render(request, 'find.html', self.params)
        
    def post(self, request):
        print("-- def post(self, request) --")
        ch = request.POST.get('choice')
        find_keyword = request.POST.get('find')
        find = FindForm(request, self)

        if ch == 'one':
            data = Player.objects.filter(Q(player_nm__icontains=find_keyword)|Q(player_kana__icontains=find_keyword))
        elif ch == 'two': #名前
            data = Player.objects.filter(player_nm__icontains=find_keyword)
        elif ch == 'three': #カナ
            data = Player.objects.filter(player_kana__icontains=find_keyword)
        elif ch == 'four': #背番号
            data = Player.objects.filter(number=find_keyword)
        elif ch == 'five': #年齢
            data = Player.objects.filter(age=find_keyword)
        elif ch == 'six': #ドラフト年
            data = Player.objects.filter(draft_year=find_keyword)
        elif ch == 'seven': #ドラフト順位
            data = Player.objects.filter(draft_rank=find_keyword)
        elif ch == 'eight': #タイトル
            data = Player.objects.filter(award__contains=find_keyword)
            
        self.params = {
            'form': FindForm(),
            'data': data,
        }
        return render(request, 'find.html', self.params)

        

       
  

