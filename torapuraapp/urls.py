from django.urls import path

from . import views
from .views import GalleryView, PlanView, PlanResultView

# URLconfのURLパターンを逆引きできるようにアプリ名を登録
app_name = "torapuraapp"

# URLパターンを登録するためのリスト
urlpatterns = [
    # http(s)://ホスト名/以下のパスが''(無し)の場合
    # viewsモジュールのIndexViewを実行
    # URLパターン名は'index'
    path("", views.IndexView.as_view(), name="index"),
    path("gallery", views.Post_List_View.as_view(), name="gallery"),
    path("contact", views.ContactView.as_view(), name="contact"),
    path("contact_user", views.ContactUserView.as_view(), name="contact_user"),
    path("contact_company", views.ContactCompanyView.as_view(), name="contact_company"),
    path("", GalleryView.as_view(), name="post_list"),
    path("plan", views.PlanView.as_view(), name="plan"),
    path("plan/result/", views.PlanResultView.as_view(), name="plan_result"),
]
