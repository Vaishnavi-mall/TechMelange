from operator import truediv
from ckeditor_uploader.fields import RichTextUploadingField
from statistics import mode
import uuid
from django.db import models
from enum import Enum

class ChoiceEnum(Enum):
    @classmethod
    def get_value(cls, member):
        return cls[member].value[0]

    @classmethod
    def get_choices(cls):
        return tuple(x.value for x in cls)


class PositionType(ChoiceEnum):
    president = ('P', 'President')
    vicePresident = ('R', 'Vice President')
    secretary = ('S', 'Secretary')
    treasurer = ('T', 'Treasurer')
    joint_secretary = ('JS', 'Joint Secretary')
    joint_treasurer = ('JT', 'Joint Treasurer')
    coordinator = ('C', 'Coordinator')
    member = ('M', 'Member')



class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class TechFest(BaseModel):
    name = models.CharField(max_length=100,null=True,blank=True)
    short_description = models.CharField(max_length=600,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    society_logo = models.ImageField(null=True,blank=True)
    college_logo= models.ImageField(null=True,blank=True)
    university_logo=models.ImageField(null=True,blank=True)
    fest_image=models.ImageField(null=True,blank=True)
    fest_video = models.FileField(null=True,blank=True)
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    email = models.CharField(max_length=50,null=True,blank=True)
    instagram = models.CharField(max_length=50,null=True,blank=True)
    linkedin = models.CharField(max_length=50,null=True,blank=True)
    facebook = models.CharField(max_length=50,null=True,blank=True)
    twitter = models.CharField(max_length=50,null=True,blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Tech Fest'
        verbose_name = 'Tech Fest'

    def __str__(self):
        return self.name

class Events(BaseModel):
    name = models.CharField(max_length=100,null=True,blank=True)
    short_description = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    rules = models.TextField(null=True,blank=True)
    event_start_date = models.DateField(null=True,blank=True)
    event_end_date = models.DateField(null=True,blank=True)
    stages = models.IntegerField(null=True,blank=True)
    event_start_time = models.TimeField(null=True,blank=True)
    event_end_time = models.TimeField(null=True,blank=True)
    event_image = models.ImageField(upload_to="event/images", null=True,blank=True)
    event_video = models.FileField(upload_to="event/videos", null=True,blank=True)
    link =  models.TextField(null=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Events'
        verbose_name = 'Event'

    def __str__(self):
        return self.name



class Images(BaseModel):
    """ US : 11 """
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='event_images')
    name = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to="event/images", null=True,blank=True)

    class Meta:
        ordering = ('-created_at',)

class Videos(BaseModel):
    """ US : 11 """
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='event_videos')
    name = models.CharField(max_length=100,null=True,blank=True)
    video = models.FileField(upload_to="event/videos", null=True,blank=True)

    class Meta:
        ordering = ('-created_at',)

class StudentCoordinators(BaseModel):
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='event_student_coordinators')
    name = models.CharField(max_length=100,null=True,blank=True)
    image =  models.ImageField(upload_to="event/student_coordinators_images", null=True,blank=True)
    is_design_team= models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Student Coordinators'
        verbose_name = 'Student Coordinator'

    def __str__(self):
        return self.name


class TeacherCoordinators(BaseModel):
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='event_teacher_coordinators')
    name = models.CharField(max_length=100,null=True,blank=True)
    image= models.ImageField(upload_to="event/teacher_coordinator_images", null=True,blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Teacher Coordinators'
        verbose_name = 'Teacher Coordinator'

    def __str__(self):
        return self.name


class Speakers(BaseModel):
    name = models.CharField(max_length=100,null=True,blank=True)
    image =  models.ImageField(upload_to="event/speakers_images", null=True,blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Speakers'
        verbose_name = 'Speaker'

    def __str__(self):
        return self.name


class Sponsors(BaseModel):
    name = models.CharField(max_length=100,null=True,blank=True)
    image= models.ImageField(upload_to="event/sponsors_images", null=True,blank=True)
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Sponsors'
        verbose_name = 'Sponsor'

    def __str__(self):
        return self.name


class StudentCouncilMembers(BaseModel):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50,choices=PositionType.get_choices(),null=True,blank=True)
    image= models.ImageField(upload_to="event/student_council_images", null=True,blank=True)
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Student Council Members'
        verbose_name = 'Student Council'

    def __str__(self):
        return self.name


class EventsTimeLine(BaseModel):
    name = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True,blank=True)
    class Meta:
        verbose_name_plural = 'Event TimeLine'
        verbose_name = 'Event TimeLine'
