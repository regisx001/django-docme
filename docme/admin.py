from django.contrib import admin
# from unfold.admin import ModelAdmin
from .models import Post, PostGroup, DocsSetting


# class PostInline(admin.StackedInline):
#     model = Post
#     exclude = ["slug"]
#     extra = 0


@admin.register(PostGroup)
class DocsPostGroup(admin.ModelAdmin):
    search_fields = ["title"]
    # inlines = [
    #     PostInline,
    # ]


@admin.register(Post)
class DocsPostAdmin(admin.ModelAdmin):
    fields = [("header", "group", "order"), "slug", "body"]
    list_display = ["header", "group", "order"]
    list_display_links = ["header"]
    readonly_fields = ["slug"]
    search_fields = ["header", "group__title"]
    list_filter = ["group"]


@admin.register(DocsSetting)
class DocsSettingAdmin(admin.ModelAdmin):
    radio_fields = {"text_size": admin.VERTICAL}

    fieldsets = (
        ("Code View", {
            "fields": (
                (("show_line_number", "text_size", "blur"), "shadow")
            ),
        }),
    )

    def has_add_permission(self, request):
        if DocsSetting.objects.all().count() == 0:
            return True
        return False
