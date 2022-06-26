
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from .models import  Choice,Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


'''def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    
    #template = loader.get_template('polls/index.html')
    #latest_question_list = Question.objects.all()
    #output = ','.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
   
    context = {
        'latest_question_list': latest_question_list,
        
   
    }
    #return HttpResponse(template.render(context,request))
    return render(request,'polls/index.html',context)

def detail(request, question_id):
    #try:
        #question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
        #raise Http404("Question does not exist")
    #return render(request,'polls/detail.html',{'question':question})
    question = get_object_or_404(Question, pk = question_id)
    return render(request,'polls/detail.html',{'question': question})

  

def results(request,question_id):
    #response = 'you are looking at the results of question %s.'
    #return HttpResponse(response % question_id)
    #question = get_object_or_404(Question,pk=question_id)
    question = Question(pk=question_id)
    return render(request,'polls/results.html',{'question':question})'''

    
def vote(request,question_id):
    #return HttpResponse('you are voting on question %s.'% question_id)
    question = get_object_or_404(Question, pk=question_id)
   

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
       
    except KeyError:
        
        return render(request,'polls/vote.html',{'question':question,
        'error_message':
        'You did not select  choice.',})
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))      