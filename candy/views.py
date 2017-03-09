from django.shortcuts import render #render_to_response #turnsbackthewholeline
def base(request):
	title = 'Base'
	context = {
		"title":title,
	}
	return render(request,'base.html',context)