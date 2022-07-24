"""artistsalike URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from artists_alike import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Index,name="index"),
    path('Homepage/<Email>',views.Indexpage,name="index1"),
    path('Registration',views.Userreg,name="Reg"),
    path('ArtistRegistration',views.Artistreg,name="ArtistReg"),
    path('Login',views.userlogin,name="userlogin"),
    path('User Logout',views.userlogout,name="Logout"),
    path('Artist Logout',views.artistlogout,name="ArtistLogout"),
    path('Admin Logout',views.adminlogout,name="AdminLogout"),
    path('Category', views.add_show, name="addandshow"),
    path('DeleteCategory/<int:Category_id>/', views.delete_category, name="deletecategory"),
    path('<int:Category_id>/UpdateCategory', views.update_category, name="updatecategory"),
    path('Admin', views.adminpage, name="admin"),
    path('Services/<Email>', views.services, name="Services"),
    path('ContactUs/<Email>', views.contactus, name="Contact"),
    path('Services', views.services1, name="Services1"),
    path('ContactUs', views.contactus1, name="Contact1"),
    path('ShowArtists', views.show_artists, name="show_artists"),
    path('SearchArtists', views.search_artists, name="search_artists"),
    path('SearchArtists1', views.search_artists1, name="search_artists1"),
    path('Activate/user/<int:Artist_id>/', views.activate, name='activate_artists'),
    path('Deactivate/user/<int:Artist_id>/', views.deactivate, name='deactivate_artists'),
    path('DeleteArtist/<int:Artist_id>/', views.delete_artist, name="deleteartist"),
    path('ArtistsPortfolio/<Email>', views.portfolio, name="portfolio"),
    path('Artists_Portfolio', views.portfolio1, name="portfolio1"),
    path('Feedback/<Email>/<Artist_id>/<Order_id>',views.feedback, name="feedback"),
    path('<int:Artist_id>/<Email>',views.order, name="order"),
    path('Artists/<Artist_Email>',views.artists, name="artists"),
    path('Artists',views.artists1, name="artists1"),
    path('ArtistsLogin', views.artistslogin, name="artistslogin"),
    path('AdminLogin', views.adminlogin, name="adminlogin"),
    path('View_UserOrder/<Email>', views.view_userorder, name="viewuserorder"),
    path('SearchUserOrder/<Email>', views.search_userorder, name="search_userorder"),
    path('View_ArtistOrder/<Artist_Email>', views.view_artistorder, name="viewartistorder"),
    path('View_CompleteOrder/<Artist_Email>', views.view_complete, name="viewcompleteorder"),
    path('View_PendingOrder/<Artist_Email>', views.view_pending, name="viewpendingorder"),
    path('Admin_AllOrder', views.admin_allorder, name="adminallorder"),
    path('Admin_CompleteOrder', views.admin_complete, name="admincompleteorder"),
    path('Amin_PendingOrder', views.admin_pending, name="adminpendingorder"),
    path('SearchArtistOrder/<Artist_Email>', views.search_artistorder, name="search_artistorder"),
    path('SearchFeedback/<Artist_Email>', views.search_feedback, name="search_feedback"),
    path('CancelOrder/<int:Order_id>/<Email>', views.cancel_order, name="cancel_order"),
    path('UploadOrder/<int:Order_id>/<Artist_Email>', views.upload_order, name="upload_order"),
    path('View_Feedback/<Artist_Email>', views.view_feedback, name="view_feedback"),
    path('View_Order/<int:Order_id>', views.view_order, name="view_order"),
    path('UpdateOrder<int:Order_id>/<Email>', views.update_order, name="updateorder"),
    path('View_OrderArtist/<int:Order_id>', views.view_orderartist, name="view_orderartist"),
    path('Update_Rating/<int:Artist_id>/<Artist_Email>', views.avg_rating, name="avg_rating"),
    path('ExportExcel', views.export_excel, name="export_excel"),
    path('ExportPDF', views.export_pdf, name="export_pdf"),
    path('OrderReport', views.order_report, name="order_report"),
    path('Profile/<Email>', views.profile, name="profile"),
    path('UpdateProfile/<User_id>', views.update_profile, name="updateprofile"),
    path('ArtistProfile/<Artist_Email>', views.artist_profile, name="artistprofile"),
    path('Update ArtistProfile/<Artist_id>', views.update_artistprofile, name="updateartistprofile"),


]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)