import graphene
from graphene_django import DjangoObjectType, DjangoListField

from .models import Dog, Breed


class DogType(DjangoObjectType):
    class Meta:
        model = Dog
        fields = "__all__"


class Query(graphene.ObjectType):
    all_dogs = graphene.List(DogType)
    dog = graphene.Field(DogType, dog_id=graphene.Int())

    def resolve_all_dogs(self, request):
        return Dog.objects.all()

    def resolve_dog(self, dog_id):
        return Dog.objects.get(pk=dog_id)


class DogInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    age = graphene.Int()
    breed = graphene.String()
    gender = graphene.String()
    color = graphene.String()
    favoritefood = graphene.String()
    favoritetoy = graphene.String()


class CreateDog(graphene.Mutation):
    class Arguments:
        dog_data = DogInput(required=True)

    dog = graphene.Field(DogType)

    @staticmethod
    def mutate(root, info, dog_data=None):
        dog_instance = Dog(
            name=dog_data.name,
            age=dog_data.age,
            gender=dog_data.gender,
            color=dog_data.color,
            favoritefood=dog_data.favoritefood,
            favoritetoy=dog_data.favoritetoy
        )
        dog_instance.save()
        return CreateDog(dog=dog_instance)


class UpdateDog(graphene.Mutation):
    class Arguments:
        dog_data = DogInput(required=True)

    dog = graphene.Field(DogType)

    @staticmethod
    def mutate(root, info, dog_data=None):
        dog_instance = Dog.objects.get(pk=dog_data.id)

        if dog_instance:
            dog_instance.name = dog_data.name,
            dog_instance.age = dog_data.age,
            dog_instance.gender = dog_data.gender,
            dog_instance.color = dog_data.color,
            dog_instance.favoritefood = dog_data.favoritefood,
            dog_instance.favoritetoy = dog_data.favoritetoy

            dog_instance.save()

            return UpdateDog(dog=dog_instance)
        return UpdateDog(dog=None)


class DeleteDog(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    dog = graphene.Field(DogType)

    @staticmethod
    def mutate(root, info, id):
        dog_instance = Dog.objects.get(pk=id)
        dog_instance.delete()
        return None


class Mutation(graphene.ObjectType):
    create_dog = CreateDog.Field()
    update_dog = UpdateDog.Field()
    delete_dog = DeleteDog.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
