from django.db import models


class Store(models.Model):
    st_name = models.CharField(max_length=80)
    st_totall_football = models.IntegerField()
    st_returns = models.IntegerField()
    st_time_spent = models.FloatField()
    st_tot_dep_visited = models.IntegerField()
    st_tot_departments = models.IntegerField()
    st_avg_dep_time = models.IntegerField()
    st_bounce_rate = models.FloatField()
