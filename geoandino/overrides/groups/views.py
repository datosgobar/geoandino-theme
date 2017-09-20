from django.core.urlresolvers import reverse
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from geonode.groups.forms import GroupInviteForm, GroupForm, GroupUpdateForm, GroupMemberForm
from geonode.groups.models import GroupProfile, GroupInvitation, GroupMember

from geoandino.models import GroupTreeNode


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

    return render_to_response("groups/group_update.html", {
        "form": form,
        "group": group,
        }, context_instance=RequestContext(request))
