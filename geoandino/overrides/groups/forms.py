from geonode.groups import forms as group_forms
from geonode.groups.models import GroupProfile
from slugify import slugify
from django import forms
from django.utils.translation import ugettext_lazy as _


def group_slugs():
    groups = GroupProfile.objects.all()
    return list(map(lambda g: g.slug, groups))


def group_choices():
    choices = [('default', _("It doesn't depend on another group"))]
    for slug in group_slugs():
        choices.append((slug, slug))
    return choices


def add_dependency_field(form):
    form.base_fields['depends_on_group'] = forms.ChoiceField(label=_('Does it depend on another group?'),
                                                             choices=group_choices(),
                                                             widget=forms.Select())


def clean_update_form(self):
    cleaned_data = self.cleaned_data

    name = cleaned_data.get("title")
    if name is None:
        raise forms.ValidationError(
            _("You should write a name for the group."))
    slug = slugify(name)

    cleaned_data["slug"] = slug

    return cleaned_data


add_dependency_field(group_forms.GroupForm)
add_dependency_field(group_forms.GroupUpdateForm)
group_forms.GroupForm.clean = clean_update_form
