from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegisterView,
    PatientViewSet,
    DoctorViewSet,
    PatientDoctorMappingListCreateView,
    PatientDoctorsListView,
    PatientDoctorMappingDestroyView
)

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'doctors', DoctorViewSet, basename='doctor')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', RegisterView.as_view(), name='auth_register'), # 
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # 
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('mappings/', PatientDoctorMappingListCreateView.as_view(), name='mapping-list-create'),
    path('mappings/<int:patient_id>/', PatientDoctorsListView.as_view(), name='patient-doctors-list'), # [cite: 33]
    path('mappings/delete/<int:id>/', PatientDoctorMappingDestroyView.as_view(), name='mapping-delete'), # [cite: 35]
]