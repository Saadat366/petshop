from django.contrib import admin
from feedback.models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    model = Feedback
    list_per_page = 3
    list_display = ["id", "user", "title", "date", "answer"]
    readonly_fields = ["user", "phone_number", "email", "title", "text", "image", "date"]
    list_editable = ["answer"]