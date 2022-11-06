from django.urls import reverse_lazy
from django.views.generic import (TemplateView, FormView,
                                  CreateView, ListView,
                                  DetailView, UpdateView,
                                  DeleteView)
from classroom.forms import ContactForm
from classroom.models import Teacher


class HomeView(TemplateView):
    template_name = 'classroom/home.html'


class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'


class TeacherCreateView(CreateView):
    model = Teacher
    # mapping = model_form.html
    fields = "__all__"
    success_url = reverse_lazy('classroom:thank_you_view')


class TeacherListView(ListView):
    model = Teacher
    queryset = Teacher.objects.order_by('first_name')

    context_object_name = 'teacher_list'


class TeacherDetailView(DetailView):
    model = Teacher
    # mapping = model_detail.html


class TeacherUpdateView(UpdateView):
    model = Teacher
    # mapping = model_form.html
    fields = '__all__'
    success_url = reverse_lazy('classroom:list_teacher')


class TeacherDeleteView(DeleteView):
    # Form ---> Confirm Delete Button
    # default template name: model_confirm_delete.html
    model = Teacher
    success_url = reverse_lazy('classroom:list_teacher')


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'
    success_url = '/classroom/thanks'

    def form_valid(self, form):
        print(form.cleaned_data)

        return super().form_valid(form)
