from lib2to3.fixes.fix_input import context

from django.views.generic import TemplateView




class IndexView(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'HELLO WORLD - Главная'
        context['content'] = "Магазин мебели HELLO WORLD"
        return context


class AboutView(TemplateView):
    template_name = 'app/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - О нас'
        context['content'] = "О нас"
        context['text_on_page'] = "Текст о том почему этот магазин такой классный, и какой хороший товар. А админы ваще лучшие"
        return context


class AboutDeliveryView(TemplateView):
    template_name = 'app/about_delivery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О Доставке и Оплате'
        context['content'] = 'О Доставке и Оплате'
        context['text_on_page'] = 'Текст о Доставке, как она осуществляется и вариантах оплаты'
        return context

class ContactView(TemplateView):
    template_name = 'app/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'
        context['content'] = 'Контакты'
        return context