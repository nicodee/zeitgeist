# from django.contrib import admin
# from models import BlogPost
# from django import forms
# from redactor.widgets import RedactorEditor

# # class BlogPostAdmin(admin.ModelAdmin): 
 
# class BsRedactorEditor(RedactorEditor):
# 	def __init__(self, *args, **kwargs):
# 		super(BsRedactorEditor, self).__init__(*args, **kwargs)
# 		self.Media.js = (
# 			'redactor/redactor.js',
# 		)

# class BlogPostAdminForm(forms.ModelForm):
# 	class Meta:
# 		model = BlogPost
# 		widgets = {
# 		'content': BsRedactorEditor(),
# 		}
# class BlogPostAdmin(admin.ModelAdmin):
# 	form = BlogPostAdminForm
# 	list_display  = ('title', 'created', 'updated', 'content', 'publish', 'tag', 'slug')
# 	list_filter   = ('tag', 'created', 'updated', 'publish')
# 	search_fields = ['title', 'tag']

# admin.site.register(BlogPost, BlogPostAdmin)
# # admin.site.register(BlogPost, BlogPostAdminForm)