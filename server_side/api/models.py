from django.db import models


class Store(models.Model):
    st_name = models.CharField(max_length=100)
    st_total_footfall = models.IntegerField()
    st_returning_footfall = models.IntegerField()
    st_time_spent = models.FloatField()
    st_tot_dep_visited = models.IntegerField()
    st_tot_departments = models.IntegerField()
    st_avg_dep_time = models.FloatField()
    st_bounce_rate = models.FloatField()

    def __str__(self):
        return self.st_name
