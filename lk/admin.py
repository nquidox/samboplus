import datetime

from django.contrib import admin
from django.core.exceptions import ValidationError

from .forms import CustomUserCreateForm
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.db.models.functions import ExtractYear
from django.db.models import Q

from lk.sizes import jacket_size, shorts_size, shoes_size

##### Filters section #####


class WeightFilter(admin.SimpleListFilter):
    title = 'Текущий вес'
    parameter_name = 'weight'

    def lookups(self, request, model_admin):
        return(
            ('0-30', 'от 0 до 30 кг'),
            ('30-40', 'от 30 до 40 кг'),
            ('40-50', 'от 40 до 50 кг'),
            ('50-60', 'от 50 до 60 кг'),
            ('60-70', 'от 60 до 70 кг'),
            ('70-80', 'от 70 до 80 кг'),
            ('80-90', 'от 80 до 90 кг'),
            ('90-100', 'от 90 до 100 кг'),
            ('100+', 'свыше 100 кг'),
        )

    def queryset(self, request, queryset):
        if not self.value():
            return queryset

        if self.value() == '0-30':
            return queryset.filter(current_weight__gte=0, current_weight__lt=30)

        if self.value() == '30-40':
            return queryset.filter(current_weight__gte=30, current_weight__lt=40)

        if self.value() == '40-50':
            return queryset.filter(current_weight__gte=40, current_weight__lt=50)

        if self.value() == '50-60':
            return queryset.filter(current_weight__gte=50, current_weight__lt=60)

        if self.value() == '60-70':
            return queryset.filter(current_weight__gte=60, current_weight__lt=70)

        if self.value() == '70-80':
            return queryset.filter(current_weight__gte=70, current_weight__lt=80)

        if self.value() == '80-90':
            return queryset.filter(current_weight__gte=80, current_weight__lt=90)

        if self.value() == '90-100':
            return queryset.filter(current_weight__gte=90, current_weight__lt=100)

        if self.value() == '100+':
            return queryset.filter(current_weight__gte=100)


class YearFilter(admin.SimpleListFilter):
    title = 'Год рождения'
    parameter_name = 'year'

    def lookups(self, request, model_admin):
        year_list = CustomUser.objects.annotate(y=ExtractYear('birth_date'))\
            .order_by('-y')\
            .values_list('y', flat=True)\
            .distinct()
        return [(str(y), (str(y))) for y in year_list]

    def queryset(self, request, queryset):
        if self.value() is not None:
            return queryset.filter(birth_date__year=self.value())
        return queryset


class DocumentsFilter(admin.SimpleListFilter):
    title = 'Документы'
    parameter_name = 'documents'

    def lookups(self, request, model_admin):
        return (
            ('missing', 'Отсутствуют'),
            ('expired', 'Просрочены'),
            ('debt', 'Задолженность')
        )

    def queryset(self, request, queryset):
        if not self.value():
            return queryset

        if self.value() == 'missing':
            return queryset.filter(
                Q(agreement__icontains='') |
                Q(passport__icontains='') |
                Q(insurance__icontains='') |
                Q(medical_report__icontains='') |
                Q(school_certificate__icontains='')
            )

        if self.value() == 'expired':
            today = datetime.datetime.today()
            return queryset.filter(
                Q(agreement_expiration_date__lt=today) |
                Q(insurance_expiration_date__lt=today) |
                Q(medical_report_expiration_date__lt=today) |
                Q(school_certificate_expiration_date__lt=today)
            )

        if self.value() == 'debt':
            return queryset.filter(debt=True)


class SizesFilter(admin.SimpleListFilter):
    title = 'Размеры одежды'
    parameter_name = 'sizes'

    def lookups(self, request, model_admin):
        return(
            ('calculated_sizes', 'Расчетные размеры'),
        )

    def queryset(self, request, queryset):
        if not self.value():
            return queryset

        if self.value() == 'calculated_sizes':
            return queryset


##### Filters section end #####


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreateForm
    list_display = ('username',)
    readonly_fields = ('jacket', 'shorts', 'shoes')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Персональная информация', {'fields': ('first_name', 'patronymic', 'last_name', 'photo')}),
        ('Информация о спортсмене', {'fields': ('gender', 'birth_date', 'place_of_birth', 'home_address',
                                                'current_weight', 'current_height',
                                                'chest', 'waist', 'hips', 'foot',
                                                'jacket', 'shorts', 'shoes')}),
        ('Информация о родителях/опекунах', {'fields': ('fullname1', 'phone_number1', 'fullname2', 'phone_number2')}),
        ('Документы', {'fields': ('passport',
                                  'application_blank',
                                  'agreement', 'agreement_expiration_date',
                                  'medical_report', 'medical_report_expiration_date',
                                  'insurance', 'insurance_expiration_date',
                                  'school_certificate', 'school_certificate_expiration_date',
                                  'debt')}),
        ('Права доступа', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Даты', {'fields': ('last_login', 'date_joined')}),
    )

    ##### Filters section #####

    list_filter = ('gender', YearFilter, DocumentsFilter, WeightFilter, SizesFilter)

    def get_list_display(self, request):
        if request.GET.get('documents', False) == 'missing':
            return self.list_display + ('first_name', 'last_name',
                                        'application_blank', 'agreement', 'passport', 'insurance',
                                        'medical_report', 'school_certificate')

        elif request.GET.get('documents', False) == 'expired':
            return self.list_display + ('first_name', 'last_name', 'agreement_expiration_date',
                                        'insurance_expiration_date',
                                        'medical_report_expiration_date',
                                        'school_certificate_expiration_date')

        elif request.GET.get('documents', False) == 'debt':
            return self.list_display + ('first_name', 'last_name', 'debt')

        elif request.GET.get('sizes', False) == 'calculated_sizes':
            return self.list_display + ('chest', 'waist', 'hips', 'foot', 'jacket', 'shorts', 'shoes')

        else:
            # стандартный набор столбцов в таблице спортсменов
            return self.list_display + ('first_name', 'last_name', 'gender', 'current_weight', 'birth_date')

    # расчетные поля

    def jacket(self, obj):
        return jacket_size(obj.current_height, obj.chest, obj.waist)
    jacket.short_description = 'Размер куртки'

    def shorts(self, obj):
        return shorts_size(obj.hips)
    shorts.short_description = 'Размер шорт'

    def shoes(self, obj):
        return shoes_size(obj.foot)
    shoes.short_description = 'Размер обуви'

    ##### Filters section end #####


admin.site.register(CustomUser, CustomUserAdmin)
