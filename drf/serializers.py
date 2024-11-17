from rest_framework import serializers, validators

from drf.models import ApiUser, Warehouse, Product, Order


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField(validators=[
        validators.UniqueValidator(ApiUser.objects.all())
    ])
    password = serializers.CharField(min_length=6, max_length=20, write_only=True)
    type = serializers.ChoiceField(choices=['Поставщик', 'Покупатель'])

    def update(self, instance, validate_data):
        if email := validate_data.get('email'):
            instance.email = email
            instance.save(update_fields=['email'])

        if password := validate_data.get('password'):
            instance.set_password(password)
            instance.save(update_fields=['password'])

    def create(self, validated_data):

        user = ApiUser.objects.create(
            email=validated_data['email'],
            username=validated_data['email'],
            type=validated_data['type']
        )

        user.set_password(validated_data['password'])
        user.save(update_fields=['password'])

        return user


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(validators=[
        validators.UniqueValidator(Product.objects.all())
    ])
    count = serializers.IntegerField()
    warehouse = serializers.PrimaryKeyRelatedField(queryset=Warehouse.objects.all())

    def create(self, validated_data):
        # warehouse = validated_data['warehouse']
        product = Product.objects.create(
            name=validated_data['name'],
            count=validated_data['count'],
            warehouse=validated_data['warehouse']
        )

        return product

    def update(self, instance, validated_data):
        if count := validated_data['count']:
            instance.count += count
            instance.save(update_fields=['count'])
        return instance


class OrderSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.exclude(count=0))
    count = serializers.IntegerField()

    def create(self, validated_data):
        count = validated_data['count']
        product = Product.objects.select_for_update().get(id=validated_data['product'].id)
        if product.count < count:
            raise serializers.ValidationError(
                f'Недостаточно товара на складе! Запрашивается {count}, в наличии {product.count}')

        product.count -= count
        product.save(update_fields=['count'])

        order = Order.objects.create(
            product=product,
            count=count,
            user=self.context['request'].user
        )
        return order
