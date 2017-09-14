from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from geonode.groups.forms import GroupInviteForm, GroupMemberForm
from geonode.groups.models import GroupProfile

from django.utils.translation import ugettext as _


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