from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('upload-documents/', views.upload_documents, name='upload_documents'),  # URL pattern for document uploads
    path('delete_transcript/<int:transcript_id>/', views.delete_transcript, name='delete_transcript'),
    path('delete-document/<str:doc_type>/', views.delete_document, name='delete_document'),
    path('coursework/', views.coursework, name='coursework'),
    path('class_attendance/', views.attendance, name='class-attendance'),
    path('payment_history/', views.payments, name='payment-history'),
    path('downloads/', views.download_view, name='downloads'),
    path('menschen_a1/', views.menschen_a1, name='menschen_a1'),
    path('menschen_a2/', views.menschen_a2, name='menschen_a2'),
    path('menschen_b1/', views.menschen_b1, name='menschen_b1'),
    path('grammatik_aktiv/', views.Grammatik_Aktiv, name='grammatik_aktiv'),
    # New path for change_password view
    path('change-password/', views.change_password, name='change_password_url'),
    # New imports
    path('import-candidates/', views.import_candidates_view, name='import-candidates' )
]