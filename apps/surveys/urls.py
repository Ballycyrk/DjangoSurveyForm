from django.conf.urls import include, url, patterns
from apps.surveys import views

urlpatterns = patterns ('',
  url(r'^$', views.index, name='survey'),
  url(r'submit$', views.process_form, name='submit'),
  )
