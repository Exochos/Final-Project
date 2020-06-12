from django.db import models
from django.contrib.auth.models import User

#Making a meetup model with the relevent fields.
class MeetUp(models.Model):
	meetup_name = models.CharField(max_length=255)
	meetup_date = models.DateField()
	meetup_time = models.TimeField()
	meetup_location = models.CharField(max_length=255)
	meetup_desc = models.CharField(max_length=255)
	user_id = models.ForeignKey(User, on_delete = models.DO_NOTHING)

	# meeting_id = models.IntegerField(primary_key=True)
	def __str__(self):
		return self.meetup_name
	class Meta:
		db_table='meetup'
		verbose_name_plural='meetups'

#Activity model
class Activity(models.Model):
    activity_name = models.CharField(max_length=255)
    activity_type = models.CharField(max_length=255)
    activity_desc = models.TextField()

    def __str__(self):
        return self.activity_name
    
    class Meta:
        db_table='activity'
        verbose_name_plural='activities'