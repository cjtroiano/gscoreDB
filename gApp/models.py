from django.db import models

class Score(models.Model):
	Course = models.CharField(max_length=100)
	Score = models.IntegerField()
	Date = models.DateField(auto_now_add=True)

	def __str__(self):
		output = self.Course + " " + str(self.Score) + " " + str(self.Date)
		return output