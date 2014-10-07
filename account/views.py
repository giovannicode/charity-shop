from django.shortcuts import render, redirect

def signup(request):
  if request.method == 'GET':
    form = UserCreatorForm
    return render(request, 'account/signup.html', {'form': form})

  elif request.method == 'POST':
    form = UserCreatorForm(request.POST)

    if form.is_valid():
      user = form.save()
      return redirect('account:account_login')
    else:
      return render(request, 'account/signup.html', {'form': form})
