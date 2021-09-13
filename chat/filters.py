

import django_filters

from bases.filters import BaseFilters

from .models import Conversation, ChatMessage, Participant


class MessageFilters(BaseFilters):
    """
        Chat message Filters will define here
    """
    conversation = django_filters.CharFilter(
        field_name='conversation__id',
        lookup_expr='icontains'
    )
    message = django_filters.CharFilter(
        field_name='message',
        lookup_expr='icontains'
    )
    sender = django_filters.CharFilter(
        field_name='sender__email',
        lookup_expr='icontains'
    )
    created_on = django_filters.CharFilter(
        field_name='created_on__date', lookup_expr='exact'
    )
    start = django_filters.CharFilter(
        field_name='created_on__date', lookup_expr='gte'
    )
    end = django_filters.CharFilter(
        field_name='created_on__date', lookup_expr='lte'
    )

    class Meta:
        model = ChatMessage
        fields = [
            'id',
            'conversation',
            'message',
            'sender',
            'is_read',
            'created_on'
        ]


class ConversationFilters(BaseFilters):
    """
        Conversation filters will be defined here
    """
    client = django_filters.CharFilter(
        field_name='client__email',
        lookup_expr='icontains'
    )
    participant = django_filters.CharFilter(
        field_name='participants__user_id',
        lookup_expr='exact'
    )
    created_on = django_filters.CharFilter(
        field_name='created_on__date', lookup_expr='exact'
    )
    updated_on = django_filters.CharFilter(
        field_name='updated_on__date', lookup_expr='exact'
    )
    start = django_filters.CharFilter(
        field_name='created_on__date', lookup_expr='gte'
    )
    end = django_filters.CharFilter(
        field_name='created_on__date', lookup_expr='lte'
    )

    class Meta:
        model = Conversation
        fields = [
            'id',
            'client',
            'created_on',
            'updated_on',
            'is_blocked'
        ]


class ParticipantFilters(BaseFilters):
    """
        Conversation filters will be defined here
    """
    client = django_filters.CharFilter(
        field_name='client__email',
        lookup_expr='icontains'
    )
    name = django_filters.CharFilter(
        field_name='name', lookup_expr='icontains'
    )
    user_id = django_filters.CharFilter(
        field_name='user_id', lookup_expr='exact'
    )
    last_seen = django_filters.CharFilter(
        field_name='last_seen__date', lookup_expr='exact'
    )

    class Meta:
        model = Participant
        fields = [
            'id',
            'client',
            'name',
            'user_id',
            'last_seen',
            'is_online'
        ]