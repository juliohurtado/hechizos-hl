# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template.context import RequestContext
from django.http import JsonResponse

from django.views.generic import DetailView, ListView, View

from .models import Spell, Group


class SpellListView(ListView):
	model = Spell
	template_name = 'spells/spell_list.html'
	context_object_name = 'spells'

class SpellSearchView(View):
	model = Spell
	def get(self, request, *args, **kwargs):
		if self.request.is_ajax():
			spells = self.model.objects.filter(name__istartswith=request.GET['name']).values('id', 'name', 'slug')
			return JsonResponse(list(spells), safe=False)
		return JsonResponse("Solo se permiten consultas mediante AJAX", safe=False)

class SpellDetailView(DetailView):
    model = Spell
    template_name = 'spells/spell_detail.html'
    slug_field = 'name'
    context_object_name = 'spell'
