from django.shortcuts import render

def index(request):
  try:
    request.session['counter']
  except:
    request.session['counter'] = 0
  return render(request, 'surveys/index.html')

def process_form(request):
  request.session['counter'] += 1
  context = {
    'counter'   : request.session['counter'],
    'name'      : request.POST['name'],
    'location'  : request.POST['location'],
    'favorite'  : request.POST['lang'],
    'comments'  : request.POST['comments']
    }
  print context
  return render(request, 'surveys/show.html', context)

