from django.shortcuts import render, redirect
from . forms import *
from django.contrib import messages
# from django.shortcuts import render, redirect
from django.views import generic



# Create your views here.
def home(request):
    return render(request,'dashboard/home.html')

def notes(request):
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            notes = Notes(user=request.user,title=request.POST['title'],description=request.POST['description'])
            notes.save()
        messages.success(request,f"Notes Added from {request.user.username} Succesfully!")
    else:    
        form = NotesForm()
    notes = Notes.objects.filter(user=request.user)
    context = {'notes':notes,'form':form}
    return render(request,'dashboard/notes.html',context)

# def delete_note(request,pk=None):
#     Notes.objects.get(id=pk).delete()
#     return redirect("notes")

def delete_note(request, pk):
    try:
        note = Notes.objects.get(id=pk)
        note.delete()
        return redirect("notes")
    except Notes.DoesNotExist:
    
        return redirect("notes_not_found") 
 
    
# aq wertili schirdeba
class NotesDetailView(generic.DetailView):
    model = Notes







def homework(request):
    if request.method == "POST":
         form = HomeworkForm(request.POST)
         if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished = False
            except:
                finished = False
            homeworks = Homework(
                user = request.user,
                subject = request.POST['subject'],
                title = request.POST['title'],
                description = request.POST['description'],
                due = request.POST['due'],
                is_finished = finished

            ) 
            homeworks.save()    
            messages.success(request,f'Homework Added from{request.user.username}!!!')          
    else:
        form = HomeworkForm()
    homework = Homework.objects.filter(user=request.user)
    if len(homework)==0:
        homework_done = True
    else:
        homework_done = False    

    context = {
               'homeworks':homework,
               'homeworks_done':homework_done,
               'form':form,
               }
    return render(request,'dashboard/homework.html',context)



