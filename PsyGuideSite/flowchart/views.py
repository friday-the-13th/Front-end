from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Chart
from .forms import ChartForm

from .xml_reader import Node, load_xml
from .models import ChartNode

def view_all_charts(request):
	return render(request, 'flowchart/view_all_charts.html', {'flowcharts': Chart.objects.all()})

def view_chart(request):
	pk = request.GET.get('pk')
	if pk:
		flowchart = Chart.objects.get(pk=pk)
		return render(request, 'flowchart/view_chart.html', { 'flowchart': flowchart })
	else:
		return render(request, 'flowchart/view_chart.html')

def parse_xml_string(request):
    pk = request.POST
    nodes = load_xml(pk['xml'])

    for id, node in nodes.items():
        parents = node.get_parents()
        children = node.get_children()
        if len(parents) == 0 and len(children) == 0:
            continue
        if len(parents) > 0:
            for id, node in parents:
                child = Child.object.create(node)

        chart_node = ChartNode.objects.create(nodeId=id,
                content=node.get_content(),
                # parent=parents,
                # child=children,
                plan=pk)

    return render(request, 'flowchart/view_chart.html')

def add_chart(request):
	form = ChartForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect(reverse('flowchart:view_all_charts'))
	context = {
		'form': form
	}
	return render (request, 'flowchart/add_chart.html', context)

def edit_chart(request):
    if 'pk' in request.GET:
        pk = request.GET.get('pk')
        if request.method == "POST":
            form = ChartForm(request.POST or None)
            if form.is_valid():
				# This -1 is to ignore the slash at the end
                pk = pk[:-1]
                p = Chart.objects.get(pk=pk)
                p.name = form.cleaned_data['name']
                p.chart = form.cleaned_data['chart']
                p.save()
            else:
                rp = get_object_or_404(Chart, pk=pk)
                rform = ChartForm(instance=p)
                rcontext = {'form': form, 'flowchart': Chart.objects.get(pk=pk)}
        return render(request, 'flowchart/view_all_charts.html', context)
    else:
        return render(request, 'flowchart/view_all_charts.html')
