from django.db import models
from django.utils import timezone

class Memo(models.Model):
    memo_text = models.CharField(max_length=200)
    insert_date = models.DateTimeField('date inserted', default=timezone.datetime.now())
    def __str__(self):
        return f"{self.id}_{self.memo_text}"
    class Meta:
        db_table='tbl_memo_memo'

class Tips(models.Model):
    memo = models.ForeignKey(Memo, on_delete=models.CASCADE)
    tips_text = models.CharField(max_length=200)
    insert_date = models.DateTimeField('date inserted', default=timezone.datetime.now())
    class Meta:
        db_table='tbl_memo_tips'

