from django import forms
from .models import Teachercreate,Comment,CommentAnswer,Studentsolution,Gradeassignment
from .models import Question,Answer
from django.contrib import messages



class ClassroomForm(forms.ModelForm):
    class Meta:
        model=Teachercreate
        fields=('subject','code')



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment',)

class CommentAnswerForm(forms.ModelForm):

    class Meta:
        model = CommentAnswer
        fields = ('comment',)


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('text', )


class BaseAnswerInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()

        has_one_correct_answer = False
        for form in self.forms:
            if not form.cleaned_data.get('DELETE', False):
                if form.cleaned_data.get('is_correct', False):
                    has_one_correct_answer = True
                    break
        if not has_one_correct_answer:
            
            raise ValidationError('Mark at least one answer as correct.', code='no_correct_answer')

class AssignmentForm(forms.ModelForm):
    class Meta:
        model=Studentsolution
        fields=('pdf',)



class GradeForm(forms.ModelForm):
    class Meta:
        model= Gradeassignment
        fields=('grade','total')