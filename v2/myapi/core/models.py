from django.db import models
# import pydantic
# Create your models here.

class planCostShares(models.Model):
    deductible = models.IntegerField()
    _org = models.TextField()
    copay = models.IntegerField()
    objectId = models.TextField()
    objectType = models.TextField()


class linkedService(models.Model):
    _org = models.TextField()
    objectId = models.TextField()
    objectType = models.TextField()
    name = models.TextField()


class planserviceCostShares(models.Model):
    deductible = models.IntegerField
    _org = models.TextField()
    copay = models.IntegerField()
    objectId = models.TextField()
    objectType = models.TextField()


class linkedPlanService(models.Model):
    _org = models.TextField()
    objectId = models.TextField()
    objectType = models.TextField()
    linkedService = models.OneToOneField(linkedService, on_delete=models.CASCADE)
    planserviceCostShares = models.OneToOneField(planserviceCostShares, on_delete=models.CASCADE)


class plan(models.Model):
    _org = models.TextField()
    objectId = models.TextField(unique=True)
    objectType = models.TextField()
    planType = models.TextField()
    creationDate = models.TextField()
    linkedPlanServices = models.ManyToManyField(linkedPlanService)
    planCostShares = models.OneToOneField(planCostShares, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.objectId}'

    class Meta:
        app_label = 'api'


# if __name__ == "__main__":
#     obj = plan(**validator.json_schema)
#     print(obj.objectId)


def load_dict(dict):
    obj = plan()
    obj.planCostShares = planCostShares(**dict["planCostShares"])
    obj._org = dict["_org"]
    obj.objectId = dict["objectId"]
    obj.objectType = dict["objectType"]
    obj.planType = dict["planType"]
    obj.creationDate = dict["creationDate"]
    return obj
