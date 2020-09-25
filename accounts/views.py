from django.views.generic import TemplateView

class AboutpageView(TemplateView):
	template_name = 'register.html'
class RowPage(TemplateView):
    template_name='user_registration.html'