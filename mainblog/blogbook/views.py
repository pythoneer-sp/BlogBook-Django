from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at') # Fetch all blogs ordered by creation date in descending order
    return render(request, "blog_list.html", {"blogs":blogs}) # Render the list of blogs

def blog_create(request):
    if request.method == "POST": # Check if the request method is POST(indicating form submission)
        form = BlogForm(request.POST, request.FILES) # Create a form instance with the submitted data and any uploaded files
        if form.is_valid():
            blog = form.save(commit=False) # Save the form data but do not commit to the database yet
            blog.user = request.user # Assign the current user to the blog instance
            blog.save() # Save the blog instance to the database
            return redirect('blog_list') # Redirect to the blog list page after saving
    else:
        form = BlogForm() # If the request method is not POST, create an empty form instance
    return render(request, "blog_form.html", {"form": form}) # Render the blog_form.html template with the form for blog creation

def blog_edit(request, blog_id): # Function to edit an existing blog post
    blog = get_object_or_404(Blog, pk=blog_id, user=request.user) # Fetch the blog post or return a 404 error if not found, ensuring the logged-in user is the owner
    if request.method == "POST": # Check if the request method is POST (indicating form submission for editing)
        form = BlogForm(request.POST, request.FILES, instance=blog) # Create a form instance with the submitted data and the existing blog instance
        if form.is_valid():
            form.save(commit=False)
            blog.user = request.user # Ensure the user is still the owner of the blog post
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog) # if the request is not post, instantiate the form pre-filled with the blog data for editing
    return render(request, "blog_form.html", {"form": form})

def blog_delete(request, blog_id): # Function to delete a blog post
    blog = get_object_or_404(Blog, pk=blog_id, user = request.user) 
    if request.method == "POST": # Check if the request method is POST (indicating deletion confirmation)
        blog.delete() # Delete the blog post
        return redirect('blog_list') # Redirect to the blog list page after deletion
    return render(request, "blog_delete.html", {"blog": blog}) # Render the deletion confirmation page with the blog details