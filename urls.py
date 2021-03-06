from django.conf.urls import *
from django.views.generic import RedirectView
  
urlpatterns = patterns('eomf.photos.views',
    (r'^$', 'home'),
    (r'^browse/$', 'browse'),
    (r'^map/$', 'map'),
    (r'^FieldPhoto/$', 'FieldPhoto'),
    #Personalized
    (r'^cocorahs(?P<date>\w*)/$', 'cocorahs'),

    (r'^user/$', 'user_photos'),
    (r'^workset/$', 'workset_photos'),

    (r'^download/$', 'download'),
    (r'^batchedit/$', 'batchedit'),

    url(r'^upload/$', 'upload', name='upload'),
    (r'^preload/$', 'preload'),
    (r'^upload/preload/$', 'preload'),
    (r'^upload/preload/delete/(?P<name>.+)$', 'preload_delete'),
    (r'^mobile/upload/$', 'mobile_upload'), #mobile upload view
    (r'^mobile/upload2/$', 'mobile_upload2'), #mobile upload view

    url(r'^view/(?P<id>\d+)/$', 'view', name="photo-view"),
    url(r'^edit/(?P<id>\d+)/$', 'edit', name="photo-edit"),
    url(r'^delete/(?P<id>\d+)/$', 'delete', name="photo-del"),
    (r'^exif/(?P<id>\d+)/$', 'exif'),

    #Data feeds
    (r'^data.kml$','kml'),
    (r'^clusters.kml$', 'clusters'),
    (r'^clusters.php$', 'clusters'),
    (r'^photos.json$', 'photos_json'),
    (r'^photos.html$', 'photos_html'),
    (r'^photos2.html$', 'photos_html2'),
    #(r'^photos_near_coord/lat=(?P<lat>-?\d+(\.\d+)?)_lon=(?P<lon>-?\d+(\.\d+)?)_rad=(?P<radius>\d+(\.\d+)?)/$','photos_coord'),

    #Legacy redirects
    #(r'^map.php$', RedirectView.as_view(url='/photos/map/')),
    #(r'^testmap.php$', RedirectView.as_view(url='/photos/testmap/')),
    (r'^query.php$',  RedirectView.as_view(url='/photos/browse/')),
    (r'^upload.php$',  RedirectView.as_view(url='/photos/upload/')),
)

