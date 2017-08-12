from django.db import models

# LANGUAGES = (
#     'C',
#     'C++',
#     'JAVA',
#     'PYTHON',
#     'RUBY',
#     'GO',
#     'SCALA',
#     'JAVASCRIPT'
#     'PERL'
#     )

class users(models.Model):
    user_name = models.CharField(max_length=60)
    email_id = models.EmailField
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    password_salt = models.CharField(max_length=80)
    active = models.BooleanField()

# Create your models here.
class questions(models.Model):
    url = models.URLField()
    content = models.TextField()
    difficulty = models.CharField(max_length=5)
    author_id = models.ForeignKey(users)

class tags(models.Model):
    tag_name = models.CharField(max_length=80)

class question_tags(models.Model):
    question_id = models.ForeignKey(questions, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(tags, on_delete=models.CASCADE)

class submissions(models.Model):
    question_id = models.ForeignKey(questions, on_delete=models.CASCADE)
    user_id = models.ForeignKey(users, on_delete=models.CASCADE)
    code = models.TextField()
    # language =  models.CharField(choices=LANGUAGES, default='PYTHON')