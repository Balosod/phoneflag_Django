from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .users.views import ActivateUserEmail, UserProfile
from .homepage.views import HomePage
from .search.views import Search
from .category.views import Category
from .brand.views import Brand
from .preview.views import Preview
from .order.views import Order
from .review.views import Review
from .reply.views import Reply
from .rating.views import Rating
from .product_filter.views import FilteredProductList


router = DefaultRouter()

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api-token-auth/", views.obtain_auth_token),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("auth/users/activate/account/", ActivateUserEmail.as_view()),
    path("users/profile/", UserProfile.as_view()),
    path("marketplace/homepage/", HomePage.as_view()),
    path("marketplace/search/", Search.as_view()),
    path("marketplace/shop/category/<str:name>", Category.as_view()),
    path("marketplace/shop/category/filter/", FilteredProductList.as_view()),
    path("marketplace/shop/brand/<str:name>", Brand.as_view()),
    path("marketplace/shop/product/<int:id>", Preview.as_view()),
    path("marketplace/shop/product/order/", Order.as_view()),
    path("marketplace/shop/product/review/", Review.as_view()),
    path("marketplace/shop/product/reply/", Reply.as_view()),
    path("marketplace/shop/product/rating/", Rating.as_view()),
    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r"^$", RedirectView.as_view(url=reverse_lazy("api-root"), permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
