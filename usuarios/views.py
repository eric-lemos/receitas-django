from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha1 = request.POST['password']
        senha2 = request.POST['password2']

        if not nome.strip():
            print('O campo nome não pode ficar em branco.')
            return redirect('cadastro')

        if not email.strip():
            print('O campo email não pode ficar em branco.')
            return redirect('cadastro')

        if not senha1 != senha2:
            print('As senhas não são iguais.')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            print('Este usuário já existe!')
            return redirect('cadastro')

        user = User.objects.create_user(
            username=nome, email=email, password=senha1)
        user.save()

        print('Usuário cadastrado com sucesso!')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    # if request.method == 'POST':
    #     usuario = request.POST['username']
    #     senha = request.POST['password']

    #     entrar =  authenticate(
    #         username=usuario, password=senha)
        
    #     if entrar is not None:
    #         pass
    #     else:
    #         pass
        
    # else:
    return render(request, 'usuarios/login.html')

def dashboard(request):
    pass

def logout(request):
    pass
