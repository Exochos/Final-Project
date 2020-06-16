#django imports
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

#imports from our app
from .models import MeetUp, Activity
from .views import *
from .forms import *


# TESTS FOR MODELS #
class MeetUpTest(TestCase):
    def test_string(self):
        meetupname = MeetUp(meetup_name='Django Basics')
        self.assertEqual(str(meetupname), meetupname.meetup_name)
    
    def test_table(self):
        self.assertEqual(str(MeetUp._meta.db_table), 'meetup')    

class ActivityTest(TestCase):
    def test_string(self):
        activity = Activity(activity_name='Hackathon')
        self.assertEqual(str(activity), activity.activity_name)
    
    def test_table(self):
        self.assertEqual(str(Activity._meta.db_table), 'activity') 

# TESTS FOR VIEWS #
class IndexTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('index'))
       self.assertEqual(response.status_code, 200)

class MeetUpViewTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('meetup'))
       self.assertEqual(response.status_code, 200)

class ActivityViewTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('activity'))
       self.assertEqual(response.status_code, 200)

class MeetUpDetailsViewTest(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.meetup = MeetUp.objects.create(meetup_name='Learn Django',  meetup_date='2020-07-01', meetup_time='13:00', meetup_location='Online', meetup_desc='Learn the basics of Django', user_id=self.test_user)

    def test_meetupdetails_success(self):
        response=self.client.get(reverse('meetupdetails', args=(self.meetup.id,)))
        self.assertEqual(response.status_code, 200)

# TESTS FOR FORMS #
class MeetUpFormTest(TestCase):
    def test_typeform_is_valid(self):
        testuser=User.objects.create(pk=1).pk
        form=MeetUpForm(data={'meetup_name': "Learn Django", 'meetup_date': "2020-07-01", 'meetup_time': "13:00", 'meetup_location': "online", 'meetup_desc': "django basics", 'user_id':"testuser"})
        self.assertTrue(form.is_valid())
    
    def test_typeform_empty(self):
        form=MeetUpForm(data={'meetup_name': "", 'meetup_date': "", 'meetup_time': "", 'meetup_location': "", 'meetup_desc': "", 'user_id':""})
        self.assertFalse(form.is_valid())

class ActivityFormTest(TestCase):
    def test_typeform_is_valid(self):
        form=ActivityForm(data={'activity_name': "Django Projects", 'activity_type': "workshop", 'activity_desc ': "collaborative Django projects"})
        self.assertTrue(form.is_valid())
    
    def test_typeform_empty(self):
        form=ActivityForm(data={'activity_name': "", 'activity_type': "", 'activity_desc': ""})
        self.assertFalse(form.is_valid())

# TESTS FOR AUTHENTICATION #
class New_MeetUp_authentication_test(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.meetup = MeetUp.objects.create(meetup_name='Learn Django',  meetup_date='2020-07-01', meetup_time='13:00', meetup_location='Online', meetup_desc='Learn the basics of Django', user_id=self.test_user)

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newmeetup'))
        self.assertRedirects(response, '/accounts/login/?next=/meetup/newmeetup/')

    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username='testuser1', password='P@ssw0rd1')
        response=self.client.get(reverse('newmeetup'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'meetup/newmeetup.html')