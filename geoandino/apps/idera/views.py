# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic import View
from geonode.base.models import ResourceBase


class IderaMetadata(View):

    template_name = 'layers/metadata_as_text.html'

    def get(self, request, resource_id):

        def check_if_not_none(param):
            if param is not None:
                return param
            return ''

        resource = check_if_not_none(ResourceBase.objects.get(id=resource_id))
        title = check_if_not_none(resource.title)
        reference_date = str(check_if_not_none(resource.csw_insert_date))
        reference_date_type = check_if_not_none(resource.date_type)
        edition = check_if_not_none(resource.edition)
        summary = check_if_not_none(resource.abstract)
        state = str(check_if_not_none(resource.is_published))
        creator_contact_point = check_if_not_none(resource.owner.email)
        maintenance_frequency = check_if_not_none(resource.maintenance_frequency)
        topic = check_if_not_none(resource.category)
        dirty_keywords = check_if_not_none(resource.keyword_list)
        keywords = ''
        for k in dirty_keywords():
            keywords += k + ", "
        keywords = keywords[:len(keywords)-2]
        constraints = str(check_if_not_none(resource.restriction_code_type))
        if not constraints == '':
            constraints += ', '
        constraints += check_if_not_none(resource.constraints_other)
        type = check_if_not_none(resource.csw_type)
        # from geonode.maps.models import MapLayer                          |
        # maplayer = MapLayer.objects.filter(name=resource.title).all()     | escala
        # scale = maplayer.map.zoom                                         |
        data_language = check_if_not_none(resource.language)
        temporal_extent = ''
        if resource.temporal_extent_start is not None and resource.temporal_extent_end is not None:
            temporal_extent = str(resource.temporal_extent_start) + ' - ' + str(resource.temporal_extent_end)
        geographic_extent = ''
        if resource.bbox_x0 is not None and \
                resource.bbox_x1 is not None and resource.bbox_y0 is not None and resource.bbox_y1 is not None:
                geographic_extent = 'Latitud Norte: ' + str(resource.bbox_x0) + ', ' + '' \
                                       'Latitud Sur: ' + str(resource.bbox_x1) + ', ' + '' \
                                       'Latitud Oeste: ' + str(resource.bbox_y0) + ', ' + '' \
                                       'Latitud Este: ' + str(resource.bbox_y1)
        projection = check_if_not_none(resource.srid)
        link = check_if_not_none(resource.detail_url)
        lineage = check_if_not_none(resource.data_quality_statement)
        response = render(request, self.template_name, {'title': title,
                                                        'reference_date': reference_date,
                                                        'reference_date_type': reference_date_type,
                                                        'edition': edition,
                                                        'summary': summary,
                                                        'state': state,
                                                        'creator_contact_point': creator_contact_point,
                                                        'metadata_contact_point': creator_contact_point,
                                                        'maintenance_frequency': maintenance_frequency,
                                                        'topic': topic,
                                                        'keywords': keywords,
                                                        'constraints': constraints,
                                                        'type': type,
                                                        'data_language': data_language,
                                                        'data_character_set': 'UTF-8',
                                                        'temporal_extent': temporal_extent,
                                                        'geographic_extent': geographic_extent,
                                                        'description': summary,
                                                        'projection': projection,
                                                        'link': link,
                                                        'protocol': 'WWW:LINK-1.0-http--link',
                                                        'link_name': title,
                                                        'link_description': summary,
                                                        'lineage': lineage,
                                                        'id': resource_id,
                                                        'metadata_identifier': resource_id,
                                                        'version': edition,
                                                        'metadata_language': data_language,
                                                        'metadata_character_set': 'UTF-8',
                                                        'metadata_creation_date': reference_date})
        response['Content-Disposition'] = 'attachment; filename=metadata.xml'
        return response
