from django import forms
from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from authentication.models import ApplicationUser


class ApplicationUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = ApplicationUser
        fields = ('email', 'first_name', 'last_name', 'organization', 'is_active')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(ApplicationUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class ApplicationUserChangeForm(forms.ModelForm):

    class Meta:
        model = ApplicationUser
        fields = ('email', 'first_name', 'last_name', 'organization', 'is_active')


class ApplicationUserAdmin(UserAdmin):
    form = ApplicationUserChangeForm
    add_form = ApplicationUserCreationForm

    list_display = ('email', 'first_name', 'last_name', 'organization', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('organization',)})
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
    list_filter = ()


admin.site.register(ApplicationUser, ApplicationUserAdmin)
admin.site.unregister(Group)
