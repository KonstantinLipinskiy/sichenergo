from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login 
from django.contrib import messages 

def entrance(request): 
	if request.method == "POST": 
		username = request.POST['username'] 
		password = request.POST['password'] 
		# Аутентификация пользователя 
		user = authenticate(request, username=username, password=password) 
		if user is not None: 
			# Если аутентификация успешна, выполняем вход пользователя 
			login(request, user) 
			# Перенаправляем на страницу администратора 
			return redirect('/admin/') 
		else: 
			# Если аутентификация не удалась, выводим сообщение об ошибке 
			messages.error(request, 'Неверное имя пользователя или пароль.') 
			# Если метод запроса GET, просто рендерим шаблон 
	
	context = { 'title': 'Вхід', } 
	
	return render(request, 'entrance/entrance.html', context)
