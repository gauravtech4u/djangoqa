from django.db import models 
from django.contrib.auth.models import User

class QuestionnaireManager(models.Manager):
    """ Manager for displaying all questionnaires with display flag 1 """
    def get_query_set(self):
        return super(QuestionnaireManager,self).get_query_set().filter(display_flag=True)
        
class OpenQuestionManager(models.Manager):
    """ Manager for displaying all questionnaires with display flag 1 """
    def get_query_set(self):
        return super(OpenQuestionManager,self).get_query_set().filter(type='open')
        
class MultipleChoiceManager(models.Manager):
    """ Manager for displaying all questionnaires with display flag 1 """
    def get_query_set(self):
        return super(MultipleChoiceManager,self).get_query_set().filter(type='multiple-choice')

class Post(models.Model):
    """ abstract class with basic fields """
    display_flag                =  models.BooleanField(default = True)
    created_date =  models.DateTimeField(auto_now = True)
    modified_date  =  models.DateTimeField(auto_now_add = True)
        
    class Meta:
        ordering  =  ('-created_date',)
        abstract=True
    
    objects=models.Manager()

class Questionnaire(Post):
    """ Questionnaire having multiple questions """
    name                     =  models.CharField(max_length = 300)
    slug                     =  models.SlugField(max_length = 255, unique = True)
    def __unicode__(self):
        return self.name
    
    objects=models.Manager()
    qa_manager=QuestionnaireManager()

class Question(Post):
    """ Questions of type open or multiple-choice """
    questionnaire = models.ForeignKey(Questionnaire)
    type = models.CharField(choices=(('open','OPEN'),('multiple-choice','MULTIPLE CHOICE'),),max_length=100,default='open')
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, blank=True, null=True)
    def __unicode__(self):
        return self.description[:20]
    
    class Meta:
        unique_together = ( 'questionnaire', 'description' )
        
    objects=models.Manager()
    open_questions=OpenQuestionManager()
    multiplechoice_questions=MultipleChoiceManager()

class QuestionChoice(Post):
    question = models.ForeignKey(Question)
    description = models.CharField( max_length=256,)
    priority = models.IntegerField()
    
    def __unicode__(self):
        return self.description[:40]
        
    class Meta:
        unique_together = ( 'question', 'description' )
    
class Answer(Post):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question,editable=False)
    description = models.TextField()

    def __unicode__(self):
        return self.description[:40]
    
    class Meta:
        order_with_respect_to='question'