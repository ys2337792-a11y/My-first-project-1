from django.http import JsonResponse
from .models import Student, Complaint


# ✅ Add Complaint
def add_complaint(request):
    if request.method == "POST":
        name = request.POST.get("name")
        room = request.POST.get("room")
        complaint_text = request.POST.get("complaint")

        student, created = Student.objects.get_or_create(
            name=name,
            room_number=room
        )

        Complaint.objects.create(
            student=student,
            complaint_text=complaint_text
        )

        return JsonResponse({"message": "Complaint Submitted Successfully"})

    return JsonResponse({"error": "Invalid Request"})


# 🔍 Track Complaint
def track_complaint(request):
    name = request.GET.get("name")

    complaints = Complaint.objects.filter(student__name=name).values(
        "id", "complaint_text", "status", "created_at"
    )

    return JsonResponse(list(complaints), safe=False)


# 🔄 Update Status (Admin use)
def update_status(request, id):
    if request.method == "POST":
        complaint = Complaint.objects.get(id=id)
        complaint.status = request.POST.get("status")
        complaint.save()

        return JsonResponse({"message": "Status Updated Successfully"})

    return JsonResponse({"error": "Invalid Request"})