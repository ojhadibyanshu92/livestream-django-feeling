from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

CONDITIONS = (
    (0, 'Ecstatic'),
    (5, 'Passionate'),
    (10, 'Happy'),
    (15, 'Optimistic'),
    (20, 'Content'),
    (25, 'Board'),
    (26, 'Tired'),
    (27, 'Hungry'),
    (30, 'Pessimistic'),
    (35, 'Frustrated'),
    (40, 'Overwhelmed'),
    (45, 'Worried'),
    (50, 'Angry'),
    (55, 'Jealous'),
    (60, 'Insecure'),
    (65, 'Guilty'),
    (70, 'Fear'),
    (75, 'Grief'),
    (80, 'Despair'),
    (85, 'Paranoid'),
)


class Thought(models.Model):
    user = models.ForeignKey(User, related_name='thoughts', on_delete=models.CASCADE)
    recorded_at = models.DateTimeField(default=timezone.now, editable=False)
    condition = models.IntegerField(choices=CONDITIONS)
    notes = models.TextField(blank=True, default='')

    def __str__(self):
        return '{}:{}'.format(self.recorded_at.strftime('%Y-%m-%d %H:%M:%S'), self.get_condition_display())

    class Meta:
        ordering = ['-recorded_at']
