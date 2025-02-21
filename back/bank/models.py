from django.db import models
from django.conf import settings


class Bank(models.Model):
  fin_co_no = models.CharField(max_length=20, unique=True)
  kor_co_nm = models.CharField(max_length=30)


class DepositProduct(models.Model):
  bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
  like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_products")
  fin_prdt_cd = models.TextField(unique=True)                   # 금융 상품 코드
  # kor_co_nm = models.TextField(default='none')                  # 금융 회사 명
  fin_prdt_nm = models.TextField(default='none')                # 금융 상품 명
  etc_note = models.TextField(default='none')                   # 금융 상품 설명
  join_deny = models.IntegerField(default=-1)                   # 가입 제한
  join_member = models.TextField(default='none')                # 가입 대상
  join_way = models.TextField(null=True, default='none')                   # 가입 방법
  spcl_cnd = models.TextField(default='none')                   # 우대 조건\
  deposit_type = models.IntegerField(default=-1)                 # 예/적금 구분 , 예금 = 1 적금 = 2

class DepositOption(models.Model):
  product = models.ForeignKey(DepositProduct, on_delete=models.CASCADE)
  fin_prdt_cd = models.TextField(default='none')
  intr_rate_type_nm = models.CharField(max_length=100)
  intr_rate = models.FloatField(null=True, default=-1)
  intr_rate2 = models.FloatField(null=True, default=-1)
  save_trm = models.IntegerField(default=-1)


  
