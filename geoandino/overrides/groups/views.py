from django.core.urlresolvers import reverse
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from geonode.groups.forms import GroupInviteForm, GroupForm, GroupUpdateForm, GroupMemberForm

from geoandino.models import GroupTreeNode

from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from geonode.groups.forms import GroupInviteForm, GroupMemberForm
from geonode.groups.models import GroupProfile

from django.utils.translation import ugettext as _



@login_required
def group_create(request):
    if request.method == "POST":
        form = GroupForm(request.POST, request.FILES)
        if form.is_valid():
            group = form.save(commit=False)
            group.save()
            form.save_m2m()
            group.join(request.user, role="manager")
            node_dependency = form.cleaned_data['depends_on_group']
            add_node_dependency(group, node_dependency)
            return HttpResponseRedirect(
                reverse(
                    "group_detail",
                    args=[
                        group.slug]))
    else:
        form = GroupForm()

    return render_to_response("groups/group_create.html", {
        "form": form,
    }, context_instance=RequestContext(request))


def add_node_dependency(group, node_dependency):
    if node_dependency != 'default':
        parent_node = GroupTreeNode.objects.get(group__title=node_dependency)
        child_node = GroupTreeNode.objects.get(group=group)
        parent_node.children.add(child_node)
        child_node.parent = parent_node
        child_node.save()


def remove_own_title(form, group):
    choices = form.fields['depends_on_group'].choices
    for choice in choices:
        if choice[1] == group.title:
            choices.remove(choice)
    form.fields['depends_on_group'].choices = choices


@login_required
def group_update(request, slug):
    group = GroupProfile.objects.get(slug=slug)
    if not group.user_is_role(request.user, role="manager"):
        return HttpResponseForbidden()

    if request.method == "POST":
        form = GroupUpdateForm(request.POST, request.FILES, instance=group)
        if form.is_valid():
            group = form.save(commit=False)
            group.save()
            form.save_m2m()
            return HttpResponseRedirect(
                reverse(
                    "group_detail",
                    args=[
                        group.slug]))
    else:
        form = GroupForm(instance=group)
        remove_own_title(form, group)

    return render_to_response("groups/group_update.html", {
        "form": form,
        "group": group,
        }, context_instance=RequestContext(request))


def internationalize_fields():
    GroupMemberForm.base_fields['role'].label = _('Role')
    GroupMemberForm.base_fields['role'].choices = [
        ("member", _("Member")),
        ("manager", _("Manager")),
]
    GroupMemberForm.base_fields['user_identifiers'].label = _('User identifiers')


def group_members(request, slug):
    group = get_object_or_404(GroupProfile, slug=slug)
    ctx = {}

    if not group.can_view(request.user):
        raise Http404()

    if group.access in [
            "public-invite",
            "private"] and group.user_is_role(
            request.user,
            "manager"):
        ctx["invite_form"] = GroupInviteForm()

    if group.user_is_role(request.user, "manager"):
        internationalize_fields()
        ctx["member_form"] = GroupMemberForm()

    ctx.update({
        "group": group,
        "members": group.member_queryset(),
        "is_member": group.user_is_member(request.user),
        "is_manager": group.user_is_role(request.user, "manager"),
    })
    ctx = RequestContext(request, ctx)
    return render_to_response("groups/site_group_members.html", ctx)
