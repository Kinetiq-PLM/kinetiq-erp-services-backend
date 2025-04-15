from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/services/",
        include(
            [
                path("ticket/", include("service_ticket.urls")),
                path("call/", include("service_call.urls")),
                path("contract/", include("service_contract.urls")),
                path("request/", include("service_request.urls")),
                path("report/", include("service_report.urls")),
                path("billing/", include("service_billing.urls")),
                path("analysis/", include("service_analysis.urls")),
                path("order/", include("service_order.urls")),
                path("delivery/", include("service_delivery_order.urls")),
                path("after-analysis/", include("after_analysis.urls")),
                path("renewal/", include("warranty_renewal.urls")),
            ]
        ),
    ),
]