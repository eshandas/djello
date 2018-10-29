from django.urls import path

from .api_views import (
    AnomaliesDetectedAPI,
    AccountsScannedAPI,
    LogsProcessedAPI,
    PeanutsEatenAPI,
    YearlySalesAPI,
    BarChartAPI,
    RadarChartAPI,
    DoughnutChartAPI,
)

app_name = 'sample_app_api'
urlpatterns = [
    path('anomalies-detected/', AnomaliesDetectedAPI.as_view(), name='anomalies_detected'),
    path('accounts-scanned/', AccountsScannedAPI.as_view(), name='accounts_scanned'),
    path('logs-processed/', LogsProcessedAPI.as_view(), name='logs_processed'),
    path('peanuts-eaten/', PeanutsEatenAPI.as_view(), name='peanuts_eaten'),
    path('yearly-sales/', YearlySalesAPI.as_view(), name='yearly_sales'),
    path('bar-chart/', BarChartAPI.as_view(), name='bar_chart'),
    path('radar-chart/', RadarChartAPI.as_view(), name='radar_chart'),
    path('doughnut-chart/', DoughnutChartAPI.as_view(), name='doughnut_chart'),
]
