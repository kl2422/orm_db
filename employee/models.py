from django.db import models

# Create your models here.


"""部门"""
class Dept(models.Model):
    deptNo = models.AutoField(primary_key=True)
    dname = models.CharField(max_length=50, null=True)
    loc = models.CharField(max_length=50, null=True)
    class Meta:
        db_table = "dept"


"""员工信息"""
class Emp(models.Model):
    empNo = models.AutoField(unique=True, db_index=True, primary_key=True)
    ename = models.CharField(max_length=20, blank=True, default='', db_index=True)
    job = models.CharField(max_length=50, null=True)
    mgr = models.ForeignKey('self', on_delete=models.CASCADE, db_column='mgr', null=True, db_constraint=False)
    hireDate = models.DateField(null=True)
    sal = models.DecimalField(null=True, max_digits=8, decimal_places=2)
    comm = models.DecimalField(null=True, max_digits=8, decimal_places=2)
    gender_choices = (
        (0, "女"),
        (1, "男"),
    )
    gender = models.IntegerField(choices=gender_choices)
    # 与dept一对多，通过deptno关联
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE, db_column="deptno", null=True, db_constraint=False)
    # 是否删除
    is_valid_choices = (
        (0, "无效"),
        (1, "有效"),
    )
    isValid = models.IntegerField(db_column="is_valid", choices=is_valid_choices, default=1)

    class Meta:
        db_table = 'emp'


"""薪水等级"""
class SaleGrade(models.Model):
    grade = models.AutoField(primary_key=True)
    losal = models.IntegerField()
    hisal = models.IntegerField()
    class Meta:
        db_table = 'salegrade'

