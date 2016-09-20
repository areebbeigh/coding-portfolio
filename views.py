from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from coding_portfolio.models import Project, Language, About

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
    language_object = get_object_or_404(Language, name=language)
    paginator = Paginator(language_object.project_set.order_by('-publish_date'), 6)

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
    context = {
        'project': project_object,
    }
    return render(request, 'project_detail.html', context)


def search(request):
    """ Search view """
    if "q" in request.GET:
        queries = request.GET['q'].split()
        projects = []
        for q in queries:
            projects.extend(list(Project.objects.filter(name__icontains=q)))
            try:
                # If a number is given, include the project with that ID if any
                q = int(q)
                projects.extend(Project.objects.get(id=q))
            except ValueError:
                pass

        context = {
            'projects': projects,
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
