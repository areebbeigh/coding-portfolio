"""
   Copyright 2016 Areeb Beigh

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.conf import settings
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Project, Language, About, Platform


# TODO: Be able to show <code> or <pre> blocks as code in posts. - Need help with this!


def index(request):
    """ Index view, returns a list of recent projects in the context """
    recent_projects = []
    for i in range(0, 6):
        try:
            recent_projects.append(Project.objects.order_by('-publish_date')[i])
        except IndexError:
            break
    context = {
        'projects': recent_projects,
    }
    return render(request, 'index.html', context)


def project_list(request, language):
    """ Returns the projects list for a given language """
    language = get_object_or_404(Language, name=language)
    paginator = Paginator(language.project_set.order_by('-publish_date'), 6)

    if 'page' not in request.GET:
        page = 1
    else:
        page = request.GET['page']
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)

    context = {
        'projects': projects,
        'language': language,
    }
    return render(request, 'projects_page.html', context)


def project_detail(request, project_id):
    """ Returns view for individual project pages """
    project_object = get_object_or_404(Project, id=project_id)
    # Temporary, till custom website icons are supported
    website_thumbnail = settings.MEDIA_URL + "default_website_thumbnail.svg"
    context = {
        'project': project_object,
        'website_thumbnail': website_thumbnail,
    }
    return render(request, 'project_detail.html', context)


def search(request):
    """ Search view """
    if "q" in request.GET:
        queries = request.GET['q'].split()
        projects = []
        for q in queries:
            projects.extend(list(Project.objects.filter(
                Q(name__icontains=q) |
                Q(description__icontains=q) |
                Q(short_description__icontains=q))))

            for lang in Language.objects.filter(name__icontains=q):
                for project in lang.project_set.all():
                    projects.append(project)

            for platform in Platform.objects.filter(name__icontains=q):
                for project in platform.project_set.all():
                    projects.append(project)

            try:
                # If a number is given, include the project with that ID if any
                q = int(q)
                projects.append(Project.objects.get(id=q))
            except:
                pass

        projects = set(projects)

        context = {
            'projects': list(projects),
        }
        return render(request, 'search_page.html', context)
    else:
        return HttpResponseRedirect("/")


def about(request):
    """ About view """
    try:
        about = About.objects.get().description
    except:
        about = "No information here yet."

    return render(request, 'about_page.html', {'about': about})
