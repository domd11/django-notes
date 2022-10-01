
from pydoc import Doc
from unicodedata import category
from urllib import request
from django.views.generic import ListView
from django.shortcuts import render, redirect


# Create your views here.
from .models import Document


def editor(request):
    docid = int(request.GET.get('docid', 0))
    documents = Document.objects.all()

    if request.method == 'POST':
        docid = int(request.POST.get('docid', 0))
        title = request.POST.get('title')
        category = request.POST.get('category')
        priority = request.POST.get('priority')
        content = request.POST.get('content', '')

        if docid > 0:
            document = Document.objects.get(pk=docid)
            document.title = title
            document.content = content
            document.category = category
            document.priority = priority

            document.save()

            return redirect('/?docid=%i' % document.id)

        else:
            document = Document.objects.create(
                title=title, content=content, category=category, priority=priority)
            return redirect('/?docid=%i' % document.id)

    if docid > 0:
        document = Document.objects.get(pk=docid)
    else:
        document = ''

    context = {
        'docid': docid,
        'documents': documents,
        'document': document
    }

    return render(request, 'editor.html', context)


def delete_document(request, docid):
    document = Document.objects.get(pk=docid)
    document.delete()
    return redirect('/?docid=0')


class CatListView(ListView):
    template_name = 'category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'docs': Document.objects.filter(category=self.kwargs['category'])
        }
        return content


class PriorityView(ListView):
    template_name = 'priority.html'
    context_object_name = 'statuslist'

    def get_queryset(self):
        content = {
            'status': self.kwargs['priority'],
            'docs': Document.objects.filter(priority=self.kwargs['priority'])
        }

        return content
