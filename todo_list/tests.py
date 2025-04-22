from django.test import TestCase, Client
from django.urls import reverse
from .models import Todo
class HomrViewTest(TestCase):

    def setup(self):
        #create a todo
        Todo.objects.create(title="Todo", description='Test 1').save()
        Todo.objects.create(title="Todo 1", description='Test 2').save()
        self.client = Client()

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
    
    def test_home_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response,'index.html')

    def test_home_view_context_data(self):
        
        response = self.client.get(reverse('home'))
        print('Todo:', Todo.objects.all())
        self.assertIn('list',response.context)
        self.assertEqual(len(response.context['list']),0)